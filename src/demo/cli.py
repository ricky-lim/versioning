import importlib.metadata
import tomllib
from pathlib import Path


def app():
    print(f"Version: {get_version()}")

def get_version() -> str:
    """Get the version"""
    try:
        # First try to get version from package metadata (installed mode)
        return importlib.metadata.version("versioning")
    except importlib.metadata.PackageNotFoundError:
        # Fallback to pyproject.toml for development mode
        pyproject_path = Path(__file__).parent / "pyproject.toml"
        try:
            with open(pyproject_path, "rb") as f:
                pyproject = tomllib.load(f)
            return pyproject["project"]["version"]
        except (FileNotFoundError, KeyError):
            return "unknown"


if __name__ == "__main__":
    app()
