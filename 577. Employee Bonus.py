import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # 使用 merge 合并两个 DataFrame，根据 'empId' 列进行合并
    emp = employee.merge(bonus, on='empId', how='left')
    emp = emp[['name','bonus']]#只要這兩行
    # 使用 drop 方法删除 bonus 大于等于 1000 的行
    emp = emp.drop(emp[emp['bonus'] >= 1000].index)

    return emp
