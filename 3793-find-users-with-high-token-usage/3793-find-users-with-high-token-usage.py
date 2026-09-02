import pandas as pd

def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:
    
    df = (
        prompts.groupby('user_id')
                .agg(
                    prompt_count=('prompt','size'),
                    avg_tokens=('tokens','mean'),
                    max_tokens=('tokens','max')
                )
                .reset_index()
    )

    df = df[
        (df['prompt_count']>=3)&
        (df['max_tokens']>df['avg_tokens'])
    ]

    df['avg_tokens'] = df['avg_tokens'].round(2)
    
    return (
        df.sort_values(
            ['avg_tokens', 'user_id'],
            ascending=[False, True]
        )
        [['user_id', 'prompt_count', 'avg_tokens']]
    )
    return df