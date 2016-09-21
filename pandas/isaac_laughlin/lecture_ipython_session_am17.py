# coding: utf-8
import pandas as pd
prices = pd.Series([1,1,2,3,5], index=['apple', 'pear', 'banana', 'mango', 'jackfruit'])
prices
prices.index
prices.iloc[1:3]
prices.loc['pear']
prices.loc['pear':]
prices.loc['pear':'mango']
prices.ix['pear':'mango']
prices.ix[1:4]
foo = pd.Series([9,382,493])
foo
foo.sort_values()
foo.sort_values(ascending=False)
foo.ix[0]
prices['banana']
prices[3]
prices
prices.mean()
prices.std()
prices.median()
prices.describe()
for val in prices:
    print val
    
discount_prices = prices.apply(lambda x: .9*x if x>3 else x)
discount_prices
prices.empty
produce = pd.DataFrame({'price':prices,
'discount_price':discount_prices,
'inventory':inventory})
inventory = pd.Series([10,50,41,22])
inventory
inventory = pd.Series([10,50,41,22], index=['pear', 'banana', 'mango', 'apple'])
inventory
prices
inventory*prices
prices, inventory
nonunique_inventory = pd.Series([10,50,41,22,50], index=['pear', 'banana', 'mango', 'apple', 'apple'])
nonunique_inventory
nonunique_inventory*prices
inventory > 20
inventory[inventory>20]
produce = pd.DataFrame({'price':prices,
'discount_price':discount_prices,
'inventory':inventory})
produce
produce.loc['pear']
produce.loc['pear','price']
produce.loc['pear':,'price']
produce.loc['banana':,'price']
produce.loc['banana':'mango','price']
produce.loc['pear']
type(produce.loc['pear'])
produce
pd.concat([produce, nonunique_inventory])
pd.concat([produce, nonunique_inventory], axis=1)
alt_produce = pd.DataFrame({'price':prices,
'discount_price':discount_prices,
'inventory':nonunique_inventory})
alt_produce = pd.DataFrame({'price':prices,
'discount_price':discount_prices,
'inventory':nonunique_inventory}.values())
alt_produce = pd.DataFrame({'price':prices,
'discount_price':discount_prices,
'inventory':inventory}.values())
alt_produce
alt_produce.T
prices
prices.nme
prices.name
prices.name = 'foo'
alt_produce = pd.DataFrame({'price':prices,
'discount_price':discount_prices,
'inventory':inventory}.values())
alt_produce
produce
produce['pear']
produce.loc['pear']
produce
produce.iloc[2:, 1]
produce.ix[[0,2,3], ['discount_price']]
produce.iloc[[0,2,3]].loc[:,'discount_price']
produce.discount_price
produce.mean
produce
produce
produce.loc[produce.discount_price>=3,:]
produce.loc[:, produce.max()>5]
produce.max()
produce['inventory_value'] = produce['inventory']*produce['price']
produce
del produce['inventory_value']
produce
produce['inventory_value'] = produce['inventory']*produce['price']
produce
produce.drop(['inventory_value'])
produce.drop(['inventory_value'], axis=1)
produce
produce.drop(['inventory_value'], axis=1, inplace=True)
produce
get_ipython().magic(u'save lecture_ipython_session.py 1-88')
