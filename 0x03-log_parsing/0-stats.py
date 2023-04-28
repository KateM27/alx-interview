#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import sys
import random
from time import sleep
import datetime

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

# testing script
for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \
                     \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
                        random.randint(1, 255), random.randint(1, 255),
                        random.randint(1, 255), random.randint(1, 255),
                        datetime.datetime.now(),
                        random.choice([200, 301, 400, 401, 403,
                                       404, 405, 500]),
                        random.randint(1, 1024)
    ))
    sys.stdout.flush()
