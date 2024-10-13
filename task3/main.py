import sys
from pathlib import Path
from colorama import Fore, Style


def print_directory_structure(path: Path, prefix: str = ""):
    """Recursively prints the directory structure with colored output."""
    if not path.exists():
        print(f"Error: The path {path} does not exist.")
        return
    if not path.is_dir():
        print(f"Error: The path {path} is not a directory.")
        return

    for item in path.iterdir():
        if item.is_dir():
            try:
                print(f"{prefix}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                print_directory_structure(item, prefix + "  ")
            except PermissionError:
                print(f"{prefix}{Fore.RED}{"  Access denied"}{Style.RESET_ALL}")
        else:
            print(f"{prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 main.py /path/to/directory")
        sys.exit(1)

    directory_path = Path(__file__).parent / Path(sys.argv[1])
    print_directory_structure(directory_path)
