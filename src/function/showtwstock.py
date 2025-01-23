import requests
import pandas as pd
from io import StringIO
import twstock
from datetime import datetime

def fetch_tw_stock_data():
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
    response = requests.get(url)
    response.encoding = 'utf-8'
    data = response.text
    df = pd.read_csv(StringIO(data))
    return df

def fetch_tpex_stock_data():
    # 取得所有上櫃股票代碼
    tpex_stocks = twstock.twse.tpex_stocks()
    
    # 建立空的 DataFrame
    columns = ['證券代號', '證券名稱', '成交股數', '成交筆數', '成交金額', 
              '開盤價', '最高價', '最低價', '收盤價', '漲跌']
    df = pd.DataFrame(columns=columns)
    
    # 取得每支股票的即時資料
    for stock in tpex_stocks:
        try:
            s = twstock.Stock(stock['code'])
            data = {
                '證券代號': stock['code'],
                '證券名稱': stock['name'],
                '成交股數': s.capacity[-1] if s.capacity else 0,
                '成交筆數': s.transaction[-1] if s.transaction else 0,
                '成交金額': s.turnover[-1] if s.turnover else 0,
                '開盤價': s.open[-1] if s.open else 0,
                '最高價': s.high[-1] if s.high else 0,
                '最低價': s.low[-1] if s.low else 0,
                '收盤價': s.price[-1] if s.price else 0,
                '漲跌': s.change[-1] if s.change else 0
            }
            df = df.append(data, ignore_index=True)
        except Exception as e:
            print(f"取得 {stock['code']} {stock['name']} 資料失敗: {str(e)}")
            continue
            
    return df

def show_tw_stock_data():
    print("=== 上市股票 ===")
    df_tw = fetch_tw_stock_data()
    for index, row in df_tw.iterrows():
        print(f"名稱: {row['證券名稱']}, 股號: {row['證券代號']}")
    
    print("\n=== 上櫃股票 ===")
    df_tpex = fetch_tpex_stock_data()
    for index, row in df_tpex.iterrows():
        print(f"名稱: {row['證券名稱']}, 股號: {row['證券代號']}")

if __name__ == "__main__":
    show_tw_stock_data()
    def show_tw_stock_realtime_data():
        df_tw = fetch_tw_stock_data()
        df_tpex = fetch_tpex_stock_data()
        
        print("=== 上市股票即時價格 ===")
        for index, row in df_tw.iterrows():
            stock = twstock.Stock(row['證券代號'])
            print(f"名稱: {row['證券名稱']}, 股號: {row['證券代號']}, 即時價格: {stock.price[-1]}")
        
        print("\n=== 上櫃股票即時價格 ===")
        for index, row in df_tpex.iterrows():
            stock = twstock.Stock(row['證券代號'])
            print(f"名稱: {row['證券名稱']}, 股號: {row['證券代號']}, 即時價格: {stock.price[-1]}")

    if __name__ == "__main__":
        show_tw_stock_data()
        #show_tw_stock_realtime_data()
