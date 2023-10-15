import pandas as pd

all_brands = ['Svoboda Baby', 'Солнце и Луна', 'Ecolatier', 'Planeta Organica', 'Ecolatier', 'Ecolatier', 'Алиса', 'AQA baby', 'EO laboratorie', 'Солнце и Луна', 'Dr. Tuttelle', 'Green Mama', 'Ecolatier', 'Ecolatier', 'Чистая Линия', 'Алиса', 'Natura Siberica', 'Natura Siberica', 'Natura Siberica', 'Ecolatier', 'Organic Kitchen', 'AQA baby', 'Onme', 'Onme', 'Onme', 'Dr. Tuttelle', 'Dr. Tuttelle', 'Dr. Tuttelle', 'Natura Siberica', 'Dr. Tuttelle', 'Organic Kitchen', 'Compagnie de Provence', 'Dr. Tuttelle', 'AQA baby', 'Laboratorium', 'Laboratorium', 'Laboratorium', 'Planeta Organica', 'Natura Siberica', 'Natura Siberica', 'Morgans', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Lion', 'Pusy', 'Nesti Dante', 'Nesti Dante', 'Nesti Dante', 'Planeta Organica', 'La Corvette', 'Pigeon', 'Floid', 'Floid', 'Natura Siberica', 'Bioderma', 'Natura Siberica', 'HerbOlive', 'Saltrain', 'Acca Kappa', 'Acca Kappa', 'Acca Kappa', 'Acca Kappa', 'Bioderma', 'Press Gurwitz Perfumerie', 'Pigeon', 'Press Gurwitz Perfumerie', 'Press Gurwitz Perfumerie', 'Pigeon', 'Haan', 'Haan', 'Haan', 'Haan', 'Giardino Magico', 'Giardino Magico', 'Babe Laboratorios', 'Biothal', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'Compagnie de Provence', 'La Corvette', 'La Corvette', 'La Corvette', 'Natura Siberica', 'Acca Kappa', 'La Corvette', 'Number(13)', "I'm From", "I'm From", 'Grown Alchemist', 'Hobepergh Asiago', 'Tonka', 'Nesti Dante', 'SA.AL\\u0026CO', 'Grown Alchemist', 'Morgans', 'Tangent GC', 'Tangent GC', 'Margaret Dabbs', 'La Corvette', 'La Corvette', 'La Corvette', 'La Corvette', 'Hobepergh Asiago', 'Grown Alchemist', 'La Sultane de Saba', 'La Sultane de Saba']

all_articuls = ['RTLACN152001', 'RTLACZ520101', 'RTLACD122601', 'RTLABK763401', 'RTLACO475301', 'RTLACO475401', 'RTLACN160901', 'RTLADA542901', 'RTLACT237001', 'RTLACZ520001', 'RTLADA547101', 'RTLACX678302', 'RTLACD125001', 'RTLACD124801', 'RTLABO093501', 'RTLACN160301', 'NA026LWLQC34', 'NA026LWLQC36', 'RTLAAE818101', 'RTLABO085601', 'OR013LWJTDP8', 'RTLADA543001', 'MP002XU059IK', 'MP002XU059HJ', 'MP002XU059HP', 'RTLADA545501', 'RTLAAY960101', 'RTLAAY960301', 'RTLABZ486901', 'RTLADA546501', 'RTLADA217101', 'CO100LWMJCM8', 'RTLADA547001', 'RTLADA543701', 'MP002XU0517B', 'MP002XU0517C', 'MP002XU0517D', 'RTLABY632201', 'RTLACK717701', 'RTLAAE817101', 'MP002XU0DWUM', 'MP002XU051ZI', 'MP002XU051ZR', 'MP002XU051ZN', 'MP002XU051ZC', 'MP002XU051ZO', 'MP002XU051ZL', 'MP002XU0CSEA', 'MP002XU051ZS', 'MP002XU051ZQ', 'MP002XU051ZK', 'MP002XU00QBN', 'MP002XU051Z9', 'MP002XU051Z8', 'MP002XC012JS', 'MP002XU00056', 'MP002XU051Z3', 'MP002XU051Z1', 'MP002XU051YY', 'RTLABK766601', 'MP002XU050F0', 'RTLACZ749301', 'RTLADA679201', 'RTLADA679001', 'RTLADB519601', 'BI046LUKUGO7', 'RTLACC906301', 'MP002XU04VC8', 'MP002XU0CVXX', 'RTLABP685701', 'RTLABP685601', 'AC001LMCUGC6', 'AC001LUDWBR2', 'BI046LUKUGU1', 'MP002XU05EBZ', 'RTLACZ750101', 'MP002XU04Z96', 'MP002XU04Z8W', 'RTLACZ749901', 'MP002XW0JMTB', 'MP002XW0JMT9', 'MP002XW0JMTA', 'MP002XW0JMTE', 'RTLACU510301', 'RTLACU509701', 'MP002XW035LC', 'MP002XW031LW', 'CO100LUJTEA9', 'CO100LUJTEA7', 'CO100LUJTEA6', 'CO100LUJTEA8', 'CO100LUJTEA5', 'CO100LUJTEA4', 'RTLABV806101', 'RTLABV806201', 'RTLABV806301', 'CO100LUJTDY0', 'RTLABO317401', 'CO100LUJTDY1', 'CO100LUJTEC7', 'RTLABO317501', 'MP002XU04JAQ', 'MP002XU054IF', 'MP002XU03J5S', 'RTLACP758301', 'AC001LMCUGC3', 'MP002XU050ET', 'MP002XU00Q7T', 'MP002XU00QM1', 'MP002XU00QM5', 'RTLACY321701', 'RTLACY401701', 'MP002XU05E6X', 'MP002XU0CSE6', 'RTLACX184901', 'RTLACY325601', 'MP002XM1H62H', 'RTLAAO017901', 'RTLAAO017301', 'RTLAAC846001', 'MP002XU050EX', 'MP002XU050EZ', 'MP002XU03N9I', 'MP002XU03JBI', 'RTLACY400801', 'RTLADA556901', 'MP002XW0FFJU', 'MP002XW0FFK5']

all_countries = ['Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Китай', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Франция', 'Китай', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Россия', 'Соединенное Королевство', 'Италия', 'Италия', 'Италия', 'Италия', 'Италия', 'Италия', 'Италия', 'Италия', 'Италия', 'Италия', 'Италия', 'Италия', 'Италия', 'Таиланд', 'Россия', 'Италия', 'Италия', 'Италия', 'Россия', 'Франция', 'Япония', 'Италия', 'Италия', 'Россия', 'Франция', 'Россия', 'Греция', 'Корея, Республика', 'Италия', 'Италия', 'Италия', 'Италия', 'Франция', 'Россия', 'Япония', 'Россия', 'Россия', 'Япония', 'Испания', 'Испания', 'Испания', 'Испания', 'Россия', 'Россия', 'Испания', 'Россия', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Франция', 'Россия', 'Италия', 'Франция', 'Россия', 'Корея, Республика', 'Корея, Республика', 'Австралия', 'Италия', 'Россия', 'Италия', 'Австрия', 'Австралия', 'Соединенное Королевство', 'Франция', 'Франция', 'Соединенное Королевство', 'Франция', 'Франция', 'Франция', 'Франция', 'Италия', 'Австралия', 'Франция', 'Франция']

all_prices = ['208 ', '225 ', '255 ', '270 ', '272 ', '272 ', '272 ', '280 ', '281 ', '308 ', '310 ', '320 ', '323 ', '323 ', '328 ', '332 ', '340 ', '340 ', '340 ', '340 ', '344 ', '350 ', '376 ', '376 ', '376 ', '380 ', '400 ', '400 ', '408 ', '410 ', '432 ', '495 ', '510 ', '520 ', '529 ', '529 ', '529 ', '530 ', '612 ', '660 ', '699 ', '699 ', '699 ', '699 ', '699 ', '699 ', '699 ', '699 ', '699 ', '699 ', '699 ', '699 ', '724 ', '724 ', '768 ', '790 ', '804 ', '804 ', '819 ', '820 ', '837 ', '863 ', '890 ', '890 ', '960 ', '980 ', '1 003 ', '1 180 ', '1 200 ', '1 220 ', '1 220 ', '1 290 ', '1 290 ', '1 370 ', '1 380 ', '1 388 ', '1 450 ', '1 450 ', '1 455 ', '1 495 ', '1 495 ', '1 495 ', '1 495 ', '1 500 ', '1 500 ', '1 620 ', '1 690 ', '1 815 ', '1 815 ', '1 815 ', '1 815 ', '1 815 ', '1 815 ', '1 815 ', '1 815 ', '1 815 ', '1 898 ', '1 898 ', '1 898 ', '1 898 ', '1 898 ', '1 977 ', '1 977 ', '1 995 ', '2 020 ', '2 300 ', '2 337 ', '2 400 ', '2 490 ', '2 490 ', '2 600 ', '2 775 ', '2 900 ', '2 934 ', '2 970 ', '3 200 ', '3 260 ', '3 500 ', '3 500 ', '3 850 ', '3 895 ', '3 895 ', '3 995 ', '3 995 ', '4 425 ', '4 590 ', '7 480 ', '7 480 ']

all_discounts = ['20', '25', '15', 0, '15', '15', '15', 0, '15', '25', 0, 0, '15', '15', '20', '15', '15', '15', '15', '15', '20', 0, '39', '39', '39', 0, 0, 0, '15', 0, '20', '25', 0, 0, 0, 0, 0, 0, '15', 0, 0, '5', '5', '5', '9', '5', '5', '9', '5', '5', '5', '9', '15', '15', '20', '38', '15', '15', '14', 0, '40', '25', 0, 0, 0, 0, '15', 0, 0, 0, 0, 0, 0, 0, 0, '25', '19', '19', '25', 0, 0, 0, 0, 0, 0, '25', 0, '25', '25', '25', '25', '25', '25', '25', '25', '25', '25', '25', '25', '25', '25', '40', '40', 0, 0, 0, '40', 0, 0, 0, 0, '25', 0, '10', '25', 0, 0, 0, 0, 0, 0, 0, 0, 0, '25', 0, 0, 0]

all_names = ['Мыло -крем для младенца 0+, 250 мл', 'Пена для купания от макушки до пяток Календула и ромашка 0+ флакон/дозатор, 265 мл (2 шт.)', 'Мыло -крем, "Мягкий уход", 0+, 250 мл', 'Мыло Pure для рук, 300 мл', 'Мыло для тела и волос "Питание & Восстановление" ORGANIC COCONUT, 350 мл', 'Мыло для тела и волос "Глубокое восстановление" ORGANIC ARGANA, 350 мл', 'Набор для ухода за телом жидкое мыло для детей "Чистота и защита ручек", 300 мл + крем детский "Нежный уход", 45 мл', 'Жидкое мыло для малыша, 250 мл', 'Жидкое мыло -крем, 300 мл', 'Жидкое мыло детское, 500мл (2 шт.)', 'Жидкое мыло с экстрактами ромашки и алоэ вера, 250 мл', 'Крем для тела "алоэ и экстракт овса", 300 мл', 'Жидкое мыло для рук мандарин & мята, 400 мл', 'Жидкое мыло для рук алоэ & миндальное молочко, 400 мл', 'Жидкое мыло БЕРЕЗОВОЕ ДЛЯ ВСЕЙ СЕМЬИ 520 мл', 'Жидкое мыло 2 шт. "Чистота и защита ручек", 300 мл', 'Мыло жидкое Увлажняющее, 500 мл', 'Мыло жидкое Питательное, 500 мл', 'Гель для душа Fresh SPA home Нежное мыло для тела "Арджунская баня", 170 мл', "Средство для интимной гигиены Крем-мыло Girls' Friendly Бережный уход для девочек с 3-х лет, 250 мл", 'Жидкое мыло "Ничего\xa0личного, просто\xa0мыло" by\xa0F\xa0Magazine, 300 мл', 'Жидкое мыло для малыша, 400 мл', 'Жидкое мыло «Лаванда и можжевельник», 400 мл', 'Жидкое мыло «Иланг-иланг и шалфей», 400 мл', 'Жидкое мыло «Кардамон и ваниль», 400 мл', 'Мыло туалетное твердое детское : "Красавчик" (3 шт.)', 'Жидкое мыло с миндалем, 500 мл', 'Жидкое мыло с алоэ вера, 500 мл', 'Жидкое мыло на каждый день, Siberica Бибеrika, "Ладушки-ладошки", 500 мл', 'Жидкое мыло антибактериальное, для мытья детских принадлежностей, 500 мл', 'Мыло для лица KLAVA COCA Magic Rock, для глубокого очищения проблемной кожи, 50 г', 'Жидкое мыло для тела и рук Exfoliant/Exfoliating Liquid Marseille Soap, 30 мл', 'Жидкое мыло с экстрактами ромашки и алоэ вера, 500 мл', 'Средство для интимной гигиены INTIMPFLEGE-SCHAUM, для девочек, в виде Пенки, 0% мыла, 250 мл', 'Жидкое мыло 250 мл', 'Жидкое мыло 250 мл', 'Жидкое мыло 250 мл', 'Масло для лица и тела, Cleaner, твердое, Solid/NEW ZEALAND, 60 г', 'Жидкое мыло для волос и тела, СТЕКЛО/Льняное, 250 мл', 'Мыло Чёрное для тела и волос с антибактериальным эффектом, 500 мл', 'Мыло ', 'Мыло Mediterranean touch/Прикосновение средиземноморья 250 г', 'Мыло Tuscan lavender/Лаванда 250 г', 'Мыло Fig and almond milk/Инжир и миндальное молоко 250 г', 'Мыло Tuscan wisteria  and lilac/Глициния и сирень 250 г', 'Мыло Pomegranate and blackcurrant/Гранат и черная смородина 250 г', 'Мыло Garden in bloom/Цветущий сад 250 г', 'Мыло Монастыри и предместья, 250г', 'Мыло Cypress tree/Кипарис 250 г', 'Мыло Broom/Дрок 250 г', 'Мыло Black cherry and red berries/Черешня и красные ягоды 250 г', 'Мыло Prickly pear from Taormina/Опунция из Таормины 250 г', 'Мыло Capri/Капри 250 г', 'Мыло Portofino/Портофино 250 г', 'Набор для ухода за руками Мыло-пенка, Розовый персик 250 мл + запасной блок 200 мл', 'Мыло пенка для рук парфюмированное косметическое увлажняющее с витамином Е, 300 мл', 'Мыло White/Белое 250 г', 'Мыло 60th Anniversary luxury gold soap/Юбилейное золотое 250 г', 'Мыло Aqua dea marine/Морская богиня 250 г', 'Мыло ROYAL SPA «Антиоксидантное» густое медовое, 300 мл', 'Мыло 100 г', 'Мыло Мыло-пенка для младенцев с рождения, сменный блок, 400мл', 'Мыло CITRUS SPECTRE, 120 г', 'Мыло VETYVER SPLASH, 120 г', 'Мыло Sauna & Sport for Men / Густое северное мыло-детокс для волос, лица и тела, 250 мл', 'Мыло Атодерм, 150 г', 'Мыло Mystic Sardaana Парфюмированное для рук, 300 мл', 'Мыло оливковое с вулканическим песком Санторини и экстрактом виноградной лозы, 85 г', 'Мыло Graysalt Soap, 80g', 'Мыло SAKURA TOKYO, 150 г', 'Мыло Mandarin & Green Tea, 150 г', 'Мыло "Белый Мускус" 150 г', 'Мыло "Зеленый Мандарин" 150 гр', 'Мыло Себиум, 100 г', 'Жидкое мыло Press Gurwitz Perfumerie, 300 мл', 'Мыло пенка для младенцев с рождения, флакон, 500 мл', 'Жидкое мыло №5, имбирь, ваниль, вербена, натуральное, парфюмированное, 300 мл', 'Жидкое мыло для рук "№3 Табак, Ваниль, Корица", 300 мл', 'Мыло Мыло-пенка для младенцев с рождения, сменный блок, 800мл', 'Жидкое мыло для рук с пребиотиками и Алоэ Вера "Крепкая маргарита" /HAND SOAP MARGARITA SPIRIT, в мягкой упаковке, 350 мл', 'Жидкое мыло для рук с пребиотиками и Алоэ Вера "Таинственный закат" /HAND SOAP SUNSET FLEUR, в мягкой упаковке, 350 мл', 'Жидкое мыло для рук с пребиотиками и Алоэ Вера "Душистая вербена" /HAND SOAP PURIFYING VERBENA, в мягкой упаковке, 350 мл', 'Жидкое мыло для рук с пребиотиками и Алоэ Вера "Утренняя свежесть" /HAND SOAP MORNING GLORY, в мягкой упаковке, 350 мл', 'Жидкое мыло Grapefruit & Santal, 250мл', 'Жидкое мыло AMBRE-DREAM, 250 мл', 'Жидкое мыло очищающее, масляное для сухой, чувствительной и атопичной кожи (без воды) с Омега 3,6 и 9, 500 мл', 'Жидкое мыло Герань Мандарин 300 мл', 'Жидкое мыло для тела и рук, Fresh Verbena, 300 мл', 'Жидкое мыло для тела и рук, Средиземное море, 300 мл', 'Жидкое мыло для тела и рук, Ароматная Лаванда/Aromatic Lavender, 300 мл', 'Жидкое мыло для тела и рук, Дикая роза/Wild Rose жидкое мыло для тела и рук, 300 мл', 'Жидкое мыло  для тела и рук, Цветы Хлопка/Cotton Flower, 300 мл', 'Жидкое мыло Olive Wood, 300 мл', 'Жидкое мыло Figue De Provence/Fig Of Provence Liquid Marseille Soap, 300 мл', 'Жидкое мыло Pamplemousse Rose/Pink Grapefruit Liquid Marseille Soap 300 мл', 'Жидкое мыло Romarin Vitamine/Revitalizing Rosemary Liquid Marseille Soap, 300 мл', 'Жидкое мыло Марсельское, для тела и рук Белый чай/White Tea 300 ml', 'Жидкое мыло расслабляющее для тела и рук Anis Lavande/Anise Lavender Liquid Marseille Soap, 300 мл', 'Жидкое мыло для тела и рук "Черный чай", 300 мл.', 'Жидкое мыло для тела и рук, Karite/Shea, 300 мл', 'Жидкое мыло энергизирующее для тела и рук Menthe Basilic/Mint Basil Liquid Marseille Soap 300 мл', 'Мыло традиционное марсельское гипоаллергенное, 750 г', 'Жидкое мыло 500 мл', 'Жидкое мыло 250 мл', 'Набор для ухода за телом парфюмированный, Cedre de Siberie, Set of the interior collection, Мыло для рук и тела 300мл + Крем для рук и тела 300мл + Косметичка на молнии', 'Мыло Жидкое Muschio Bianco, 300 мл', 'Жидкое мыло 500 мл', 'Жидкое мыло ', 'Жидкое мыло Nyeok Hand Wash, 300g', 'Жидкое мыло Geuneul Hand Wash, 300g', 'Жидкое мыло "Апельсин, кедр и шалфей", 300 мл', 'Жидкое мыло для лица и рук Face And Hand Soap 500 мл', 'Мыло SPACE, 386 мл', 'Мыло Набор мыло волнующая Тоскана, 6*150г', 'Жидкое мыло Aromatic Hand Wash, 350 мл', 'Жидкое мыло "Тасманский перец, мандарин и ромашка", 500 мл', 'Набор для ухода за телом шампунь 3в1 100 мл + мыло 80 г', 'Жидкое мыло KIYOMI, 350 мл', 'Жидкое мыло YUZU, 350 мл', 'Жидкое мыло питательное NOURISHING HAND WASH, 200 мл', 'Жидкое мыло 500 мл', 'Жидкое мыло 500 мл', 'Набор для ухода за телом "Алоэ Вера", "Карите-Гранат", "Молоко Ослицы", "Масло Арганы", 4х100 г', 'Набор для ухода за телом мыло 4 шт. ', 'Жидкое мыло Face and Hand Mineral Soap, скраб для лица и рук, 500 мл', 'Набор для ухода за руками Набор-дуэт для глубокого увлажнения кожи рук "Сладкий апельсин"', 'Мыло для лица и тела c эвкалиптом, 300 мл', 'Мыло для лица и тела c арганом и эвкалиптом, 300 мл']

data = { "Название": all_names, "Артикул": all_articuls, "Цена": all_prices,
        "Скидка": all_discounts, "Бренд": all_brands, "Страна": all_countries}

df = pd.DataFrame(data)

with open('output.txt', 'w', encoding='utf8') as f_out:
    print(df, file=f_out)
