import pandas as pd

def game_analysis(df: pd.DataFrame) -> pd.DataFrame:
    df['event_date'] = pd.to_datetime(df['event_date'])
    return df.groupby('player_id', as_index = False)['event_date'].min().rename(columns = {
        'event_date': 'first_login'
    })
