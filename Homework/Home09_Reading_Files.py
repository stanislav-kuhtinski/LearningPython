__author__ = 'stanislav-kuhtinski'
from pathlib import Path

data_folder = Path('Files')
print('This is the path ', data_folder.cwd())
file_to_open = data_folder / "weekdays.txt"

f = open(file_to_open)

print(f.read())
