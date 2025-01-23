import requests
import pandas as pd
from io import StringIO  # 從標準庫匯入 StringIO
import twstock

def fetch_tw_stock_data():
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
    response = requests.get(url)
    response.encoding = 'utf-8'
    data = response.text

    df = pd.read_csv(StringIO(data))
    return df

def show_tw_stock_data():
    df = fetch_tw_stock_data()
    for index, row in df.iterrows():
        print(f"名稱: {row['證券名稱']}, 股號: {row['證券代號']}")

if __name__ == "__main__":
    show_tw_stock_data()
    def show_tw_stock_realtime_data():
        df = fetch_tw_stock_data()
        for index, row in df.iterrows():
            stock = twstock.Stock(row['證券代號'])
            print(f"名稱: {row['證券名稱']}, 股號: {row['證券代號']}, 即時價格: {stock.price[-1]}")

    if __name__ == "__main__":
        show_tw_stock_data()
        show_tw_stock_realtime_data()

