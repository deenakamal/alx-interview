#!/usr/bin/python3
"""reads stdin,compute metrics"""
import re


def get_input(lines):
    """gets target info from input."""
    line = lines.split(' ')
    return {
        'status_code': line[-2],
        'file_size': int(line[-1]),
    }


def print_stats(file_size_sum, status_codes_stats):
    """Print acumulated statistics of HTTP log"""
    print('File size: {:d}'.format(file_size_sum), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        n = status_codes_stats.get(status_code, 0)
        if n > 0:
            print('{:s}: {:d}'.format(status_code, n), flush=True)


def run():
    """run input parser"""
    line_n = 0
    file_size_sum = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            line_info = get_input(line)
            code = line_info.get('status_code', '0')
            if code in status_codes_stats.keys():
                status_codes_stats[code] += 1
            file_size_sum += line_info['file_size']
            line_n += 1
            if line_n % 10 == 0:
                print_stats(file_size_sum, status_codes_stats)
    except (KeyboardInterrupt, EOFError, SystemExit):
        print_stats(file_size_sum, status_codes_stats)


if __name__ == '__main__':
    run()
