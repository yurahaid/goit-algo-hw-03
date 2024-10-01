import os
from pathlib import Path
import shutil



def copy_files(from_path: str, dist: str = "dist"):
    path = Path(from_path)
    try:
        for resource in path.iterdir():
            if Path(resource).is_dir():
                copy_files(resource)
            else:
                try:
                    copy_into(resource, dist)
                except Exception as e:
                    print(f'can`t copy file {resource} got error {e}')
    except Exception as e:
        print(f'can`t iterate over {from_path} got error {e}')





def copy_into(file: str, dist: str):
    ext = Path(file).suffix
    if len(ext) == 0:
        return
    dist_dir = Path(os.path.join(dist, ext))
    if not dist_dir.exists():
        dist_dir.mkdir(parents=True)

    shutil.copy(file, str(dist_dir))

def parse_input(user_input: str):
    from_dir, *args = user_input.split()
    to_dir = "dist"
    if len(args) > 0:
        to_dir = args[0]

    return from_dir, to_dir




from_path, to_path= parse_input(input("Enter form and to directories: "))

copy_files(from_path, to_path)