#Read lines from TSLA.txt
file = open("/workspaces/DATA_3500_Isaac_Morris/HW4/TSLA.txt")
lines = file.readlines()
for line in lines:
    price = float(line)
    price = round(price, 2) # to round the price to 2 decimals
    print(price)
