import pandas as pd

minder = pd.read_csv('gapminder.csv')
print(minder)
print(minder.index)
print(minder.shape)
print(minder.ndim)
print("----------------------------------------------------------------------")

print(minder.head())
print(minder.tail())
print("----------------------------------------------------------------------")

print(minder.iloc[0:5:4,:])
print(minder.loc[:,('country','year')])
print("----------------------------------------------------------------------")

print(minder.loc[0:30,'lifeExp'])
print("----------------------------------------------------------------------")

print(minder[((minder['year']==1972)|(minder['year']==1957))&(minder['country']=='Benin')&(minder['continent']=='Africa')])
print("----------------------------------------------------------------------")

print(minder.iloc[0:84 ,:])
