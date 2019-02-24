__author__ = 'stanislav-kuhtinski'
from pathlib import Path
import re
import json


def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as filehandle:
        filehandle.write(json.dumps(content, indent=4))
    print('Data has been sucessfully save to', filename)

def read_file(file_to_open):
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
    content_list = []

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
        content_dict = add_header(data)
        content_list.append(content_dict)  # append dictionary to list
    print('File {} has been sucessfully read' .format(file_to_open))
    return content_list


def add_header(my_list):
    columns = ['Timestamp', 'Status', 'Action', 'Info']
    my_dict = {}  # dictionary to store file data
    for index, elem in enumerate(my_list):
        my_dict[columns[index]] = my_list[index]
    return my_dict


data_folder = Path('Files')
file_to_read = data_folder / "example_log.log"
file_to_save = data_folder / "example_log_edited.log"
content_raw_list = read_file(file_to_read)
# print(json.dumps(content_raw_list, indent=4))  # indent - number of spaces to indent by
write_to_file(file_to_save, content_raw_list)
