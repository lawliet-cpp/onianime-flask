
from bs4 import BeautifulSoup
import requests


def get_anime_watch_link(query, episode):
    base_link = 'https://animeblkom.net'
    response = requests.get(base_link + '/search?query='+query)

    soup = BeautifulSoup(response.content, 'html5lib')

    soup.prettify()

    anime_div = soup.find('div', attrs={'class': 'name'})
    link = anime_div.a['href']
    response2 = requests.get(f'{base_link}{link}/{str(episode)}')
    print(response2.content)
    soup2 = BeautifulSoup(response2.content, 'html5lib')
    iframe = soup2.find('iframe')

    return iframe['src']


def get_download_link(anime_name, episode):
    response = requests.get(
        f'https://animelek.me/episode/{anime_name}-{episode}-الحلقة')

    soup = BeautifulSoup(response.content, 'html5lib')
    soup.prettify()
    downloads = soup.find('div', attrs={'id': 'downloads'})

    links = downloads.find_all('li', attrs={'class': 'watch'})
    download_links = []
    for link in links:
        anime = {
            'link': link.a["href"],
            'name': link.a.text
        }
        download_links.append(anime)

    return download_links
