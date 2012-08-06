import csv
import math
import numpy
from scipy import stats

def calcStats(times):
  tps = len(times)
  mean = numpy.mean(times)
  median = numpy.median(times)
  percentile_99 = stats.scoreatpercentile(times, 99)
  return [tps, mean, median, percentile_99]

statsReader = csv.reader(open('filtered.csv', 'r'), delimiter=',')
times=[]
for row in statsReader:
    sec = int(math.floor(float(row[0])))
    while len(times) < sec + 1:
        times.append([])
    times[sec].append(float(row[1]))

stats = [calcStats(time) for time in times[32730:32790]]

statsWriter = csv.writer(open('detailed.csv', 'w'), delimiter=',')
i = 0
for stat in stats:
    statsWriter.writerow(stat)
    i += 1

