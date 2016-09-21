# coding: utf-8
get_ipython().magic(u'paste')
pd.merge(left, right, on='key')
get_ipython().magic(u'paste')
result=  pd.merge(left, right, on=['key1', 'key2'])
result
result=  pd.merge(left, right, on=['key1', 'key2'], how='inner')
result=  pd.merge(left, right, on=['key1', 'key2'], how='left')
result=  pd.merge(left, right, on=['key1', 'key2'], how='right')
result
result=  pd.merge(left, right, on=['key1', 'key2'], how='outer')
result
get_ipython().magic(u'pinfo left.join')
get_ipython().magic(u'paste')
grocery
grocery.groupby('category')
g = grocery.groupby('category')
g.aggregate(np.mean)
import numpy as np
g.aggregate(np.mean)
g.mean()
g.transform(lambda x: x - x.mean())
grocery
grocery.price - grocery.price.mean()
grocery
grocery
g.filter(lambda x: len(x)>2)
grocery[grocery.category=='meat']
g.filter(lambda x: x.price > 5)
g.filter(lambda x: (x.price > 5).any())
g.aggregate(np.mean)
g['price'].aggregate(np.mean)
g.filter(lambda x: (x > 5).any())
g['price'].filter(lambda x: (x > 5).any())
for thing in g:
    print thing
    
grocery
_239
g['price'].filter(lambda x: (x > 5).any())
grocery.price > 5
(grocery.price > 5).any()
(grocery.price > 5).all()
#Keep all entries from data whose price is greater than the group average.
grocery
def higher_than_avg(df):
    mean = df.mean()
    above_mean = df.price > mean
    return df[above_mean]
hight_than_avg(grocery)
higher_than_avg(grocery)
def higher_than_avg(df):
    mean = df.mean()
    print  mean
    above_mean = df.price > mean
    return df[above_mean]
higher_than_avg(grocery)
get_ipython().magic(u'debug')
def higher_than_avg(df):
    mean = df.price.mean()
    above_mean = df.price > mean
    return df[above_mean]
    
higher_than_avg(grocery)
g.apply(higher_than_avg)
def higher_than_avg(df):
    mean = df.price.mean()
    above_mean = df.price > mean
    return df[above_mean,:]
    
    
g.apply(higher_than_avg)
def higher_than_avg(df):
    mean = df.price.mean()
    above_mean = df.price > mean
    return df.ix[above_mean,:]
    
    
    
g.apply(higher_than_avg)
