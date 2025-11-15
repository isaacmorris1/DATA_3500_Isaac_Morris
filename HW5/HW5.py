import json
def meanReversionStrategy(prices):
    print("{ticker} Mean Reversion Strategy Output: 2024 - 2025 Data\n-----------------")
    file = open("/workspaces/DATA_3500_Isaac_Morris/HW4/{ticker}.txt")
    lines = file.readlines()
    prices = []
    for line in lines:
        line = float(line)
        prices.append(line)
    counter = 0
    final_profit = 0
    buy = 0
    first_buy = True
    for price in prices:
        current_price = price
        avg_price = (prices[counter] + prices[counter - 1] + prices[counter - 2] + prices[counter - 3] + prices[counter - 4]) / 5
        if counter >= 5:
            if current_price < (avg_price * 0.98) and buy == 0:
                print("Buying at:", "\t", price)
                buy = current_price
                if first_buy == True:
                    first_buy = False
                    first_buy_amount = current_price   
            elif current_price > (avg_price * 1.02) and buy != 0:
                trade_profit = current_price - buy
                print("Selling at:", "\t", price)
                trade_profit = round(trade_profit, 2)
                print("Trade profit:", "\t", trade_profit)
                final_profit += trade_profit
                buy = 0
        counter += 1
    final_profit = round(final_profit, 2)
    print("-----------------\nTotal Profit:", "\t", final_profit)
    print("First buy:", "\t", first_buy_amount)
    final_profit_percentage = ( final_profit / first_buy_amount ) * 100
    final_profit_percentage = round(final_profit_percentage, 2)
    print("%", "return:", final_profit_percentage)
    return final_profit, final_profit_percentage

def simpleMovingAverageStrategy(prices):
    print("{ticker} Mean Reversion Strategy Output: 2024 - 2025 Data\n-----------------")
    file = open("/workspaces/DATA_3500_Isaac_Morris/HW4/{ticker}.txt")
    lines = file.readlines()
    prices = []
    for line in lines:
        line = float(line)
        prices.append(line)
    counter = 0
    final_profit = 0
    buy = 0
    first_buy = True
    for price in prices:
        current_price = price
        avg_price = (prices[counter] + prices[counter - 1] + prices[counter - 2] + prices[counter - 3] + prices[counter - 4]) / 5
        if counter >= 5:
                buy = current_price
                if first_buy == True:
                    first_buy = False
                    first_buy_amount = current_price   
                trade_profit = current_price - buy
                print("Selling at:", "\t", price)
                trade_profit = round(trade_profit, 2)
                print("Trade profit:", "\t", trade_profit)
                final_profit += trade_profit
                buy = 0
        counter += 1
    final_profit = round(final_profit, 2)
    print("-----------------\nTotal Profit:", "\t", final_profit)
    print("First buy:", "\t", first_buy_amount)
    final_profit_percentage = ( final_profit / first_buy_amount ) * 100
    final_profit_percentage = round(final_profit_percentage, 2)
    print("%", "return:", final_profit_percentage)
    return final_profit, final_profit_percentage

tickers = {"AAPL", "ADBE", "AMZN", "CSCO", "CVX", "GOOG", "JPM", "MSFT", "NVDA", "TSLA"}
for ticker in tickers:
    file = open("/workspaces/DATA_3500_Isaac_Morris/HW4/{ticker}.txt")
    lines = file.readlines()
    prices = []
    for line in lines:
        line = float(line)
        prices.append(line)
meanReversionStrategy()