z = 0

#change the number below to your state's sales tax is.
tax = .0625

while 1 > 0:
    x = input('What is the price of your next item? If you are done type Done:')
    if str(x) == str('Done'):
        y = float(y) * float(tax) + float(y)
        z = round(y, 2)
        print('Your total is ',z)
        break
    elif str(x) == str('done'):
     y = float(y) * float(tax) + float(y)
     z = round(y, 2)
     print('Your total is $',z)
     break
    y = float(z) + float(x)            
    z = y
    x = 0
    print(y)