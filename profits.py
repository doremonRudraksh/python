months = ("january", "Febraury","March", "April", "May", "June", "july", "August", "September", "October", "November", "December")

profits = (20000,45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

max_profit = max(profits)
max_index = profits.index(max_profit)
print(max_index)

max_month = months[max_index]
print("Maximum profit of  " + str(max_profit) + " was recoreded in the month of " + str(max_month) )

min_profit = min(profits)
min_index = profits.index(min_profit)
print(min_index)

min_month = months[min_index]
print("minimum  profit of " + str(min_profit) + " was recorded in  the month of " + str(min_month))
