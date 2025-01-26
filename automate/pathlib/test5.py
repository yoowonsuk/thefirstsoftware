from pathlib import Path
from datetime import datetime

path = Path('files/December/a.txt')
stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")

print(stats)

root_dir = Path('files')

for path in root_dir.glob("**/*"):
    if path.is_file():
        created_date = date.fromtimestamp(path.stat().st_ctime)
        created_date_str = created_date.strftime("%Y-%m-%d_%H:%M:%S")
        new_filename = created_date_str + '_' + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)
