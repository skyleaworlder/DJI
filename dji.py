import subprocess
import argparse

parser = argparse.ArgumentParser()
group_un = parser.add_mutually_exclusive_group()

file_type = [
    { "method": "--untargz", "help": "unzip *.tar.gz" },
    { "method": "--untar", "help": "unzip *.tar" },
    { "method": "--ungz", "help": "unzip *.gz" },
    { "method": "--unzip", "help": "unzip *.zip" },
    { "method": "--unrar", "help": "unzip *.rar" },
    { "method": "--un7z", "help": "unzip *.7z" },
    { "method": "--unbz2", "help": "unzip *.bz2" },
    { "method": "--untarxz", "help": "unzip *.tar.xz" },
    { "method": "--untarbz2", "help": "unzip *.tar.bz2" }
]

parser.add_argument(
    "file_name", type=str,
    help="file name input"
)
for elem in file_type:
    group_un.add_argument(
        elem["method"], action="store_true",
        default=False, help=elem["help"]
    )

args = parser.parse_args()

if __name__ == "__main__":
    if args.untargz:
        subprocess.call("tar -xzvf "+args.file_name, shell=True)
    elif args.untar:
        subprocess.call("tar -xvf "+args.file_name, shell=True)
    elif args.ungz:
        subprocess.call("gzip -dv "+args.file_name, shell=True)
    elif args.unzip:
        subprocess.call("unzip -o "+args.file_name, shell=True)
    # unrar
    elif args.unrar:
        subprocess.call("unrar e " +args.file_name, shell=True)
    # p7zip-full
    elif args.un7z:
        subprocess.call("7z x " + args.file_name, shell=True)
    # bzip2
    elif args.unbz2:
        subprocess.call("bzip2 -d "+ args.file_name, shell=True)
    elif args.untarxz:
        subprocess.call("tar -xJvf "+args.file_name, shell=True)
    elif args.untarbz2:
        subprocess.call("tar -xjvf "+args.file_name, shell=True)
    else:
        pass