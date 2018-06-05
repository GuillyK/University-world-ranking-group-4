import urllib.request
import dryscrape
import bs4 as bs
import csv

my_url = 'https://www.timeshighereducation.com/world-university-rankings/2018/world-ranking#!/page/0/length/25/sort_by/rank/sort_order/asc/cols/stats'
session = dryscrape.Session()
session.visit(my_url)
response = session.body()
csvfile = '/home/topteulen/Desktop/codeer_opdrachten/test.csv'


soup = bs.BeautifulSoup(response, 'html.parser')

rows = soup.find('tbody')


table = [[cells.text for cells in rows("td")] for rows in soup("tr")]

print(table)
with open("output.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerows(table)

#https://stackoverflow.com/questions/18544634/convert-a-html-table-to-json
