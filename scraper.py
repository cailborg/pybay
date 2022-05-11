import requests
import pandas as pd
page = requests.get("https://www.ebay.com.au/sch/Music/11233/i.html?_from=R40&_fosrp=1&_nkw=son+lux+tomorrows+vinyl&_in_kw=1&_ex_kw=&_sacat=11233&_mPrRngCbx=1&_udlo=20&_udhi=100&_ftrt=901&_ftrv=1&_sabdlo=&_sabdhi=&_samilow=&_samihi=&_sadis=15&_stpos=2261&_fsradio2=%26LH_PrefLoc%3D1&_sargn=-1%26saslc%3D2&_salic=15&LH_SubLocation=1&_fss=1&_saslop=1&_sasl=&_fsradio=LH_SellerWithStore%3D1&_sop=15&_dmd=1&_ipg=60")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="ResultSetItems")

titles = []
prices = []
shippings = []
urls = []

import re
def find_numbers(string, ints=True):            
    numexp = re.compile(r'[-]?\d[\d,]*[\.]?[\d{2}]*') #optional - in front
    numbers = numexp.findall(string)    
    numbers = [float(x.replace(',','')) for x in numbers]
    if ints is True:
        return [int(x.replace(',','').split('.')[0]) for x in numbers]            
    else:
        return numbers

for items in results.find_all(class_="sresult", limit=5):
    title = items.find(class_="lvtitle").get_text(strip=True)
    price = find_numbers(items.find(class_="lvprice").get_text(strip=True), ints=False)
    shipping = find_numbers(items.find(class_="fee").get_text(strip=True), ints=False)
    url = items.find("a" , href=True)

    titles.append(title)
    prices.append(*price)
    shippings.append(*shipping)
    urls.append(url['href'])

totals = [x+y for x,y in zip(prices,shippings)]
print(prices)
print(shippings)
print(totals)

mylst = pd.DataFrame({'Product name: ':titles, 'Price: ':prices, 'Shipping: ':shippings, 'Total: ':totals, 'URL: ':urls})
mylst.to_csv("output.csv")