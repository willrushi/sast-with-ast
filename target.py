import subprocess
import sys

if __name__ == "__main__":
    str1 = "hello world"
    str1 = str1.replace("world", "planet")
    print(str1)

    str2 = sys.argv[1]

    subprocess.Popen("id", shell=True).communicate()
    subprocess.Popen(str2).communicate()
    subprocess.Popen(str2, shell=True).communicate()
