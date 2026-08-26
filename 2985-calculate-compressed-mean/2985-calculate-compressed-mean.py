import pandas as pd

def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    orders['total'] = orders['item_count'] * orders['order_occurrences']
    orders['average_items_per_order'] = orders['total'].sum() / orders['order_occurrences'].sum()
    return orders[['average_items_per_order']].round(2).drop_duplicates()