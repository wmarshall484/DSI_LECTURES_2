import requests
from bs4 import BeautifulSoup
import urlparse
import os
import sys
import urllib

def get_gallery_links_for_species(species_code):
    base_url = 'https://www.wildflower.org/gallery/species.php'
    url = '{}?id_plant={}'.format(base_url, species_code)
    page_src = requests.get(url).text
    soup = BeautifulSoup(page_src, 'html5lib')
    content = soup.find('div', id='fullpage_content')
    tables = content.findAll('table')
    links = [urlparse.urljoin(base_url, table.find('a')['href']) for table in tables]
    return links

def get_full_image_url_from_gallery(gallery_link):
    page_src = requests.get(gallery_link).text
    soup = BeautifulSoup(page_src, 'html5lib')
    center = soup.find('center')
    return center.find('img')['src']

def download_image_of_species(species_code):
    links = get_gallery_links_for_species(species_code)
    for i, link in enumerate(links):
        img_url = get_full_image_url_from_gallery(link)
        extension = os.path.splitext(urlparse.urlparse(img_url).path)[1]
        filename = '{}_{}{}'.format(species_code, i, extension)
        urllib.urlretrieve(img_url, filename)

if __name__ == '__main__':
    try: os.mkdir('data')
    except OSError: pass
    os.chdir('data')
    download_image_of_species(sys.argv[1])
