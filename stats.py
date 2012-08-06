import csv
import math
import numpy
from scipy import stats

def calcStats(times):
  tps = len(times)/60
  mean = numpy.mean(times)
  median = numpy.median(times)
  percentile_80 = stats.scoreatpercentile(times, 80)
  percentile_90 = stats.scoreatpercentile(times, 90)
  percentile_95 = stats.scoreatpercentile(times, 95)
  return [tps, mean, median, percentile_80, percentile_90, percentile_95]

statsReader = csv.reader(open('filtered.csv', 'r'), delimiter=',')
times=[]
for row in statsReader:
    sec = int(math.floor(float(row[0])))
    minutes = sec / 60
    if len(times) < minutes + 1:
        times.append([])
    times[minutes].append(float(row[1]))

stats = [calcStats(time) for time in times]

statsWriter = csv.writer(open('stats.csv', 'w'), delimiter=',')
statsWriter.writerow(['tps', 'mean', 'median', 'percentile_80', 'percentile_90', 'percentile_95'])
i = 0
for stat in stats:
    statsWriter.writerow([i] + stat)
    i += 1

