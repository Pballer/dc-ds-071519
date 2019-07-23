import pandas as pd
seattleZipCodes = [98101, 98102, 98103, 98104, 98105, 98106, 98107, 98108, 98109, 98112, 98115, 98116, 98117, 98118, 98119, 98121, 98122, 98125, 98126, 98133, 98134, 98136, 98144, 98146, 98154, 98164, 98174, 98177, 98178, 98195, 98199]

sales_df = pd.read_csv('data/EXTR_RPSale.csv')
sales_df = sales_df[['Major', 'Minor', 'DocumentDate', 'SalePrice']]

bldg_df = pd.read_csv('data/EXTR_ResBldg.csv')
bldg_df = bldg_df[['Major', 'Minor', 'SqFtTotLiving', 'ZipCode']]

sales_data = pd.merge(sales_df, bldg_df, on=['Major', 'Minor'])

sales_df['Major'] = pd.to_numeric(sales_df['Major'], errors='coerce')
sales_df['Minor'] = pd.to_numeric(sales_df['Minor'], errors='coerce')

sales_data = pd.merge(sales_df, bldg_df, on=['Major', 'Minor'])

sales_data.dropna(subset=['ZipCode'], inplace=True)

sales_data = sales_data.loc[sales_data.SalePrice > 0]
sales_data = sales_data.loc[sales_data.SqFtTotLiving > 0]

sales_data['ZipCode'] = sales_data.ZipCode.map(lambda z: str(z)[:5])

sales_data['PricePerSqFt'] = sales_data.SalePrice / sales_data.SqFtTotLiving

sales_data['date'] = pd.to_datetime(sales_data.DocumentDate)
sales_data2019 = sales_data[sales_data.date.dt.year == 2019].copy()

sales_data2019['ZipCode'] = pd.to_numeric(sales_data2019['ZipCode'])
seattleZipCodeDf = pd.DataFrame(seattleZipCodes, columns=['ZipCode'])
seattle = pd.merge(sales_data2019, seattleZipCodeDf, on='ZipCode', how='inner')
seattle.to_csv('seattle.csv')

seattle2019Mean = seattle.PricePerSqFt.mean()

print('Seattle 2019 mean price per square foot: ', seattle2019Mean)