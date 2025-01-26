with open('file3.csv', 'r') as file:
    content = file.read()

#print(content[:-1])
modified_content = content[:-1]
with open('file3-new.csv', 'w') as file:
    file.write(modified_content)


from pathlib import Path
files_dir = Path('files')
print(files_dir) # files

for filepaths in files_dir.iterdir()
    #print(filepaths)
    with open(filepath, 'r') as file:
        content = file.read()
        new_content = content[:-1]
        # new_content = content.replace('amount', 'units') # dir(str)

    with open(filepath, 'w') as file:
        file.write(new_content)


# cp -a files/ files_backup
