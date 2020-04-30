import pandas as pd

print(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))

fruit_sales = pd.DataFrame({'Apples':[35,41], 'Bananas':[21,34]}, index = ['2017 Sales', '2018 Sales'])

print(fruit_sales)

quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
recipe = pd.Series(quantities, index = items, name = 'Dinner')

print(recipe)


print('\n')
prueba = pd.read_csv('/home/bob/Downloads/_PaP - 2020.csv', index_col=0)
print(prueba)
print(prueba.head())
print('\n')
print(prueba.Marca)
print('\n')
print(prueba['Centro'])
print('\n')
print(prueba['Centro'][5])
print('\n')
print(prueba['Centro']['3/2/2020'])
print('\n')
print(prueba.iloc[0])
print('\n')
print(prueba.iloc[:,0])
print('\n')
print(prueba.iloc[:,3])
print('\n')
print(prueba.loc[prueba.Técnico == '115393'])
print('\n')
print(prueba.Técnico.isin(['115393']))
print('\n')
print(prueba.Técnico.describe())
print('\n')
print(prueba.Técnico.unique())
print('\n')
print(prueba.Marca.value_counts())