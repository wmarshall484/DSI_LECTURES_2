from bs4 import BeautifulSoup
import requests
import urllib
import re
from collections import Counter
import pandas as pd
import os
from sklearn.preprocessing import scale

class FedPapers(object):
    FEDERALIST_PAPERS_URL = 'http://www.let.rug.nl/usa/documents/1786-1800/the-federalist-papers/'

    def __init__(self, save_path='data/federalist_papers.pkl'):
        self.save_path = save_path
        
    def get_index(self):
        request = requests.get(self.FEDERALIST_PAPERS_URL)
        self.index_page = request

    def _parse_papers(self, response):
        soup = BeautifulSoup(response.content)
        content = soup.select('div#content')[0]
        text = content.text.lower().split()    
        return text

    def get_list(self, start_li=0, end_li=87):
        soup = BeautifulSoup(self.index_page.content, 'lxml')
        link_list = soup.findAll('li')[start_li:end_li]
        self.link_list = link_list

    def get_links(self):
        self.links = [x.find('a')['href'] for x in self.link_list]

    def get_authors(self):
        author_re = '\([JHM].*?\)'
        authors = [re.findall(author_re, x.text) for x in self.link_list]
        authors = [author[0] if author else None for author in authors]
        authors = pd.Series(authors)
        authors.name = 'Author'
        self.authors = self._fix_authors(authors)

    def get_data(self):    
        links  = [x.find('a')['href'] for x in self.link_list]

        self.pages = [requests.get(self.FEDERALIST_PAPERS_URL+link)
                      for link in self.links]
        self.data = [self._parse_papers(page) for page in self.pages]
    
        self.counts = [Counter(x) for x in self.data]
        self.data = pd.DataFrame(self.counts).fillna(0)

    def get_scaled_data(self, cols=None):
        if cols:
            return scale(self.data.loc[:,cols])
        return scale(self.data)

    def get_groups(self, groups, cols=None):
        for g in groups:
            print g
            mask = self.authors == g
            yield g, self.get_scaled_data(cols=cols)[mask]

    def _fix_authors(self, authors):
        typos = {'(Hamilt on)': '(Hamilton)',
                 '(M adison)': '(Madison)',
                 '(Ham ilton)': '(Hamilton)',
                 '(Hamilton )': '(Hamilton)'}
        return authors.replace(typos)

    def get_df(self):
        return pd.concat([self.authors, self.data], axis=1)

    def get_filtered_df(self, mask):
        mask = self.authors.isin(mask)
        return self.get_df().ix[mask,:]

    def get_all(self):
        self.get_index()
        self.get_list()
        self.get_links()
        self.get_authors()
        self.get_data()
    
    def load_data(self):
        if os.path.exists(self.save_path):
            dataframe = pd.read_pickle(self.save_path)
            self.data = dataframe.ix[:,1:]
            self.authors = dataframe.ix[:,0]
        else:
            self.get_all()
            self.get_df().to_pickle(self.save_path)
            
if __name__ == '__main__':
    fp = FedPapers()
    fp.load_data()
    
    
