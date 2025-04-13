def calculate_order_book_depth(order_book_df):
    bid_depth = order_book_df[['BidQtyL' + str(i) for i in range(1, 21)]].sum(axis=1)
    ask_depth = order_book_df[['AskQtyL' + str(i) for i in range(1, 21)]].sum(axis=1)
    return bid_depth, ask_depth

def calculate_price_acceleration(trade_df, time_window=2):
    trade_df['PriceDiff'] = trade_df['Price'].diff()
    trade_df['TimeDiff'] = trade_df['Time'].diff().dt.total_seconds()
    trade_df['Acceleration'] = trade_df['PriceDiff'].diff() / trade_df['TimeDiff'].diff()
    return trade_df