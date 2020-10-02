import os


# print(os.getcwd())
file_path = os.path.abspath(__file__)
file_dir_name = os.path.dirname(file_path)


parent_dir_name = os.path.dirname(file_dir_name)
print(parent_dir_name)
os.chdir(parent_dir_name)
print(os.getcwd())

