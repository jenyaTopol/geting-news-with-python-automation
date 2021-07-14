#first install thelibrary=====> pip install GoogleNews
from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews = GoogleNews(period= '1d')
googlenews.search('USA')#or any other contry that you are interested
result = googlenews.result()
for x in result:
    print("-" * 10)
    print('Title--', x['title'])
    print('Date/Time--', x['date'])
    print('Description--', x['desc'])
    print('lins--', x['link'])
