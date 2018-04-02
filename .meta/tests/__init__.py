import os
import sys
from functools import reduce
from collections import Counter
from colorama import Fore, Style
from tests.helpers import markdown, BASE_DIR

def check_readme():
    with open(os.path.join(BASE_DIR, 'README.md')) as file:
        list_items = markdown.find_markdown_list_items(file)
        files = markdown.calculate_completed_list_items(list_items)
        return files

def generate_output(verbose=False):
    files = check_readme()
    for file in files:
        if file[0].casefold() == 'failed':
            print(f'{Fore.RED}FAILED :: {file[1]} {Style.RESET_ALL}')
        elif file[0].casefold() == 'passed' and verbose:
            print(f'{Fore.GREEN}PASSED :: {file[1]} {Style.RESET_ALL}')

    failed = [file for file in files if file[0].casefold() == 'failed']
    passed = [file for file in files if file[0].casefold() == 'passed']

    coverage = int(len(failed) / len(files) * 100)
    if coverage <= 50:
        print(f'{Fore.RED}', end='')
    elif 50 < coverage <= 75:
        print(f'{Fore.YELLOW}', end='')
    elif coverage > 75:
        print(f'{Fore.GREEN}', end='')
    print(f'\nTotal Documentation Coverage {coverage}%', end=' ')
    print(f'{Style.RESET_ALL}\n')

    if len(failed) > 0:
        sys.exit(-1)
    else:
        sys.exit(0)