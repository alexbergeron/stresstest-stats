Theses are small Python scripts that take the .csv result file made by multi-mechanize after stress tests and generates results for every minute in the test.

It was created because Multi-Mechanize took too long to generate graphs on long-running benchmarks dealing with dozens of millions of transactions. I had to generate reports faster without using too much CPU resources.

The stats are regrouped for every minute of the test, so the detailed results will be less precise. The details.py generates results for every second, but uses a subset of the running time to avoid taking too much time.
