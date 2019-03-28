import requests

# fetch data from  API
response = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
data = response.json()
best_bid=data['bid']
best_ask=data['ask']
print('bid bitbay:',best_bid,'ask bitbay:',best_ask)

#TASKS (11p)
#To use the requests library you have to install it first. If you have pip and you're using python3 interpreter in your project
# then simply pip3 install requests

# 1 Find another public API with cryptocurrency and compare prices. As an output print:
# "Currently the XXX exchange market is better for buying whilst YYY is better for selling" (3p)
odpowiedz=requests.get("http://api.nbp.pl/api/exchangerates/rates/c/usd/2019-03-28/?format=json")
informacje=odpowiedz.json()
kupno=informacje['rates'][0]['ask']
response1=requests.get("https://api.crex24.com/v2/public/tickers?instrument=BTC-USD")
data1=response1.json()
bid=data1[0]['bid']
ask=data1[0]['ask']
rynek1='BITBAY'
rynek2='CREX24'
print("bid crex24:",bid*kupno, "ask crex24:", ask*kupno)
if bid*kupno>best_bid:
    if ask*kupno>best_ask:
        print(f"Currently the {rynek1} exchange market is better for buying whilst {rynek2} is better for selling")
        kozakbid=bid*kupno
    elif ask*kupno<best_ask:
        print(f"Currently the {rynek2} exchange market is better for buying and also {rynek2} is better for selling")
        kozakbid = bid * kupno
else:
    if ask*kupno>best_ask:
        print(f"Currently the {rynek1} exchange market is better for buying and also {rynek1} is better for selling")
        kozakbid = best_bid
    elif ask*kupno<best_ask:
        print(f"Currently the {rynek2} exchange market is better for buying whilst {rynek1} is better for selling")
        kozakbid = best_bid

# 2 Use https://randomuser.me API to download a random user data.
# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)

import random
lista={}
indeksy=[]

for key in range(1,100):
    y = True
    while y==True:
        try:
            response_user = requests.get("https://randomuser.me/api/?inc=id,name,login")
            uzytkownik = response_user.json()
            username = uzytkownik['results'][0]['login']['username']
            name = uzytkownik['results'][0]['name']['first']
            last_name = uzytkownik['results'][0]['name']['last']
            godnosc = name + ' ' + last_name
            id = uzytkownik['results'][0]['id']['value']
            kozak={'username':username,'name':godnosc,'id':id,'BTC':random.uniform(.5,2.5),'PLN':random.randint(20000,50000)}
            lista[key]=kozak
            y=False
        except:
            pass

import pprint
pprint.pprint(lista)



# 3 Prepare a simulation of transactions between these users
# Take random user and pair him/her with another one. Assume a random amount but take real world price. Sum up the transaction printing:
# username1 exchanged X.XXX BTC with username2 for PLN YYYYY.YYY PLN. (2p)
# Simulate real time - do not proceed all transactions at once. Try to make around 100 transactions per minute (2p)
# Simulate user's assets. Creating a user assign random amount of a given currency. Take it into account while performing a transaction.
# Remember to amend user's assets after the transaction. (2p)

import random
import time
username = 'username'
BTC = 'BTC'
PLN = 'PLN'
for i in range(100):
    ilosc = 10000
    indeks1 = random.randint(1, 99)
    while lista[indeks1][PLN]<2500:
        indeks1=random.randint(1,99)
    indeks2=indeks1
    while indeks2==indeks1 or lista[indeks2][BTC]<0.15:
        indeks2=random.randint(1,99)
    while lista[indeks1]['PLN'] < ilosc*kozakbid or lista[indeks2]['BTC'] < ilosc:
        ilosc=random.random()
    cena=ilosc*kozakbid
    lista[indeks1][BTC] +=ilosc
    lista[indeks1][PLN] -= cena
    lista[indeks2][BTC] -= ilosc
    lista[indeks2][PLN] += cena
    print(f'użytkownik {lista[indeks1][username]} kupił od użytkownika {lista[indeks2][username]} '
          f'{ilosc}BTC za sumę {cena}zlotych. '
          f'Aktualne zasoby użytkownika {lista[indeks1][username]} to: BTC:{lista[indeks1][BTC]} PLN: {lista[indeks1][PLN]} '
          f'Aktualne zasoby użytkownika {lista[indeks2][username]} to: BTC:{lista[indeks2][BTC]} PLN: {lista[indeks2][PLN]} ')


    time.sleep(3/5)
pprint.pprint(lista)


