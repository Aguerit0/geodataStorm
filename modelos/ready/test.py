from Data import GetData

YEAR = 2000
MONTH = 1
DAY = 20

data = GetData()
url_by_month = data.get_data_by_month(YEAR, MONTH)
url_by_year = data.get_data_by_year(YEAR)
df1 = data.scrapping_data(url_by_month)
df2 = data.scrapping_data(url_by_year)


print(df1.head(), df2.head())

