import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor = actor_director.groupby(
        ['actor_id', 'director_id']
    ).size().reset_index(name='count')

    actor = actor[actor['count'] >= 3]

    return actor[['actor_id', 'director_id']]