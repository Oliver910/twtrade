import twstock
from db import get_db_connection

def get_stock_lists():
    # 取得所有股票列表
    stock_lists = twstock.codes
    
    # 連線資料庫
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 清空現有資料
    cursor.execute("TRUNCATE TABLE stock_lists")
    
    # 插入新資料
    for code, info in stock_lists.items():
        if info.type == '股票':
            cursor.execute("""
                INSERT INTO stock_lists 
                (type, code, name, ISIN, start, market, industry_group, CFI)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                info.type,
                code,
                info.name,
                getattr(info, 'isin', ''),
                info.start,
                info.market,
                info.group,
                info.CFI
            ))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("股市列表已成功更新至資料庫")

if __name__ == "__main__":
    get_stock_lists()
