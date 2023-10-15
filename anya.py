import requests
url = 'https://www.lamoda.ru/catalogsearch/result/?q=%D1%88%D1%82%D0%B0%D0%BD%D1%8B+%D0%BA%D0%B0%D1%80%D0%B3%D0%BE&submit=y&gender_section=women&sort=price_asc'
r = requests.get(url)
text = r.text

n_in = text.find('</h2><span class="d-catalog-header__product-counter">')
text = text[n_in+53:]

n_out = text.find('товар')
number = str(text[:n_out])
print(number)

url1 = 'https://www.lamoda.ru/p/mp002xw0102n/clothes-tvoe-bryuki/'
r1 = requests.get(url1)
text1 = r1.text
with open ('sakd.txt', 'w', encoding='utf-8') as f:
    print(text1, file=f)



country_in = text1.find('"title":"Страна производства","value":')

text1 = text1[country_in+39:]

country_out = text1.find('"')
country = text1[:country_out]
print(country)

discount_in = text1.find('"discount_lamoda_and_loyalty_and_action"')
if discount_in != -1:
    text1 = text1[discount_in+41:]
    discount_out = text1.find(',')
    discount = text1[:discount_out]
    print(discount)
else:
    discount = 0
    print(discount)
'''
for page in range(1, pages+1):
    url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc' + '&page=' + str(page)
    print(url)
    r = requests.get(url)
    text = r.text
    if page == pages:
        l = num - (pages-1)*60
    for _ in range(l):
        i = text.find('<div class="x-product-card__card"><a href="')
        text = text[i + 43:]
        j = text.find('" class=')
        end_url = text[:j]
        url = 'https://www.lamoda.ru/' + end_url
        text = text[j:]
        all_urls.append(url)
'''