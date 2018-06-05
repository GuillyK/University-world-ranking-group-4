
import urllib.request
import bs4 as bs
import dryscrape

my_url = 'https://www.timeshighereducation.com/world-university-rankings/2018/world-ranking#!/page/0/length/25/sort_by/rank/sort_order/asc/cols/stats'
session = dryscrape.Session()
session.visit(my_url)
response = session.body()



soup = bs.BeautifulSoup(response, 'html.parser')

rows = soup.find('tbody')


for row in rows:
    cols = row.find_all('td')
    print(cols)
