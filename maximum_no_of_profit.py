#Given the trads of the company maximum your profit.
def maximum_profit(P):
    m=0
    for i in range(0,len(P)):
        for j in range(i+1,len(P)):
            m=max(m,P[j]-P[i])
    return m
prices=[455,460,465,451,414,415,441]
c=maximum_profit(prices)
print("Maximum Profit of Company: ",c)