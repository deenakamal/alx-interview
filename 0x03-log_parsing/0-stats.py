#!/usr/bin/python3
"""Reads stdin line by line and computes HTTP log metrics."""
import re


def parse_log_entry(entry):
    """
    Extract relevant information from a single log entry.

    Args:
        entry (str): A line from the HTTP log input.

    Returns:
        dict: Contains 'response_code' and 'response_size'.
    """
    parts = entry.split(' ')
    return {
        'response_code': parts[-2],
        'response_size': int(parts[-1]),
    }


def display_summary(total_size, response_counts):
    """
    Display accumulated statistics of HTTP log entries.

    Args:
        total_size (int): Total accumulated size of responses.
        response_counts (dict): Dictionary of counts for each status code.
    """
    print(f'Total size: {total_size}', flush=True)
    for code in sorted(response_counts.keys()):
        count = response_counts.get(code, 0)
        if count > 0:
            print(f'{code}: {count}', flush=True)


def process_logs():
    """
    Continuously read and process log entries from stdin.
    """
    entry_count = 0
    total_size = 0
    response_counts = {
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
            log_entry = input()
            entry_data = parse_log_entry(log_entry)
            response_code = entry_data.get('response_code', '0')
            if response_code in response_counts:
                response_counts[response_code] += 1
            total_size += entry_data['response_size']
            entry_count += 1
            if entry_count % 10 == 0:
                display_summary(total_size, response_counts)
    except (KeyboardInterrupt, EOFError, SystemExit):
        display_summary(total_size, response_counts)


if __name__ == '__main__':
    process_logs()
