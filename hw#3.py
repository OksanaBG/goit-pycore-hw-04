import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def print_directory_structure(path: Path, prefix: str = ''):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}|_{item.name}/")
                print_directory_structure(item, prefix + '    ')
            else:
                #file 
                print(f"{prefix}{Fore.GREEN}|_{item.name}")
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Permission Denied] {path}")

def main():
    #Get the path as argv - if not from intput 
    if len(sys.argv) > 1:
        path_str = sys.argv[1]
    else:
        path_str = input("Please enter the path to folder:>>> ")

    path = Path(path_str)

    # Cheking if it is a folder
    if not path.exists():
        print(f"{Fore.RED}Error:>>> The path on exists")
        sys.exit(1)
    if not path.is_dir():
        print(f"{Fore.RED}Error: The path is not a folder.")
        sys.exit(1)

    print(f"{Fore.YELLOW}The structure of folder:>>> {path.resolve()}")
    print_directory_structure(path)

if __name__ == "__main__":
    main()