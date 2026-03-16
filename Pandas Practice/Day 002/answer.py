import pandas as pd
df = pd.DataFrame({
    'date':       pd.date_range('2024-01-01', periods=10, freq='D').tolist() * 3,
    'stock':      ['RELIANCE'] * 10 + ['TCS'] * 10 + ['INFY'] * 10,
    'close_price':[2500, 2520, 2480, 2510, 2550, 2530, 2560, 2590, 2570, 2600,
                   3400, 3420, 3380, 3450, 3470, 3440, 3480, 3500, 3520, 3490,
                   1500, 1520, 1490, 1510, 1530, 1550, 1540, 1560, 1580, 1570]
})

df\
.assign(
    rolling_avg=lambda x: (
        x.groupby('stock')['close_price']
         .transform(
            lambda s: s.rolling(window=3).mean()
        )
    )
)\
.assign(
    pct_change=lambda x: (
        x.groupby('stock')['close_price']
         .transform(lambda s: (s - s.shift(1)) / s.shift(1))
    )
)\
.assign(
    trend=lambda x: np.where(
        x['pct_change'].isna(), None,
        np.where(x['pct_change'] > 0, 'up',
        np.where(x['pct_change'] < 0, 'down', 'flat'))
    )
)