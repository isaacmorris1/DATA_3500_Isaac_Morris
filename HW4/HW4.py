#Read lines from TSLA.txt
file = open("/workspaces/DATA_3500_Isaac_Morris/HW4/TSLA.txt")
lines = file.readlines()
prices = []
for line in lines:
    line = float(line)
    line = round(line, 2) # to round the price to 2 decimals
    prices.append(line)
counter = 0
final_profit = 0
first_buy = True
for price in prices:
    current_price = price
    avg_price = (prices[counter] + prices[counter - 1] + prices[counter - 2] + prices[counter - 3] + prices[counter - 4]) / 5
    buy = current_price
    if current_price < avg_price * 0.98:
        print("Buying at:", "\t", price)
        if first_buy == True:
            first_buy = False
            first_buy_amount = current_price   
    elif current_price > avg_price * 1.02:
        trade_profit = current_price - buy
        print("Selling at:", "\t", price)
        print("Trade profit:", "\t", trade_profit)
        final_profit += trade_profit
    counter += 1
print("Total Profit:", "\t", final_profit)
print("First buy:", "\t", first_buy_amount)
final_profit_percentage = ( final_profit / first_buy_amount ) * 100
print("%", "return:", final_profit_percentage)