import pandas as pd
import time
from raw_sql import get_rows, insert_rows
from message import send_message

def check_forms():
    sheet_id = ""
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    print("#"*20)
    print('dataframe', df)
    print("lenght of dataframe ", len(df))
    print('lenght of rows ', get_rows())
    if get_rows() < len(df):
        last_row = df.iloc[-1]
        data_row = dict(last_row)
        send_message(data_row.get('Mobile Number'))
        insert_rows(data_row)
    print("#"*20)
    time.sleep(2)

    check_forms()


if __name__ == "__main__":
    check_forms()
