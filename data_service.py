import pandas as pd
def count_price_change(now, year, df):
    x = df.Price[now] - df.Price[year]
    return x
def count_price_change_percent(now, year, df):
    x = df.Price[now]/df.Price[year]*100
    return x
cols = pd.MultiIndex.from_tuples([('Product code', ''),
                                 ('Price', 2007), ('Price', 2008), ('Price', 2011), ('Price', 2017),
                                 ('Markets', '')])
avarage_prices = pd.DataFrame([[101, 101, 101, 101, 102, 102, 102, 103, 103, 103, 201, 201, 201, 202, 202, 202, 203, 203, 203],
                               [0.59, 0.74, 0.7, 0.66, 0.38, 0.36, 0.59, 0.63, 0.63, 0.36, 0.69, 0.68, 0.69, 0.88, 0.87, 0.85, 1, 0.99, 0.99],
                               [0.75, 0.83, 0.82, 0.75, 0.65, 0.6, 0.75, 0.79, 0.75, 0.6, 0.99, 0.98, 0.95, 1.24, 1.22, 1.24, 1.33, 1.31, 1.33],
                               [2.03, 2.08, 2.04, 2.03, 2.4, 2.3, 2.03, 2.04, 2, 2.35, 4.52, 4.5, 4.45, 4.56, 4.53, 4.55, 5.77, 5.75, 5.75],
                               [69.5, 70, 40, 39.8, 45, 44.6, 69.5, 40, 68, 44.8, 30, 29.6, 29.6, 25, 25, 25, 70, 68.9, 69],
                               ['Сінний', 'Бесарабський', "Лук'янівський", 'Сінний', 'Бесарабський', "Лук'янівський", 'Сінний', 'Бесарабський', "Лук'янівський",
                                'Сінний', 'Бесарабський', "Лук'янівський", 'Сінний', 'Бесарабський', "Лук'янівський", 'Сінний', 'Бесарабський', "Лук'янівський", 'Сінний']], cols).T
product_directory = pd.DataFrame([[101, 102, 103, 201, 202, 203],
                                  ['Картопля', 'Капуста', 'Цибуля', 'Помідори', 'Огірки', 'Яблука'],
                                  ['кг.', 'кг.', 'кг.', 'кг.', 'кг.', 'кг.']], ['Product code', 'Product name', 'Unit']).T

res_cols = pd.MultiIndex.from_tuples([('Markets', '', ''),
                                      ('Product name', '', ''),
                                      ('Unit', '', ''),
                                      ('Price change', 2007, ''),
                                      ('Price change', 2008, 'uah'), ('Price change', 2008, '% by 2007'),
                                      ('Price change', 2011, 'uah'), ('Price change', 2011, '% by 2008'),
                                      ('Price change', 2017, 'uah'), ('Price change', 2017, '% by 2011')])
prod_name = pd.Series(avarage_prices.replace(product_directory['Product code'].to_list(), product_directory['Product name'].to_list())['Product code'])
prod_name.name = 'Product name'
result = pd.DataFrame([avarage_prices['Markets'],
                       prod_name,
                       pd.Series(['кг.']*len(avarage_prices)),
                       avarage_prices.Price[2007],
                       count_price_change(2008, 2007, avarage_prices),
                       count_price_change_percent(2008, 2007, avarage_prices),
                       count_price_change(2011, 2008, avarage_prices),
                       count_price_change_percent(2011, 2008, avarage_prices),
                       count_price_change(2017, 2011, avarage_prices),
                       count_price_change_percent(2017, 2011, avarage_prices)], res_cols).T
print(avarage_prices)
print(product_directory)
print(result)
