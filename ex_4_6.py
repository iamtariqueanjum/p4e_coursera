def computepay(h,r):
    if(h<=40):
        pay=h*r
    elif(h>40):
        initial=40*r
        remain=h-40
        pay=initial+(remain*1.5*r)
    return pay
hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")
p = computepay(float(hrs),float(rate))
print("Pay",p)
