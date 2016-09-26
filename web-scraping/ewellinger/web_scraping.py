from IPython.core.display import HTML
from pymongo import MongoClient
from bs4 import BeautifulSoup, UnicodeDammit
from requests import get


def query_indeed(job_title, city, state):
    '''
    INPUT:
        job_title: str
        city: str
        state: str
    OUTPUT:
        requests.models.Response
    '''
    job_title = job_title.replace(' ', '+')
    url = 'http://www.indeed.com/jobs?q={0}&l={1}%2C+{2}'.format(job_title, city, state)
    response = get(url)
    if response.status_code != 200:
        print 'WARNING', response.status_code
    else:
        return response


def extract_post(post):
    '''
    INPUT:
        post: bs4.element.Tag
    OUTPUT:
        insert: dict
    '''
    try:
        title = post.find('a', attrs={'data-tn-element': 'jobTitle'}).text
    except:
        print 'ERROR EXTRACTING TITLE'
        return None
    try:
        loc = post.find('span', attrs={'class': 'location'}).text
    except:
        print 'ERROR EXTRACTING LOCATION'
        return None
    try:
        desc = post.find('span', attrs={'class': 'summary'}).text
    except:
        print 'ERROR EXTRACTING DESCRIPTION'
        return None
    insert = {'title': title,
              'location': loc,
              'description': desc}
    return insert



if __name__=='__main__':
    # # Create a instance of the MongoClient
    # client = MongoClient()
    # # Initialize the database
    # db = client['test_database']
    # # Initialize table
    # tab = db['job_desc']

    html = query_indeed('Data Scientist', 'Denver', 'CO')

    # html is the response to our query.  We can access the raw HTML by printing the content
    print html.content

    # Ew, that's no good.  BeautifulSoup to the rescue!
    soup = BeautifulSoup(html.content, 'html.parser')
    print soup.prettify()

    # That's better, but this still includes a lot of stuff we don't care about...
    # Maybe we want to get all of the job titles on the first page
    postings = soup.findAll('div', attrs={'class': 'row'})
    titles = [post.find('a', attrs={'data-tn-element': 'jobTitle'}).text for post in postings]
    print titles
