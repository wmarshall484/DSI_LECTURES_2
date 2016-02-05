

```python
import pandas as pd
```


```python
## HOW TO SET INDEX
dfone = pd.read_csv('../data/one.csv')
dfone = dfone.set_index('name')
dfone
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>number</th>
      <th>sex</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>zack</th>
      <td> 1</td>
      <td> m</td>
    </tr>
    <tr>
      <th>drake</th>
      <td> 2</td>
      <td> m</td>
    </tr>
    <tr>
      <th>dan</th>
      <td> 3</td>
      <td> m</td>
    </tr>
    <tr>
      <th>wini</th>
      <td> 9</td>
      <td> f</td>
    </tr>
    <tr>
      <th>jon</th>
      <td> 9</td>
      <td> m</td>
    </tr>
    <tr>
      <th>ryan</th>
      <td> 9</td>
      <td> m</td>
    </tr>
    <tr>
      <th>gio</th>
      <td> 4</td>
      <td> f</td>
    </tr>
  </tbody>
</table>
</div>




```python
dftwo = pd.read_csv('../data/two.csv')
dftwo = dftwo.set_index('name')
dftwo
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th> Home</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>gio</th>
      <td>   Maine</td>
    </tr>
    <tr>
      <th>zack</th>
      <td>      NY</td>
    </tr>
    <tr>
      <th>wini</th>
      <td>  Hawaii</td>
    </tr>
    <tr>
      <th>eric</th>
      <td>      CA</td>
    </tr>
    <tr>
      <th>sri</th>
      <td>      CA</td>
    </tr>
    <tr>
      <th>tripti</th>
      <td>      CA</td>
    </tr>
    <tr>
      <th>ethan</th>
      <td>      CA</td>
    </tr>
    <tr>
      <th>dr.stylez</th>
      <td>      CA</td>
    </tr>
    <tr>
      <th>jon</th>
      <td>      NY</td>
    </tr>
  </tbody>
</table>
</div>




```python
### TO USE DF.JOIN()
### THE DF AND DF2 MUST SHARE INDEX
### IE; KEYS ARE IN THE INDEX


dfone = pd.read_csv('../data/one.csv')
dfone = dfone.set_index('name')

dftwo = pd.read_csv('../data/two.csv')
dftwo = dftwo.set_index('name')

# DOCS: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.join.html
joined = dfone.join(dftwo)
joined
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>number</th>
      <th>sex</th>
      <th> Home</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>zack</th>
      <td> 1</td>
      <td> m</td>
      <td>      NY</td>
    </tr>
    <tr>
      <th>drake</th>
      <td> 2</td>
      <td> m</td>
      <td>     NaN</td>
    </tr>
    <tr>
      <th>dan</th>
      <td> 3</td>
      <td> m</td>
      <td>     NaN</td>
    </tr>
    <tr>
      <th>wini</th>
      <td> 9</td>
      <td> f</td>
      <td>  Hawaii</td>
    </tr>
    <tr>
      <th>jon</th>
      <td> 9</td>
      <td> m</td>
      <td>      NY</td>
    </tr>
    <tr>
      <th>ryan</th>
      <td> 9</td>
      <td> m</td>
      <td>     NaN</td>
    </tr>
    <tr>
      <th>gio</th>
      <td> 4</td>
      <td> f</td>
      <td>   Maine</td>
    </tr>
  </tbody>
</table>
</div>




```python
# HOW TO MERGE TWO DATAFRAMES
# PD.MERGE DF.MERGE
# EXAMPLE BETWEEN SWITCHING UP LEFT ON AND RIGHT ONW

# EXAMPLE 1 OF 3

dfone = pd.read_csv('../data/one.csv')
dftwo = pd.read_csv('../data/two.csv')

# OPTIONS: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html
merged = pd.merge(left= dfone, \
                  right= dftwo,\
                  on= 'name')
merged
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>number</th>
      <th>sex</th>
      <th> Home</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> zack</td>
      <td> 1</td>
      <td> m</td>
      <td>      NY</td>
    </tr>
    <tr>
      <th>1</th>
      <td> wini</td>
      <td> 9</td>
      <td> f</td>
      <td>  Hawaii</td>
    </tr>
    <tr>
      <th>2</th>
      <td>  jon</td>
      <td> 9</td>
      <td> m</td>
      <td>      NY</td>
    </tr>
    <tr>
      <th>3</th>
      <td>  gio</td>
      <td> 4</td>
      <td> f</td>
      <td>   Maine</td>
    </tr>
  </tbody>
</table>
</div>




```python
# HOW TO MERGE TWO DATAFRAMES
# PD.MERGE DF.MERGE
# EXAMPLE BETWEEN SWITCHING UP LEFT ON AND RIGHT ONW

# EXAMPLE 2 OF 3

dfone = pd.read_csv('../data/one.csv')
dftwo = pd.read_csv('../data/two.csv')

# OPTIONS: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html
merged = pd.merge(left= dftwo,\
                  right= dfone,\
                  on='name')
merged
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th> Home</th>
      <th>number</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>  gio</td>
      <td>   Maine</td>
      <td> 4</td>
      <td> f</td>
    </tr>
    <tr>
      <th>1</th>
      <td> zack</td>
      <td>      NY</td>
      <td> 1</td>
      <td> m</td>
    </tr>
    <tr>
      <th>2</th>
      <td> wini</td>
      <td>  Hawaii</td>
      <td> 9</td>
      <td> f</td>
    </tr>
    <tr>
      <th>3</th>
      <td>  jon</td>
      <td>      NY</td>
      <td> 9</td>
      <td> m</td>
    </tr>
  </tbody>
</table>
</div>




```python
# HOW TO MERGE TWO DATAFRAMES
# PD.MERGE DF.MERGE using how=
# EXAMPLE BETWEEN SWITCHING UP LEFT ON AND RIGHT ONW

# EXAMPLE 3 OF 3

# OPTIONS: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html

dfone = pd.read_csv('../data/one.csv')
dftwo = pd.read_csv('../data/two.csv')
merged = pd.merge(dfone, \
                  dftwo, \
                  on='name', \
                  how='left')
merged
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>number</th>
      <th>sex</th>
      <th> Home</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>  zack</td>
      <td> 1</td>
      <td> m</td>
      <td>      NY</td>
    </tr>
    <tr>
      <th>1</th>
      <td> drake</td>
      <td> 2</td>
      <td> m</td>
      <td>     NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>   dan</td>
      <td> 3</td>
      <td> m</td>
      <td>     NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>  wini</td>
      <td> 9</td>
      <td> f</td>
      <td>  Hawaii</td>
    </tr>
    <tr>
      <th>4</th>
      <td>   jon</td>
      <td> 9</td>
      <td> m</td>
      <td>      NY</td>
    </tr>
    <tr>
      <th>5</th>
      <td>  ryan</td>
      <td> 9</td>
      <td> m</td>
      <td>     NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>   gio</td>
      <td> 4</td>
      <td> f</td>
      <td>   Maine</td>
    </tr>
  </tbody>
</table>
</div>




```python
### ADD MORE ROWS TO YOUR DATA, ADD DATA BELOW YOUR DATA,
### PD.CONCAT(AXIS=1) MAKES YOUR DF LONGER...
### PD.CONCAT(AXIS=0) MAKES YOUR DF WIDER...

### EXAMPLE 1 OF 2

dfone = pd.read_csv('../data/one.csv')
dftwo = pd.read_csv('../data/two.csv')

s1 = pd.Series( [0,1,2,3], index=['a', 'b', 'c', 'd' ] )
s2 = pd.Series( [4,5], index=['e', 'f'])
s3 = pd.Series( [5], index=['g'])

scc = pd.concat( [s1,s2,s3] )
scc
```




    a    0
    b    1
    c    2
    d    3
    e    4
    f    5
    g    5
    dtype: int64




```python
### ADD MORE ROWS TO YOUR DATA, ADD DATA BELOW YOUR DATA,
### PD.CONCAT(AXIS=1) MAKES YOUR DF LONGER...
### PD.CONCAT(AXIS=0) MAKES YOUR DF WIDER...

### EXAMPLE 2 OF 2

dfone = pd.read_csv('../data/one.csv')
dftwo = pd.read_csv('../data/two.csv')

dfcc = pd.concat(objs=[dfone, dftwo],\
                 axis=1, \
                 keys= ['DF1 useful label', 'dftwo label']\
                 )
dfcc
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">DF1 useful label</th>
      <th colspan="2" halign="left">dftwo label</th>
    </tr>
    <tr>
      <th></th>
      <th>name</th>
      <th>number</th>
      <th>sex</th>
      <th>name</th>
      <th> Home</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>  zack</td>
      <td>  1</td>
      <td>   m</td>
      <td>       gio</td>
      <td>   Maine</td>
    </tr>
    <tr>
      <th>1</th>
      <td> drake</td>
      <td>  2</td>
      <td>   m</td>
      <td>      zack</td>
      <td>      NY</td>
    </tr>
    <tr>
      <th>2</th>
      <td>   dan</td>
      <td>  3</td>
      <td>   m</td>
      <td>      wini</td>
      <td>  Hawaii</td>
    </tr>
    <tr>
      <th>3</th>
      <td>  wini</td>
      <td>  9</td>
      <td>   f</td>
      <td>      eric</td>
      <td>      CA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>   jon</td>
      <td>  9</td>
      <td>   m</td>
      <td>       sri</td>
      <td>      CA</td>
    </tr>
    <tr>
      <th>5</th>
      <td>  ryan</td>
      <td>  9</td>
      <td>   m</td>
      <td>    tripti</td>
      <td>      CA</td>
    </tr>
    <tr>
      <th>6</th>
      <td>   gio</td>
      <td>  4</td>
      <td>   f</td>
      <td>     ethan</td>
      <td>      CA</td>
    </tr>
    <tr>
      <th>7</th>
      <td>   NaN</td>
      <td>NaN</td>
      <td> NaN</td>
      <td> dr.stylez</td>
      <td>      CA</td>
    </tr>
    <tr>
      <th>8</th>
      <td>   NaN</td>
      <td>NaN</td>
      <td> NaN</td>
      <td>       jon</td>
      <td>      NY</td>
    </tr>
  </tbody>
</table>
</div>




```python
### WE HAVE SOME DF, AND WE WANT TO ADD ANOTHER COLUMN TO IT, BUT, THERE ARE NOT THE SAME EXACT LENGHT
### HOW TO MAKE A DATA FRAME FROM TWO LISTS
### HOW TO BUILD A DATAFRAME
### list of verything dataframes can do: http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html

# EXAMPLE 1 OF 2

my_vals = [0,1,2,3,4,5]
my_index = ['a', 'b', 'c', 'd', 'e', 'f']
df = pd.DataFrame(data= my_vals, \
                  index=my_index, \
                  columns= ['col one'] )
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td> 0</td>
    </tr>
    <tr>
      <th>b</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>c</th>
      <td> 2</td>
    </tr>
    <tr>
      <th>d</th>
      <td> 3</td>
    </tr>
    <tr>
      <th>e</th>
      <td> 4</td>
    </tr>
    <tr>
      <th>f</th>
      <td> 5</td>
    </tr>
  </tbody>
</table>
</div>




```python
### WE HAVE SOME DF, AND WE WANT TO ADD ANOTHER COLUMN TO IT, BUT, THERE ARE NOT THE SAME EXACT LENGHT
### HOW TO MAKE A DATA FRAME FROM TWO LISTS
### HOW TO BUILD A DATAFRAME
### list of verything dataframes can do: http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html

# EXAMPLE 2 OF 2

ratings = [90, 100, 98, 42]
coolness = ['cool', 'cool', 'cool', 'not keww']
my_index = ['Drake', 'Weezy', 'Kanye', 'Papoose']

df = pd.DataFrame(data=ratings, \
                  index=my_index , \
                  columns=['ratings'])

df['coolness'] = coolness
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ratings</th>
      <th>coolness</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Drake</th>
      <td>  90</td>
      <td>     cool</td>
    </tr>
    <tr>
      <th>Weezy</th>
      <td> 100</td>
      <td>     cool</td>
    </tr>
    <tr>
      <th>Kanye</th>
      <td>  98</td>
      <td>     cool</td>
    </tr>
    <tr>
      <th>Papoose</th>
      <td>  42</td>
      <td> not keww</td>
    </tr>
  </tbody>
</table>
</div>




```python
### df.APPEND() IS PRETTY USELESS
### UNLESS... SEE CELL BELOW
# DOCS ->  http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.append.html

dfone = pd.read_csv('../data/one.csv')
dftwo = pd.read_csv('../data/two.csv')
print 'dfone.append(dftwo)'
dfone.append(dftwo)
```

    dfone.append(dftwo)





<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th> Home</th>
      <th>name</th>
      <th>number</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>     NaN</td>
      <td>      zack</td>
      <td>  1</td>
      <td>   m</td>
    </tr>
    <tr>
      <th>1</th>
      <td>     NaN</td>
      <td>     drake</td>
      <td>  2</td>
      <td>   m</td>
    </tr>
    <tr>
      <th>2</th>
      <td>     NaN</td>
      <td>       dan</td>
      <td>  3</td>
      <td>   m</td>
    </tr>
    <tr>
      <th>3</th>
      <td>     NaN</td>
      <td>      wini</td>
      <td>  9</td>
      <td>   f</td>
    </tr>
    <tr>
      <th>4</th>
      <td>     NaN</td>
      <td>       jon</td>
      <td>  9</td>
      <td>   m</td>
    </tr>
    <tr>
      <th>5</th>
      <td>     NaN</td>
      <td>      ryan</td>
      <td>  9</td>
      <td>   m</td>
    </tr>
    <tr>
      <th>6</th>
      <td>     NaN</td>
      <td>       gio</td>
      <td>  4</td>
      <td>   f</td>
    </tr>
    <tr>
      <th>0</th>
      <td>   Maine</td>
      <td>       gio</td>
      <td>NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>      NY</td>
      <td>      zack</td>
      <td>NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>  Hawaii</td>
      <td>      wini</td>
      <td>NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>      CA</td>
      <td>      eric</td>
      <td>NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>      CA</td>
      <td>       sri</td>
      <td>NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>      CA</td>
      <td>    tripti</td>
      <td>NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>      CA</td>
      <td>     ethan</td>
      <td>NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>      CA</td>
      <td> dr.stylez</td>
      <td>NaN</td>
      <td> NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>      NY</td>
      <td>       jon</td>
      <td>NaN</td>
      <td> NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
### APPEND IS PRETTY USELESS
### UNLESS...
### YOU WANT TO JUST ADD ANOTHER ROW INTO YOUR DATASET
### APPEND DOESN'T HAVE MUCH IF ANY CONDITIONAL LOGIC
# LEARN MORE AT:  http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.append.html


dfone = pd.read_csv('../data/one.csv')

just_a_list =['Fat Joe', 88, 'm']
just_a_dict = {'name': 'Ja Rule', 'number': 55, 'sex': 'm'}
list_of_dicts = [{'name': 'Big Sean', 'number': 2, 'sex': 'm' }]

print 'APPENDING A LIST'
print dfone.append(just_a_list)
print "----------------------"
print ''
print 'APPENDING A DICT, NEED TO USE ignore_index=True'
print dfone.append(just_a_dict, ignore_index=True)
print "----------------------"
print ''
print 'LIST OF A DICT WORKS LIKE A CHARM'
print dfone.append(list_of_dicts)


```

    APPENDING A LIST
             0   name  number  sex
    0      NaN   zack       1    m
    1      NaN  drake       2    m
    2      NaN    dan       3    m
    3      NaN   wini       9    f
    4      NaN    jon       9    m
    5      NaN   ryan       9    m
    6      NaN    gio       4    f
    0  Fat Joe    NaN     NaN  NaN
    1       88    NaN     NaN  NaN
    2        m    NaN     NaN  NaN
    ----------------------

    APPENDING A DICT, NEED TO USE ignore_index=True
          name  number sex
    0     zack       1   m
    1    drake       2   m
    2      dan       3   m
    3     wini       9   f
    4      jon       9   m
    5     ryan       9   m
    6      gio       4   f
    7  Ja Rule      55   m
    ----------------------

    LIST OF A DICT WORKS LIKE A CHARM
           name  number sex
    0      zack       1   m
    1     drake       2   m
    2       dan       3   m
    3      wini       9   f
    4       jon       9   m
    5      ryan       9   m
    6       gio       4   f
    0  Big Sean       2   m



```python
# HOW TO CONSTRUCT A DATAFRAME FROM A DICTIONARY
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], \
        'year': [2000, 2001, 2002, 2001, 2002], \
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

df = pd.DataFrame(data = data, \
                  columns=['pop', 'state', 'year']\
                  )
```
