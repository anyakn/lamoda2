
import requests
import math

query = input('Введите запрос: ')
query = query.replace(' ', '+')
query = query.lower()

url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc'
r = requests.get(url)
text = r.text

num_in = text.find('</h2><span class="d-catalog-header__product-counter">')
text = text[num_in+53:]
num_out = text.find('товар')
num = int(text[:num_out])
print(num)

pages = math.ceil(num/60)
print(pages)

all_urls = []
for page in range(1, pages):
    url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc' + '&page=' + str(page)
    print(url)
    r = requests.get(url)
    text = r.text
    for _ in range(60):
        i = text.find('<div class="x-product-card__card"><a href="')
        text = text[i + 43:]
        j = text.find('" class=')
        end_url = text[:j]
        url = 'https://www.lamoda.ru/' + end_url
        text = text[j:]
        all_urls.append(url)
print(all_urls)
print(len(all_urls))


all_prices = []

for n in range(len(all_urls)):
    url = all_urls[n]
    html = requests.get(url)
    text = html.text
    price_in = text.find('x-product-card-description__price-WEB8507_price_no_bold')
    text = text[price_in + 20:]
    price_out = text.find('₽')
    price = text[:price_out]
    all_prices.append(price)



print(all_prices)




'''''
all_prices = []
for n in range(60):
    url = all_urls[n]
    html = requests.get(url)
    text = html.text
    price_in = text.find('"price":"')
    text = text[price_in + 9:]
    price_out = text.find('"},"original"')
    price = text[:price_out]
    all_prices.append(price)
print(all_prices)

all_brands = []
for n in range(60):
    url = all_urls[n]
    html = requests.get(url)
    text = html.text
    brand_in = text.find(':"Другие товары ')
    text = text[brand_in + 16:]
    brand_out = text.find('","type":"brand"')
    brand = text[:brand_out]
    all_brands.append(brand)
print(all_brands)
'''''