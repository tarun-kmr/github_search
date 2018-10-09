import urllib2
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup



url = "https://github.com/search?q="

def searchparse(query):
    page = urllib2.urlopen(url+query)
    soup = BeautifulSoup(page)

    repositories_data = []
    res = soup.find('ul', attrs={'class' : 'repo-list'})
    if res:
        content_list = res.find_all(
            'div', attrs={'class' : 'repo-list-item'}
        )

        for content in content_list:
            repo_map = {}
            repo_map['repo_name'] = content.find('a') and \
                content.find('a').text
            repo_map['description'] = content.find('p') and \
                content.find('p').text
            repo_map['updated'] = content.find('relative-time') and \
                content.find('relative-time').text

            licensed_by = content.find('div', attrs={'class' : 'flex-wrap'})
            if licensed_by:
                repo_map['licensed_by'] = licensed_by.findChildren('p') and \
                    licensed_by.findChildren('p')[0].text

            repositories_data.append(repo_map)
    return repositories_data

