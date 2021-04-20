hrs=input("Enter number of hours:")
hrs=float(hrs)
rate=input("Enter rate per hour:")
rate=float(rate)
if hrs<=40:
    pay=hrs*rate
elif hrs>40:
    rate1=1.5*rate
    initial=40*rate
    hrs=hrs-40
    pay=initial+(hrs*rate1)
print(pay)
