import ast
import json
from pathlib import Path
from typing import Any, Dict


def analyze_repo(repo_root: str = ".") -> Dict[str, Any]:
    knowledge_graph = {
        "files": [],
        "dependencies": {},
        "internal_imports": {},
        "external_dependencies": set(),
        "databases": set(),
        "frameworks": set(),
        "services": set(),
        "apis": set(),
    }

    root_path = Path(repo_root)

    for py_file in root_path.rglob("*.py"):
        if (
            ".git" in py_file.parts
            or ".github" in py_file.parts
            or ".venv" in py_file.parts
            or "venv" in py_file.parts
        ):
            continue

        rel_path = str(py_file.relative_to(root_path))
        knowledge_graph["files"].append(rel_path)

        try:
            with open(py_file, "r", encoding="utf-8") as f:
                content = f.read()
                tree = ast.parse(content)

                imports = []
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for name in node.names:
                            imports.append(name.name)
                            knowledge_graph["external_dependencies"].add(
                                name.name.split(".")[0]
                            )

                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            imports.append(node.module)
                            knowledge_graph["external_dependencies"].add(
                                node.module.split(".")[0]
                            )

                knowledge_graph["internal_imports"][rel_path] = imports

                # Simple heuristic for frameworks and databases
                content_lower = content.lower()
                if "django" in content_lower:
                    knowledge_graph["frameworks"].add("Django")
                if "flask" in content_lower:
                    knowledge_graph["frameworks"].add("Flask")
                if "fastapi" in content_lower:
                    knowledge_graph["frameworks"].add("FastAPI")
                if "sqlalchemy" in content_lower:
                    knowledge_graph["databases"].add("SQLAlchemy")
                if (
                    "psycopg2" in content_lower
                    or "postgresql" in content_lower
                ):
                    knowledge_graph["databases"].add("PostgreSQL")
                if "pymongo" in content_lower or "mongodb" in content_lower:
                    knowledge_graph["databases"].add("MongoDB")
                if "sqlite3" in content_lower:
                    knowledge_graph["databases"].add("SQLite")
                if (
                    "requests" in content_lower
                    or "httpx" in content_lower
                    or "aiohttp" in content_lower
                ):
                    knowledge_graph["apis"].add("REST Client")

        except Exception as e:
            print(f"Error parsing {py_file}: {e}")

    # Convert sets to lists for JSON serialization
    for key in [
        "external_dependencies",
        "databases",
        "frameworks",
        "services",
        "apis",
    ]:
        knowledge_graph[key] = list(knowledge_graph[key])

    return knowledge_graph


if __name__ == "__main__":
    kg = analyze_repo()

    out_dir = Path(".github/automation")
    out_dir.mkdir(parents=True, exist_ok=True)

    out_file = out_dir / "knowledge_graph.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(kg, f, indent=2)

    print(f"Knowledge graph written to {out_file}")
