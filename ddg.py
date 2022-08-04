#!/usr/bin/env python
"""DuckDuckGo URL scrapper"""
from argparse import ArgumentParser
from time import time

from lib.duckduckgo import DDG

if __name__ == '__main__':
	try:
		t = time()

		arguments = ArgumentParser(
			description='DuckDuckGo URL scraper by 0x08')
		arguments.add_argument('keyword', metavar='keyword',
							   type=str, nargs='+', help='search string')
		arguments.add_argument('-n', dest='max_results', type=int,
							   help='number of results (default: all)')
		arguments.add_argument(
			'-t', dest='time', const=True, help='execution time')

		args = arguments.parse_args()

		ddg = DDG(' '.join(args.keyword), max_results=args.max_results)
		search = ddg.search()
		for link in sorted(search):
			print(link)

		if args.time:
			print(f'Execution time: {time()-t:.2f}s')
	except KeyboardInterrupt:
		print('\nCtrl+C was pressed!')
