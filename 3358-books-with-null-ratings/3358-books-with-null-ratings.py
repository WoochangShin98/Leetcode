import pandas as pd

def find_unrated_books(books: pd.DataFrame) -> pd.DataFrame:
    # no rating , book_id asc
    df = books[books['rating'].isna()]
    return df[['book_id','title','author','published_year']].sort_values('book_id')