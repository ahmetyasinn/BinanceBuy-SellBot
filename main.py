import time
import win32api
from binance.enums import *
from binance.client import Client

api_key = ''
api_secret = ''

client = Client(api_key,api_secret)

winRate = 1.016 # Burada %1,6 kazanma oranı belirtilmiştir.
dolarMiktar = 11.10 # işlem yapılacak, dolar cinsinden para miktarı
tur = 0

while True:
    tur = tur + 1 # Kaç defa alım satım işlemi yapacağımızı sayacak olan sayaç.

    price = client.get_ticker(symbol='BTCBUSD') # İşlem gerçekleştirilecek coin çiftleri belirlendi.
    coitime = client.get_server_time()
    coitime = time.strftime('%m/%d/%Y %H:%M:%S',
                            time.gmtime(coitime['serverTime'] / 1000.))
    pricefloat = float(price['askPrice']) # BTC/BUSD fiyatı elde edildi ve float değere çevrildi.
    coinMiktar = float(dolarMiktar) / float(pricefloat) # Burada 10 $ ile ne kadar BNB alcağımıza karar veriyoruz.
    coinMiktar = round(coinMiktar,5)
    priceCarp = float(pricefloat)*float(winRate)
    priceCarp = round(priceCarp,2)

    # Fiyat bağımsız alım işlemi yapıyoruz

    order = client.create_order(
        symbol='BTCBUSD',
        side='BUY',
        type='MARKET',
        quantity= coinMiktar
    )
    print('BTC alım işlemi gerçekleştirildi.')

    time.sleep(10)

    order = client.order_limit_sell(
        symbol='BTCBUSD',
        quantity=coinMiktar,
        price= priceCarp
        )

    print('BTC Satış Emri Verildi.')


    print(tur) # Tur sayısını ekrana basacak.
    print(coitime)
    print(coinMiktar)
    print(pricefloat)

    time.sleep(1800)




