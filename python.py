import pandas as pd

df = pd.read_csv('obesity_actual.csv')
df = df.drop(columns=['Sample_Size','ID'])
factors = ['Income','Age','Education']
years = [2012,2013,2014,2015,2016,2017,2018]


for factor in factors:
    result = pd.DataFrame(columns=[factor,'Value','Year'])
    if factor == 'Income':
        factor_df = df[df[factor].notnull()][df.Income != 'Data not reported'].groupby([factor,'Year'], as_index=False).mean()
    else:
        factor_df = df[df[factor].notnull()].groupby([factor,'Year'], as_index=False).mean()
    
    factor_df.to_csv('obesity_{}.csv'.format(factor))