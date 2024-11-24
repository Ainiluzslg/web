import os

for root, dirs, files in os.walk('.'):
    for dir_name in dirs:
        if dir_name == '__pycache__':
            full_path = os.path.join(root, dir_name)
            print(f"Removing: {full_path}")
            os.system(f'rmdir /S /Q "{full_path}"')
