import sys
import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        current_time = datetime.datetime.now() + datetime.timedelta(days=1)
        print("{0}\t{1}\t{2}".format(item, cost, current_time))
