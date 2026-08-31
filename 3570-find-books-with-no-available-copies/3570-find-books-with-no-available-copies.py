import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    current = borrowing_records[borrowing_records['return_date'].isna()]
    df = (current.groupby('book_id').size().reset_index(name='current_borrowers'))
    df = library_books.merge(df,on='book_id',how='left')
    df['current_borrowers'] = df['current_borrowers'].fillna(0)
    df = df[df['total_copies'] - df['current_borrowers'] == 0]
    return df[['book_id','title','author','genre','publication_year','current_borrowers']].sort_values(['current_borrowers','title'],ascending=[False,True])