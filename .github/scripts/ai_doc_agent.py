import json
import os
import subprocess
from pathlib import Path


def get_git_diff() -> str:
    try:
        # Get diff of the current working tree against HEAD
        # Or diff between previous commits if running in CI
        result = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD"], capture_output=True, text=True
        )
        return result.stdout
    except Exception as e:
        print(f"Error getting git diff: {e}")
        return ""


def generate_fallback_documentation(diff: str, kg: dict):
    print(
        "Using fallback documentation generator (No OpenAI API key provided)"
    )

    # Simple changelog update based on changed files
    changed_files = []
    for line in diff.split("\n"):
        if line.startswith("diff --git"):
            parts = line.split(" ")
            if len(parts) >= 3:
                changed_files.append(parts[2][2:])

    # Update README simply
    readme_path = Path("README.md")

    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        start_marker = "## Auto-Generated Changelog"

        # Build new text
        new_text = ""
        if changed_files:
            files_str = ', '.join(changed_files[:5])
            new_text += f"* Automated update detected changes in: {files_str}"
            if len(changed_files) > 5:
                new_text += f" and {len(changed_files)-5} other files."
            new_text += "\n"

        if start_marker in content:
            parts = content.split(start_marker)
            before = parts[0]
            next_section_idx = parts[1].find("\n## ")
            if next_section_idx != -1:
                after = parts[1][next_section_idx:]
            else:
                after = ""
            content = before + start_marker + "\n\n" + new_text + "\n" + after
        else:
            content += "\n\n" + start_marker + "\n\n" + new_text + "\n"

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated README.md with fallback generator.")


def call_openai_for_docs(diff: str, kg: dict, api_key: str):
    print(
        "Calling OpenAI API to generate intelligent documentation updates..."
    )
    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        prompt = f"""
        You are an AI Repo Maintainer. Analyze the graph and git diff,
        and provide a concise update.

        Knowledge Graph Summary:
        Frameworks: {', '.join(kg.get('frameworks', []))}
        Databases: {', '.join(kg.get('databases', []))}

        Git Diff:
        {diff[:2000]}

        Output format: A short Markdown snippet summarizing recent changes.
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful documentation agent.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
        )

        update = response.choices[0].message.content

        readme_path = Path("README.md")
        if readme_path.exists():
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()

            # If section exists, replace it to avoid endless appending
            start_marker = "## AI Documentation Agent Update"
            if start_marker in content:
                # Find the next section or end of file
                parts = content.split(start_marker)
                before = parts[0]

                # Assume a new section starts with '## '
                next_section_idx = parts[1].find("\n## ")
                if next_section_idx != -1:
                    after = parts[1][next_section_idx:]
                else:
                    after = ""

                content = (
                    before + start_marker + "\n\n" +
                    update + "\n" + after
                )
            else:
                content += (
                    "\n\n" + start_marker + "\n\n" + update + "\n"
                )

            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Updated README.md via OpenAI.")

    except ImportError:
        print(
            "OpenAI package not installed. "
            "Falling back to template gen."
        )
        generate_fallback_documentation(diff, kg)
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        generate_fallback_documentation(diff, kg)


if __name__ == "__main__":
    kg_path = Path(".github/automation/knowledge_graph.json")
    kg = {}
    if kg_path.exists():
        with open(kg_path, "r", encoding="utf-8") as f:
            kg = json.load(f)

    diff = get_git_diff()

    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        call_openai_for_docs(diff, kg, api_key)
    else:
        generate_fallback_documentation(diff, kg)
