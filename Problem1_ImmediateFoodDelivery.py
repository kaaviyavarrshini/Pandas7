import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate=(delivery['order_date']==delivery['customer_pref_delivery_date']).sum()
    total=len(delivery)
    percentage=round((100*immediate/total),2)
    return pd.DataFrame({'immediate_percentage':[percentage]})