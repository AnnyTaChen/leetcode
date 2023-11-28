import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    #先用日期排序
    weather.sort_values(by='recordDate',inplace=True)
    #日期差
    diff_date=weather['recordDate'].diff().dt.days#dt是日月年計算的套件單位
    #溫度差
    diff_temp=weather['temperature'].diff()
    return weather[(diff_date ==1)&(diff_temp>0)][['id']]
