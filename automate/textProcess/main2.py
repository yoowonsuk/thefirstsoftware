from pathlib import Path

files_dir = Path('files')

merged = ''
#for filepath in files_dir.iterdir():
for index, filepath in eumerate(files_dir.iterdir()):
    with open(filepath, 'r') as file:
        #content = file.read()
        content = file.readlines()
        new_content = content[1:]
    if index == 0:
        content = "".join(content)
        merged = merged + content + '\n'
    else:
        new_content = "".join(new_content)
        merged = merged + new_content + '\n'

#print(merged)
with open('merged.csv', 'w') as file:
    file.write(merged)

with open('merged.csv', 'r') as file:
    content = file.readlines()

content[0] = 'ID,AMOUNT,COST\n'
with open('merged.csv', 'w') as file:
    file.writelines(content) # list
    # join and write string



