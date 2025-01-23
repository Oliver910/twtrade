-- Stock Market Analysis Database Schema

-- Stock Data Table
CREATE TABLE IF NOT EXISTS stock_data (
    id SERIAL PRIMARY KEY,
    stock_code VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    open_price NUMERIC(10, 2),
    high_price NUMERIC(10, 2),
    low_price NUMERIC(10, 2),
    close_price NUMERIC(10, 2),
    volume BIGINT,
    rsi NUMERIC(6, 2),
    macd NUMERIC(6, 2),
    ema NUMERIC(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(stock_code, date) -- 確保每支股票的某一天只有一筆記錄
);

-- AI Predictions Table
CREATE TABLE IF NOT EXISTS ai_predictions (
    id SERIAL PRIMARY KEY,
    stock_code VARCHAR(10) NOT NULL,
    prediction_date DATE NOT NULL,
    predicted_price NUMERIC(10, 2),
    confidence NUMERIC(5, 4),
    model_version VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (stock_code) REFERENCES stock_data(stock_code)
);

-- Telegram Notifications Table
CREATE TABLE IF NOT EXISTS telegram_notifications (
    id SERIAL PRIMARY KEY,
    chat_id BIGINT NOT NULL,
    message TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK(status IN ('pending', 'sent', 'failed'))
);

-- Stock Configuration Table
CREATE TABLE IF NOT EXISTS stock_config (
    stock_code VARCHAR(10) PRIMARY KEY,
    stock_name VARCHAR(100) NOT NULL,
    exchange_market VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for faster queries
CREATE INDEX idx_stock_data_date ON stock_data(date);
CREATE INDEX idx_ai_predictions_date ON ai_predictions(prediction_date);
