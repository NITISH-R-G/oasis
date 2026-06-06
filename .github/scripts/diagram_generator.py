import json
from pathlib import Path


def generate_mermaid_dependency_graph(kg: dict) -> str:
    lines = ["graph TD;"]

    # Internal dependencies
    internal_imports = kg.get("internal_imports", {})
    for src_file, imports in internal_imports.items():
        src_node = src_file.replace("/", "_").replace(".", "_")

        # Clickable node to source file
        github_url = f"https://github.com/camel-ai/oasis/blob/main/{src_file}"
        lines.append(f'    {src_node}["{src_file}"]')
        lines.append(f'    click {src_node} "{github_url}" "View source"')

        for imp in imports:
            if not imp:
                continue
            # Basic matching for internal files (very simplistic)
            imp_node = imp.replace(".", "_")
            # If external dependency, represent differently
            ext_deps = kg.get("external_dependencies", [])
            if imp.split(".")[0] in ext_deps:
                lines.append(f'    {imp_node}(("{imp}"))')
            else:
                lines.append(f'    {imp_node}["{imp}"]')

            lines.append(f"    {src_node} --> {imp_node}")

    # Databases and Frameworks
    for db in kg.get("databases", []):
        db_node = f"db_{db.lower()}"
        lines.append(f"    {db_node}[({db})]")

    for fw in kg.get("frameworks", []):
        fw_node = f"fw_{fw.lower()}"
        lines.append(f'    {fw_node}{{"{fw}"}}')

    return "\n".join(lines)


def generate_architecture_markdown(kg: dict) -> str:
    mermaid_graph = generate_mermaid_dependency_graph(kg)

    content = f"""# Repository Architecture

## Dependency Graph
```mermaid
{mermaid_graph}
```

## Discovered Technologies
* **Frameworks**: {', '.join(kg.get('frameworks', [])) or 'None detected'}
* **Databases**: {', '.join(kg.get('databases', [])) or 'None detected'}
* **APIs**: {', '.join(kg.get('apis', [])) or 'None detected'}

## External Dependencies
{', '.join(kg.get('external_dependencies', []))}
"""
    return content


if __name__ == "__main__":
    kg_path = Path(".github/automation/knowledge_graph.json")
    if not kg_path.exists():
        print("Knowledge graph not found. Run repo_analyzer.py first.")
        exit(1)

    with open(kg_path, "r", encoding="utf-8") as f:
        kg = json.load(f)

    markdown_content = generate_architecture_markdown(kg)

    out_dir = Path("docs/architecture")
    out_dir.mkdir(parents=True, exist_ok=True)

    out_file = out_dir / "architecture.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Architecture documentation and diagrams written to {out_file}")
