n=int(input("Enter the number of rows:"))
for i in range(n):
    val = i+1
    dec = n-1
    for j in range(i+1):
        print(format(val,"<5"),end = " ")
        val = val+dec
        dec = dec-1
    print()
