#!/usr/bin/env python
"""DuckDuckGo URL scrapper"""
from argparse import ArgumentParser, BooleanOptionalAction
from time import time

from lib.duckduckgo import DDG

if __name__ == '__main__':
	try:
		start_time = time()

		arguments = ArgumentParser(description='DuckDuckGo URL scraper by 0x08')
		arguments.add_argument('keyword', metavar='keyword', type=str, help='search string')
		arguments.add_argument('-n', dest='max_results', type=int, help='number of results (default: all)')
		arguments.add_argument('-t', dest='time', action=BooleanOptionalAction, default=False, help='execution time')
		arguments.add_argument('-o', dest='file_output', type=str, help='save output to file')

		args = arguments.parse_args()

		ddg = DDG(' '.join(args.keyword), max_results=args.max_results)
		search = ddg.search()
		for link in sorted(search):
			print(link)

		if args.time:
			print(f'Execution time: {time()-start_time:.2f}s')
		elif args.file_output:
			with open(args.file_output, mode='w', encoding='utf-8') as file_output:
				file_output.write('\n'.join(sorted(search)))
				file_output.write('\n')

	except KeyboardInterrupt:
		print('\nCtrl+C was pressed!')
