#!/usr/bin/python3
"""interview questions: Log parsing"""

import sys

if __name__ == '__main__':
    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Prints the accumulated statistics.
        """
        print("File size: {:d}".format(file_size))
        for k in sorted(stats.keys()):
            if stats[k]:
                print("{}: {:d}".format(k, stats[k]))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            if len(data) < 2:
                continue
            try:
                status_code = data[-2]
                file_size = int(data[-1])

                filesize += file_size
                if status_code in stats:
                    stats[status_code] += 1
            except (ValueError, IndexError):
                continue

            if count % 10 == 0:
                print_stats(stats, filesize)

        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
