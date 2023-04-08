def b1_candle_condition(data):
    data=data
    ema5=calculate_ema(data, 5)
    ema15=calculate_ema(data, 15)
    ema30=calculate_ema(data, 30)
    bigcandle = all([abs(data['close'].iloc[::-1][i]-data['open'].iloc[::-1][i]) > abs(data['close'].iloc[::-1][i+1]-data['open'].iloc[::-1][i+1]) for i in range(4)])
    candle_for_buy = all([data['close'].iloc[::-1][i] < ema5[-i] and data['open'].iloc[::-1][i] < ema5[-i] for i in range(1,5)])
    candle_for_sell = all([data['close'].iloc[::-1][i] > ema5[-i] and data['open'].iloc[::-1][i] > ema5[-i] for i in range(1,5)])
    big_candle_buy = abs(data['open'].iloc[-1]-data['close'].iloc[-1]) > abs(data['max'].iloc[-1]-data['close'].iloc[-1])
    big_candle_sell = abs(data['open'].iloc[-1] - data['close'].iloc[-1]) > abs(data['min'].iloc[-1] - data['close'].iloc[-1])*3
    
    # change variable names to snake_case
    for_buy = data['open'].iloc[-1] < ema5[-1] and data['close'].iloc[-1] > ema5[-1] and candle_for_buy and big_candle_buy and bigcandle and data['close'].iloc[-1] < ema15[-1] and data['max'].iloc[-1] < ema15[-1] and ema15[-1] > ema5[-1] and ema30[-1] > ema15[-1]
    for_sell = data['open'].iloc[-1] > ema5[-1] and data['close'].iloc[-1] < ema5[-1] and candle_for_sell and big_candle_sell and bigcandle and data['close'].iloc[-1] > ema15[-1] and data['min']

    return "buy" if for_buy else "sell" if for_sell else "hold"


#B1 Backtest --
def backtest(data):
    ema5=calculate_ema(data, 5)
    ema15=calculate_ema(data, 15)
    ema30=calculate_ema(data, 30)
    bigcandle = all([abs(data['close'].iloc[::-1][i]-data['open'].iloc[::-1][i]) > abs(data['close'].iloc[::-1][i+1]-data['open'].iloc[::-1][i+1]) for i in range(4)])
    candle_for_buy = all([data['close'].iloc[::-1][i] < ema5[-i] and data['open'].iloc[::-1][i] < ema5[-i] for i in range(1,5)])
    candle_for_sell = all([data['close'].iloc[::-1][i] > ema5[-i] and data['open'].iloc[::-1][i] > ema5[-i] for i in range(1,5)])
    big_candle_buy = abs(data['open'].iloc[-1]-data['close'].iloc[-1]) > abs(data['max'].iloc[-1]-data['close'].iloc[-1])*3
    big_candle_sell = abs(data['open'].iloc[-1] - data['close'].iloc[-1]) > abs(data['min'].iloc[-1] - data['close'].iloc[-1])*3
    
    b1candle4buyc = all([data['close'].iloc[::-1][i] < ema5[-i] and data['open'].iloc[::-1][i] < ema5[-i] for i in range(2,6)])
    b1candle4sellc = all([data['close'].iloc[::-1][i] > ema5[-i] for i in range(2,6)]) and all([data['open'].iloc[::-1][i] > ema5[-i] for i in range(2,6)])
    bigcandlec = all([abs(data['close'].iloc[::-1][i]-data['open'].iloc[::-1][i]) > abs(data['close'].iloc[::-1][i+1]-data['open'].iloc[::-1][i+1]) for i in range(4)])
    
    b1buyentry = data['open'].iloc[1] < ema5[1] and \
             data['close'].iloc[1] > ema5[1] and \
             b1candle4buyc and \
             big_candle_buy and \
             bigcandlec and \
             data['close'].iloc[1] < ema15[1] and \
             data['max'].iloc[1] < ema15[1] and \
             ema15[1] > ema5[1] and \
             ema30[1] > ema15[1]

    b1buycheckwin = data['open'][1] < ema5[1] and \
                data['close'][1] > ema5[1] and \
                b1candle4buyc and \
                big_candle_buy and \
                bigcandlec and \
                data['close'][1] < ema15[1] and \
                data['high'][1] < ema15[1] and \
                ema15[1] > ema5[1] and \
                ema30[1] > ema15[1] and \
                data['close'] > data['open']
    b1buycheckloss = data['open'][1] < ema5[1] and \
                 data['close'][1] > ema5[1] and \
                 b1candle4buyc and \
                 big_candle_buy and \
                 bigcandlec and \
                 data['close'][1] < ema15[1] and \
                 data['high'][1] < ema15[1] and \
                 ema15[1] > ema5[1] and \
                 ema30[1] > ema15[1] and \
                 data['close'] < data['open']
    b1sellentry = open[1] > ema5[1] and \
                   close[1] < ema5[1] and \
                   b1candle4sellc and \
                   big_candle_sell and \
                   bigcandlec and \
                   close[1] > ema15[1] and \
                   low[1] > ema15[1] and \
                   ema15[1] < ema5[1] and \
                   ema30[1] < ema15[1]
    b1sellcheckwin = open[1] > ema5[1] and \
                     close[1] < ema5[1] and \
                     b1candle4sellc and \
                     big_candle_sell and \
                     bigcandlec and \
                     close[1] > ema15[1] and \
                     low[1] > ema15[1] and \
                     ema15[1] < ema5[1] and \
                     ema30[1] < ema15[1] and \
                     close < open
    b1sellcheckloss = open[1] > ema5[1] and \
                      close[1] < ema5[1] and \
                      b1candle4sellc and \
                      big_candle_sell and \
                      bigcandlec and \
                      close[1] > ema15[1] and \
                      low[1] > ema15[1] and \
                      ema15[1] < ema5[1] and \
                      ema30[1] < ema15[1] and \
                      close > open

    buy_count = 0
    sell_count = 0
    buy_win = 0
    sell_win = 0
    
    if b1buyentry:
        buy_count += 1
    if b1sellentry:
        sell_count += 1
    if b1buycheckwin:
        buy_win += 1
    if b1sellcheckwin:
        sell_win += 1

print("Buy count:", buy_count)
print("Sell count:", sell_count)
print("Buy win count:", buy_win)
print("Sell win count:", sell_win)