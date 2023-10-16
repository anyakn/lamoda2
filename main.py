'''
Кнопова Анна-
Каролина Балан - 65 б.
Шилкова Ульяна - 50 б.
'''

import pandas as pd
import requests
import math
import local_ru as ru

query = input(ru.qry)
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
all_prices = []
for page in range(1, pages+1):
    url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc' + '&page=' + str(page)
    print(url)
    r = requests.get(url)
    text = r.text
    if page == pages:
        k = num - (pages - 1) * 60
    else:
        k = 60
    for _ in range(k):
        i = text.find('<div class="x-product-card__card"><a href="')
        text = text[i + 43:]
        j = text.find('" class=')
        end_url = text[:j]
        url = 'https://www.lamoda.ru/' + end_url
        text = text[j:]
        all_urls.append(url)

        price_in = text.find('x-product-card-description__price-WEB8507_price_no_bold')
        text = text[price_in+124:]
        price_out = text.find('₽')
        price = text[:price_out]
        all_prices.append(price)


all_brands = []
all_articuls = []
all_countries = []
all_discounts = []
all_names = []

for n in range(len(all_urls)):
    url = all_urls[n]
    html = requests.get(url)
    text = html.text

    if text.find('<div class="x-premium-product-title-new__model-name">') == -1:
        names_in = text.find('<div class="x-premium-product-title__model-name">')
        text = text[names_in + 49:]
    else:
        names_in = text.find('<div class="x-premium-product-title-new__model-name">')
        text = text[names_in + 53:]
    names_out = text.find('</div></h1><div class')
    name = text[:names_out]
    all_names.append(name)

    brand_in = text.find(':"Другие товары ')
    text = text[brand_in + 16:]
    brand_out = text.find('","type":"brand"')
    brand = text[:brand_out]
    all_brands.append(brand)

    articul_in = text.find('[{"key":"sku","title":"Артикул","value":"')
    text = text[articul_in + 41:]
    articul_out = text.find('"},{"key":')
    articul = text[:articul_out]
    all_articuls.append(articul)

    country_in = text.find('"title":"Страна производства","value":')
    text = text[country_in + 39:]
    country_out = text.find('"')
    country = text[:country_out]
    all_countries.append(country)

    discount_in = text.find('"discount_lamoda_and_loyalty_and_action"')
    if discount_in != -1:
        text = text[discount_in + 41:]
        discount_out = text.find(',')
        discount = text[:discount_out]
    else:
        discount = 0
    all_discounts.append(discount)

print(all_brands)
print('')
print(all_articuls)
print('')
print(all_countries)
print('')
print(all_prices)
print('')
print(all_discounts)
print('')
print(all_names)
print('')

data = { ru.nm: all_names, ru.art: all_articuls, ru.pr: all_prices,
        ru.dsc: all_discounts, ru.brd: all_brands, ru.cr: all_countries}

df = pd.DataFrame(data)
pd.set_option('display.max_columns', 7)

with open('output.txt', 'w', encoding='utf8') as f_out:
    print(df, file=f_out)
