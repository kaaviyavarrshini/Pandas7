import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    lowdf=accounts[accounts['income']<20000]
    avgdf=accounts[(accounts['income']>20000) & (accounts['income']<50000)]
    highdf=accounts[accounts['income']>50000]
    return pd.DataFrame([['Low Salary',len(lowdf)],
                         ['Average Salary',len(avgdf)],
                         ['High Salary',len(highdf)]
                         ],columns=['category','accounts_count'])