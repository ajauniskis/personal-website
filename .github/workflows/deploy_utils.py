import sys


def disable_debugging():
    WARNING = "\033[93m"
    ENDC = "\033[0m"
    with open(f"./personal_website/settings.py") as f:
        file = f.read()
        if "DEBUG = True" not in file:
            print(f"{WARNING}Debugging already disabled{ENDC}")
            return

    with open("./personal_website/settings.py", "w") as f:
        print(f"{WARNING}Disabling debugging{ENDC}")
        file = file.replace("DEBUG = True", "DEBUG = False")
        f.write(file)


if __name__ == "__main__":
    globals()[sys.argv[1]]()
