commands = [
    "sudo apt-get install python3-pip"
]

def main():
    import subprocess
    import os

    if os.geteuid() == 0:
        for i in commands:
            print(f"Running >>> {i}")
            subprocess.run(i, shell=True)

        with open("requirements.txt") as f:
            req = f.read().split()

        for i in req:
            subprocess.run(f"pip install {i}", shell=True)

        print("\u001b[32m\u001b[1mInstall complete\u001b[0m\n\u001b[31m\u001b[1mMake sure to have serial enabled\u001b[0m")
    else:
        print("Please give permisions before running script")

if __name__ == "__main__":
    main()