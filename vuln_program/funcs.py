from utilities import get_home_dir

def my_func(username):
    print(f"This is the home directory of the user you entered:")
    print(get_home_dir(username).decode("utf-8"))