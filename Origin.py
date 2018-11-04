from urllib.request import Request, urlopen
import requests
import csv
import time

count = 0
while True:
    r = requests.get(url='https://api.coindesk.com/v1/bpi/currentprice.json').json()
    data = {}
    data['time'] = r['time']['updated']
    data['price'] = r['bpi']['USD']['rate']
    count += 1
    
    print(count)             
    hold = []
    if count == 1:
        reader = csv.reader(open('btcprice.csv', 'r'))
        for i in reader:
            hold.append(i)
        try:
            if data['time'] != hold[-2][0]:
                with open('btcprice.csv', 'a') as f:
                    w = csv.DictWriter(f, data.keys())
                    w.writerow(data)
        except IndexError:
            with open('btcprice.csv', 'a') as f:
                w = csv.DictWriter(f, data.keys())
                w.writerow(data)
            
    if count > 1:
        if data != datahold:
            print(data)
            with open('btcprice.csv', 'a') as f:
                w = csv.DictWriter(f, data.keys())
                w.writerow(data)
    datahold = data
    time.sleep(15)

