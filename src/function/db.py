import psycopg2
from psycopg2 import sql

def get_db_connection():
    return psycopg2.connect(
        host="127.0.0.1",
        user="trade",
        password="trade",
        dbname="twstockdb"
    )

def create_stock_lists_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_lists (
            id SERIAL PRIMARY KEY,
            type VARCHAR(50) NOT NULL,
            code VARCHAR(10) NOT NULL,
            name VARCHAR(255) NOT NULL,
            ISIN VARCHAR(12) NOT NULL,
            start DATE NOT NULL,
            market VARCHAR(50) NOT NULL,
            industry_group VARCHAR(50),
            CFI VARCHAR(10) NOT NULL,
            UNIQUE(code)
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
create_stock_lists_table()
