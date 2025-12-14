p=float(input("enter principle value:"))
t=float(input("enter time period:"))
r=float(input("enter rate of interest:"))
a=p*(1+r/100)**t
CI=a-p
print("Compound interest" ,CI)
