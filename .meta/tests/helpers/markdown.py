import os
import sys
import re
from urllib.parse import unquote
from pathlib import Path

import mistune

from bs4 import BeautifulSoup
from . import BASE_DIR


HTTP_PATTERN = r'^https?:\/\/'


project_tests = list()

def list_to_dict(ul):
    result = {}
    for li in ul.find_all("li", recursive=False):
        key = next(li.stripped_strings)
        ul = li.find("ul")
        if ul:
            result[key] = list_to_dict(ul)
        else:
            if li.find('a'):
                result[key] = li.a['href']
            else:
                result[key] = None
    return result

def find_markdown_lists(markdown):
    markdown_parser = mistune.Markdown()    
    html_string = markdown_parser(markdown)
    html = BeautifulSoup(html_string, 'html.parser')
    lists =  html.find_all('ul', recursive=False)
    
    return [list_to_dict(_list) for _list in lists]

def validate_file_exists(path_to_file):
    return (
        os.path.exists(os.path.join(BASE_DIR, path_to_file)) \
        and os.path.isfile(os.path.join(BASE_DIR, path_to_file))
    )

def parse_list_dict(_dict, depth_name=''):
    links = {}

    for key, value in _dict.items():
        if type(value) == dict:
            normal_name = re.sub(r'[^a-zA-Z0-9]+', '', key.title())
            links[key] = parse_list_dict(
                value, 
                depth_name + f'{normal_name}::'
            )
        else:
            if depth_name == '':
                depth_name = 'Global::'

            temp = (f'{depth_name[:-2]}', key, value)
            project_tests.append(temp)
            links[key] = temp
    
    return links

def parse_lists(lists):
    if len(lists):
        for _list  in lists:
            parse_list_dict(_list)

def get_completed_list_items(lists):
    parse_lists(lists)

    tests = []
    for namespace, name, path in project_tests:
        if path is not None:
            if not re.match(HTTP_PATTERN, path):
                path = os.path.normpath(path)
                if validate_file_exists(path):
                    tests.append(('Passed', f'{namespace} for file "{path}"'))

            elif re.match(HTTP_PATTERN, path) and Path(BASE_DIR).name in path:
                path = os.sep.join(re.sub(HTTP_PATTERN, '', path).split(os.sep)[5:])
                path = os.path.normpath(unquote(path))

                if validate_file_exists(path):
                    tests.append(('Passed', f'{namespace} for file "{path}"'))
                else:
                    tests.append(('Failed', f'{namespace} for file "{path}"'))
        else:
            tests.append(('Failed', namespace))
    

    return tests