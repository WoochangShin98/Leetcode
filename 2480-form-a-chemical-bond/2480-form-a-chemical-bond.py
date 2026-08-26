import pandas as pd

def form_bond(elements: pd.DataFrame) -> pd.DataFrame:
    nonmetal = elements[elements['type'] == 'Nonmetal']
    metal = elements[elements['type'] == 'Metal']
    df = metal.merge(nonmetal,how='cross')
    df = df[['symbol_x','symbol_y']]
    df = df.rename(columns={'symbol_x':'metal','symbol_y':'nonmetal'})
    return df.sort_values('nonmetal',ascending=False)
    