# Time-series
import statsmodels.api as sm

# Ingest data
df = pd.read_csv('data/birth.txt')
dates = pd.date_range(start='01/1980', end='01/2011', freq='M')
idx = dates.to_period(freq='M')
df = df.set_index(idx)

# sanity checking
df.describe()
pd.Series(dates.month).value_counts()
pd.crosstab(dates.year, dates.month)

# check time series
df.plot()
plt.show()

# Calculate birthrate
df['year'] = dates.year
df['month'] = dates.month
df.head()

df['rate']= df.groupby('year')['num_births'].apply(lambda x: x / x.sum())
np.allclose( df.groupby('year')['rate'].sum(), 1)   # check our work

# find months with high birth rates
df.groupby('month').rate.mean().order(ascending=False)

dfmonth = df.pivot(index='year', columns='month', values='rate')
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
dfmonth.columns = months

df.num_births.plot()
df.resample('Q-NOV').num_births.plot(color='red')
df.resample('A').num_births.plot(color='green')
plt.show()

# Add time features
time = np.arange(len(df))
time = pd.Series(map(lambda x: float(x) / np.max(time), time), index=idx)
time2 = time * time
time3 = time2 * time

dftime = pd.DataFrame( {'time': time, 'time2': time2, 'time3': time3, 'num_births': df.num_births}, index=idx)

ols = sm.OLS(dftime.num_births, dftime[['time', 'time2', 'time3']])
result = ols.fit()
result.summary()
result.resid.plot()
plt.show()      # this model is crap

# Try with monthly dummies
dummies = pd.get_dummies(idx.month)
dummies = dummies.set_index(idx)
dftime_dum = pd.concat( [dftime, dummies], axis=1)

ols_dum = sm.OLS(dftime_dum.num_births, dftime_dum.icol(range(1,16)))

#=========================================================================================
