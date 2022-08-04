"""DuckDuckGo URL scrapper lib"""
from time import sleep

from requests_html import HTMLSession


class DDG:
    """DuckDuckGo scrapper class"""
    def __init__(self, keywords, max_results=None) -> None:
        self.session = HTMLSession()
        self.ddg_url = 'https://html.duckduckgo.com/html/'
        self.req_data = {'q': keywords}
        self.req_headers = {
            'Content-Type': 'application/x-www-form-urlencoded'}
        self.keywords = keywords
        self.max_results = max_results
        self.selector = 'html body.body--html div div\
            div.serp__results div#links.results div.nav-link form input'
        self.links = []
        """Empty variables used in the future"""
        self.sess_req = ""
        self.req = ""

    def search(self) -> list:
        """Search function"""
        self.req = self.session.post(
            self.ddg_url, data=self.req_data, headers=self.req_headers)

        for link in self.req.html.absolute_links:
            if link not in self.links and 'ad_provider' not in link:
                self.links.append(link)

        while self.req.html.find(self.selector):
            attrs = self.req.html.find(self.selector)

            self.req_data['s'] = attrs[2].attrs['value']
            self.req_data['nextParams'] = attrs[3].attrs['value']
            self.req_data['v'] = attrs[4].attrs['value']
            self.req_data['o'] = attrs[5].attrs['value']
            self.req_data['dc'] = attrs[6].attrs['value']
            self.req_data['api'] = attrs[7].attrs['value']
            self.req_data['vqd'] = attrs[8].attrs['value']
            self.req_data['kl'] = attrs[9].attrs['value']

            self.sess_req = self.session.post(
                self.ddg_url, data=self.req_data, headers=self.req_headers)
            for link in self.sess_req.html.absolute_links:
                if link not in self.links and 'ad_provider' not in link:
                    self.links.append(link)

            if self.max_results is not None and self.max_results <= len(self.links):
                return self.links[0:self.max_results]
            sleep(0.2)
        return self.links
