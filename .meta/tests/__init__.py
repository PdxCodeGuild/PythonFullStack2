import os
import time
import sys
from functools import reduce
from collections import Counter
from colorama import Fore, Style
from tests.helpers import markdown, BASE_DIR

def check_readme():
    with open(os.path.join(BASE_DIR, 'README.md')) as file:
        lists = markdown.find_markdown_lists(file.read())
        files = markdown.get_completed_list_items(lists)
        return files

def generate_output(verbose=False):

    t = time.process_time()
    files = check_readme()
    elapsed_time = time.process_time() - t

    for file in files:
        if file[0].casefold() == 'failed':
            print(f'{Fore.RED}FAILED !! {file[1]} {Style.RESET_ALL}')
        elif file[0].casefold() == 'passed' and verbose:
            print(f'{Fore.GREEN}PASSED :: {file[1]} {Style.RESET_ALL}')

    passed = [file for file in files if file[0].casefold() == 'passed']
    failed = [file for file in files if file[0].casefold() == 'failed']

    print(f'\n{Fore.YELLOW}Ran for {elapsed_time}s\n')
    print(f'{Fore.GREEN}Passed {len(passed)} test(s)')
    print(f'{Fore.RED}Failed {len(failed)} test(s)')

    coverage = int(len(passed) / (len(passed) + len(failed)) * 100)

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