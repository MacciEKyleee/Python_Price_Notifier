import requests
from bs4 import BeautifulSoup
import smtplib
import time


while True:
    re = requests.get('https://helion.pl/ksiazki/python-wprowadzenie-wydanie-v-mark-lutz,pyth5v.htm#format/d')
    #print(re)

    res = re.content
    #print(res)

    soup = BeautifulSoup(res, 'html.parser')
    #print(soup.prettify())

    #price = soup.find('p', class_ = 'book-price')
    price = float(soup.find('ins', id='cena_d').text[0:3])

    if price < 120:
        print('Buy it')
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        smt.ehlo()
        smt.starttls()
        smt.login('maciej.cieszynskikyle@gmail.com', 'hfyhrwnwlvibglou')
        smt.sendmail('maciej.cieszynskikyle@gmail.com', 'map.cieszynski@gmail.com', f"Subject: DYSK SSD Notifier\n\nHi, price has dropper to {price}. Buy it!")
        smt.quit()
    time.sleep(24*60*60)  # Message send one per day
