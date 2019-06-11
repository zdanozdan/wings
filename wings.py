import urllib
from bs4 import BeautifulSoup
import json,csv

def wings(link):
    f = urllib.urlopen(link)
    myfile = f.read()
    
    soup = BeautifulSoup(myfile,"html.parser")
    results = soup.find_all('script')[4].contents[0]
    results = results[14:-1]
    
    data = json.loads(results)
    print "Parsing WFL page: ",link
    results = data['data']

    for e in results:
        writer.write(e['startnumber'])
        writer.write("\t")
        writer.write(str(e['rank_global']))
        writer.write("\t")
        writer.write(e['fullname'].encode('utf8'))
        writer.write('\t')
        writer.write(e['nation'])
        writer.write('\t')
        writer.write(e['location'].encode('utf8'))
        writer.write('\t')
        writer.write(e['category_short'])
        writer.write('\t')
        writer.write(str(e['rank_type_category']))
        writer.write('\t')
        writer.write(str(e['distance']))
        writer.write("\r\n");

    next_page_url = data['next_page_url']
    print "Last page: ", data['last_page']
    return next_page_url

with open('wings.tsv', 'w') as writer:
    writer.write("\r\n")
    link = "https://results.wingsforlifeworldrun.com/pl/pl/2019?page=1";
    next_url = wings(link)
    while next_url != None:
        next_url = wings(next_url)
