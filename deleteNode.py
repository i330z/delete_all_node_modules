import os

def remove_node_modules(path):
    for root, dirs, files in os.walk(path):
        if "node_modules" in dirs:
            node_modules_dir = os.path.join(root, "node_modules")
            try:
                print(f"Removing {node_modules_dir}")
                for dirpath, dirnames, filenames in os.walk(node_modules_dir, topdown=False):
                    for dirname in dirnames:
                        dir_path = os.path.join(dirpath, dirname)
                        os.rmdir(dir_path)
                os.rmdir(node_modules_dir)
            except Exception as e:
                print(f"Error removing {node_modules_dir}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path to start scanning: ")
    if os.path.exists(folder_path):
        remove_node_modules(folder_path)
        print("Done")
    else:
        print("Folder not found.")
