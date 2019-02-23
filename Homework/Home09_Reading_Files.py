__author__ = 'stanislav-kuhtinski'
from pathlib import Path
import re
import json

data_folder = Path('Files')
file_to_open = data_folder / "example_log.log"
try:
    my_file = open(file_to_open)
except Exception as error:
    print("File not found or path is incorrect ", error)

regex_for_timestamp = r'\d{2}/\d{2}.\d{2}:\d{2}:\d{2}'
regex_for_status = r'[A-Z]+\s+:|[A-Z]+:{1}'
regex_for_action = r'[a-z]+_[a-z]+'
regex_for_loginfo = r':{1}\s[a-z]*.*'
regex_del_from_status = r':*\s*:'
regex_del_from_txt = r':{1}\s'
columns = ['Timestamp', 'Status', 'Action', 'Text']
my_list = []
my_dict = {}  # dictionary to store file data

# Get next line from file
while True:
    # Get next line from file
    line = my_file.readline()
    # If line is empty then end of file reached
    if not line:
        break;
    status = re.findall(regex_for_status, line)
    log_info = re.findall(regex_for_loginfo, line)
    data = re.findall(regex_for_timestamp, line) \
           + [re.sub(regex_del_from_status, '', i) for i in status] \
           + re.findall(regex_for_action, line) \
           + [re.sub(regex_del_from_txt, '', i) for i in log_info]
    for index, elem in enumerate(data):
        my_dict[columns[index]] = data[index]

    my_list.append(my_dict)  # append dictionary to list
    print(json.dumps(my_list, indent=4))  # indent - number of spaces to indent by

# Close Close
my_file.close()
