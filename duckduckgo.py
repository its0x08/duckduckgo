from requests import post
from lxml import html
from time import sleep

def search(keywords, max_results=None):
	count = 0
	while True:
		doc = html.fromstring(post("https://duckduckgo.com/html/", data = {'q': keywords,'s': '0'}).text)
		res = [a.get('href') for a in doc.cssselect('#links .links_main a')]
		for result in res:
			yield result
			sleep(0.1)
			count += 1
			if max_results and count >= max_results:
				return
		try:
			form = doc.cssselect('.results_links_more form')[-1]
		except IndexError:
			return
		params = dict(form.fields)


