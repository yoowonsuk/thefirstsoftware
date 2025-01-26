from pathlib import Path

root_dir = Path('files')

for path in rood_dir.glob("**/*"):
    if path.is_file():
        parent_folder = path.parts
        subfolders = path.parts[1:-1] # change all occruences : command F2
        print(subfolders)

        new_filename = "-".join(subfolders) + '-' + path.name
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)
