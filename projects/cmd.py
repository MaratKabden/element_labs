import os

current_dir = "C:/"

def list_directories():
    print(os.listdir(current_dir))

def change_directory(directory):
    global current_dir
    if directory == "..":
        current_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    else:
        new_dir = os.path.join(current_dir, directory)
        if os.path.isdir(new_dir):
            current_dir = new_dir
        else:
            raise Exception(f"{directory} not found")

def create_directory(directory):
    os.makedirs(os.path.join(current_dir, directory))

def delete_directory(directory):
    os.rmdir(os.path.join(current_dir, directory))

def rename_directory(old_name, new_name):
    os.rename(os.path.join(current_dir, old_name), os.path.join(current_dir, new_name))

def view_file(file_name):
    file_path = os.path.join(current_dir, file_name)
    if os.path.isfile(file_path):
        if file_name.endswith(".txt"):
            with open(file_path, "r") as f:
                print(f.read())
        elif file_name.endswith(".md"):
            with open(file_path, "r") as f:
                print(f.read())
        else:
            raise Exception(f"File type not supported")
    else:
        raise Exception(f"{file_name} not found")

while True:
    user_input = input(current_dir + ">").strip()
    if user_input == "ls" or user_input == "dir":
        list_directories()
    elif user_input.startswith("cd "):
        change_directory(user_input.split(" ")[1])
    elif user_input.startswith("mkdir "):
        create_directory(user_input.split(" ")[1])
    elif user_input.startswith("rmdir "):
        delete_directory(user_input.split(" ")[1])
    elif user_input.startswith("rename "):
        old_name, new_name = user_input.split(" ")[1:]
        rename_directory(old_name, new_name)
    elif user_input.startswith("view "):
        view_file(user_input.split(" ")[1])
    else:
        print("Invalid command")
