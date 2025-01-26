from pathlib import Path
import zipfile

root_dir = Path('files')

for i in range(10, 21):
    filename = str(i) + ".txt"
    filepath = root_dir / Path(filename)
    filepath.touch()

root_dir = Path('files')
archive_path = root_dir / Path('archive.zip')
with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob('*.txt'):
        zf.write(path)
        path.unlink()

root_dir = Path('.')
destination = Path('destination')

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, 'r') as zf:
        #final_path = destination_path / Path(path.stem)
        zf.extractall(path=destination_path)

path = Path('destination/items1/10.csv')
print(path.absolute())

root_dir = Path(".")
search_term = '14'

for path in root_dir.rglob("*"):
    #if path.is_file():
    if search_term in path.stem:
        print(path.absolute())

root_dir = Path('destination')

for path in root_dir.glob("*.csv"):
    with open(path, 'wb') as file:
        file.write(b'')
    path.unlink()
