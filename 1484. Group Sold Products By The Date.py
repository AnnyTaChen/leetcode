import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    #agg是配合groupby，得到A的mean之類的
    df = activities.sort_values(['product','sell_date'])
    df = df.drop_duplicates()
    df=df.groupby(by='sell_date',as_index=False)['product'].agg({'num_sold':'nunique','products':','.join})
    return df
    #使用 groupby 方法，按照 'sell_date' 列进行分组。对每个分组，使用 agg 方法，计算售出的不同产品数量（'num_sold': 'nunique'）和列举所有售出的产品（'products': ','.join，使用逗号连接）。
