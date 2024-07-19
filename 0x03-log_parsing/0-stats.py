#!/usr/bin/python3
"""
    Script that reads stdin line by line and computes metrics
"""

import sys


def print_log_summary(status_counts: dict, total_size: int) -> None:
    """
    Prints the accumulated statistics of HTTP log entries.

    Args:
        status_counts (dict): Dictionary of counts for each status code.
        total_size (int): Total accumulated size of responses.
    """
    print("File size: {:d}".format(total_size))
    for status_code, count in sorted(status_counts.items()):
        if count:
            print(f"{status_code}: {count}")


def process_log_entries() -> None:
    """
    Continuously reads and processes log entries from stdin.
    """
    entry_count = 0
    total_file_size = 0
    status_code_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    try:
        for line in sys.stdin:
            entry_count += 1
            parts = line.split()
            try:
                code = parts[-2]
                if code in status_code_counts:
                    status_code_counts[code] += 1
            except IndexError:
                pass
            try:
                total_file_size += int(parts[-1])
            except (IndexError, ValueError):
                pass
            if entry_count % 10 == 0:
                print_log_summary(status_code_counts, total_file_size)
        print_log_summary(status_code_counts, total_file_size)
    except KeyboardInterrupt:
        print_log_summary(status_code_counts, total_file_size)
        raise


if __name__ == "__main__":
    process_log_entries()
