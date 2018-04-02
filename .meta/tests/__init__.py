import os
import time
import sys
from functools import reduce
from collections import Counter

import anybadge

from colorama import Fore, Style
from tests.helpers import markdown, BASE_DIR

def check_readme():
    with open(os.path.join(BASE_DIR, 'README.md')) as file:
        lists = markdown.find_markdown_lists(file.read())
        files = markdown.get_completed_list_items(lists)
        return files

def generate_coverage_badge(coverage):
    badge_path = os.path.join(BASE_DIR, '.meta', 'media', 'coverage.svg')
    badge = anybadge.Badge(
        'coverage', 
        coverage, 
        thresholds = {
            50: 'red' ,
            60: 'orange', 
            80: 'yellow',
            100: 'green'
        },
        value_suffix='%'
    )
    os.remove(badge_path)
    badge.write_badge(badge_path)

def generate_output(verbose=False):
    # Measure test time
    t = time.perf_counter()
    files = check_readme()
    elapsed_time = time.perf_counter() - t

    # Display test information
    for file in files:
        if file[0].casefold() == 'failed':
            print(f'{Fore.RED}FAILED !! {file[1]} {Style.RESET_ALL}')
        elif file[0].casefold() == 'passed' and verbose:
            print(f'{Fore.GREEN}PASSED :: {file[1]} {Style.RESET_ALL}')

    passed = [file for file in files if file[0].casefold() == 'passed']
    failed = [file for file in files if file[0].casefold() == 'failed']

    print(f'\n{Fore.YELLOW}Ran for {int(elapsed_time * 1000)} millisecond(s)')
    print(f'{Fore.GREEN}Passed {len(passed)} test(s)')
    print(f'{Fore.RED}Failed {len(failed)} test(s)')

    # Calculate the coverage
    coverage = int(len(passed) / (len(passed) + len(failed)) * 100)

    # Print it nice
    if coverage <= 50:
        print(f'{Fore.RED}', end='')
    elif 50 < coverage <= 75:
        print(f'{Fore.YELLOW}', end='')
    elif coverage > 75:
        print(f'{Fore.GREEN}', end='')
    print(f'\nTotal Documentation Coverage {coverage}%', end=' ')
    print(f'{Style.RESET_ALL}\n')

    # Generate a badge
    generate_coverage_badge(coverage)

    # Exit depending on failed tests, for CI
    if len(failed) > 0:
        sys.exit(-1)
    else:
        sys.exit(0)