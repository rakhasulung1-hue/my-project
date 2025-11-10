import subprocess
import sys

# daftar package yang ingin dipastikan terinstal
packages = [
    "colorama",
    "art",
    "dos2unix",
    "pathlib"
]

def install(package_name):
    #install Package Jika User Belum mempunyai Package nya
    try:
        __import__(package_name)
        print(f"{package_name} Is finish .")
    except ImportError:
        print(f"Waiting For Installing {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f" {package_name} is Fisnish Instaling")

# cek semua package di list
for pkg in packages:
    install(pkg)

# contoh penggunaan salah satu modul
from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.GREEN + "All Package is Ready,")
