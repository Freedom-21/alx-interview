#!/usr/bin/python3
"""interview questions: Log parsing"""

import sys

if __name__ == '__main__':
    total_file_size = 0
    status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    valid_status_codes = set(status_code_counts.keys())
    line_count = 0

    def print_stats():
        """
        Prints the accumulated statistics.
        """
        print("File size: {:d}".format(total_file_size))
        for code in sorted(status_code_counts.keys()):
            if status_code_counts[code] > 0:
                print("{}: {:d}".format(code, status_code_counts[code]))

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) < 7:
                continue

            try:
                file_size = int(parts[-1])
                status_code = parts[-2]

                total_file_size += file_size
                if status_code in valid_status_codes:
                    status_code_counts[status_code] += 1
            except ValueError:
                continue

            if line_count % 10 == 0:
                print_stats()

        print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
