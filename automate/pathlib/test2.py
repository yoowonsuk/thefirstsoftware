from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.iterdir()
#print(list(file_paths))
print(Path.cwd())
for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    #new_filepath = Path(new_filename)
    new_filepath = path.with_name(new_filename)
    print(new_filepath) #new-abc.txt
    path.rename(new_filepath)
