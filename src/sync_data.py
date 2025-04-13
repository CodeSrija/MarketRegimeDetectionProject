import pandas as pd

def sync_trade_order_data(trade_df, order_book_df):
    synced_data = pd.merge_asof(trade_df, order_book_df, on='Time', direction='nearest')
    return synced_data