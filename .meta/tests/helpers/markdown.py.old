import re
import os
import sys
from urllib.parse import unquote
from pathlib import Path

from . import BASE_DIR

PARSE_LINK_PATTERN = r'\[(.+)\]\s?\((.+)\)'
LIST_ITEM_PATTERN = r'^(\s+)?\-(\s+)?'
HTTP_PATTERN = r'^https?:\/\/'

# TODO:
# Fix nested list issue.
# Determine depth inside of markdown lists.
#

def find_markdown_list_items(file):   
    return [line for line in file.readlines() if re.match(LIST_ITEM_PATTERN, line)]

def validate_file_exists(path_to_file):
    return (
        os.path.exists(os.path.join(BASE_DIR, path_to_file)) \
        and os.path.isfile(os.path.join(BASE_DIR, path_to_file))
    )

def calculate_completed_list_items(list_items):
    tests = list()
    for item in list_items:
        depth = re.findall(r'^\s+', item)
        item = re.sub(LIST_ITEM_PATTERN, '', item)
        print(depth)

        links = re.findall(PARSE_LINK_PATTERN, item)

        if len(links):
            name = links[0][0].title().strip()
            path = links[0][1]

            if not re.match(HTTP_PATTERN, path):
                path = os.path.normpath(path)
                if validate_file_exists(path):
                    tests.append(('Passed', (name, path)))

            elif re.match(HTTP_PATTERN, path) and Path(BASE_DIR).name in path:
                path = os.sep.join(re.sub(HTTP_PATTERN, '', path).split(os.sep)[5:])
                path = os.path.normpath(unquote(path))

                if validate_file_exists(path):
                    tests.append(('Passed', (name, path)))
                else:
                    tests.append(('Failed', name.title()))
                    
        else:
            tests.append(('Failed', item.strip().title()))

    return tests