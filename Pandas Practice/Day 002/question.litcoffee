df = pd.DataFrame({
    'date':       pd.date_range('2024-01-01', periods=10, freq='D').tolist() * 3,
    'stock':      ['RELIANCE'] * 10 + ['TCS'] * 10 + ['INFY'] * 10,
    'close_price':[2500, 2520, 2480, 2510, 2550, 2530, 2560, 2590, 2570, 2600,
                   3400, 3420, 3380, 3450, 3470, 3440, 3480, 3500, 3520, 3490,
                   1500, 1520, 1490, 1510, 1530, 1550, 1540, 1560, 1580, 1570]
})


1. For each stock, calculate the 3-day rolling average of close_price
2. For each stock, calculate the daily return — percentage change from previous day's close
3. Add a trend column — 'up' if today's close is higher than yesterday's, 'down' if lower, 'flat' if the same
4. Find the single date where RELIANCE had its highest daily return
5. For each stock, find the first date where the rolling average crossed above 2520 / 3440 / 1530 (their respective thresholds)