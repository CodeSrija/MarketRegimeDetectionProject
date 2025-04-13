import pandas as pd
import os

def parse_time_column(df):
    df['Time'] = df['Time'].str.split('+').str[0]
    df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
    return df

def load_trade_data(filepath):
    df = pd.read_csv(filepath)
    df = parse_time_column(df)
    return df

def load_order_book_data(filepath):
    df = pd.read_csv(filepath)
    df = parse_time_column(df)
    return df

def load_all_data(trade_dir, book_dir):
    trade_files = sorted([os.path.join(trade_dir, f) for f in os.listdir(trade_dir) if f.endswith('.txt')])
    book_files = sorted([os.path.join(book_dir, f) for f in os.listdir(book_dir) if f.endswith('.txt')])
    
    trade_dfs = [load_trade_data(f) for f in trade_files]
    book_dfs = [load_order_book_data(f) for f in book_files]
    
    trade_df = pd.concat(trade_dfs, ignore_index=True)
    book_df = pd.concat(book_dfs, ignore_index=True)
    
    return trade_df, book_df