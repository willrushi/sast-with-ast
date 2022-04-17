import subprocess

def get_home_dir(username):
    stdout, stderr = subprocess.Popen(f"ls -lah /home/{username}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    
    return stdout