z = 0
a = 0
#change the number below to your state's sales tax is.
tax = .0625

while 1 > 0:
    x = input('What is the price of your next item? If you are done type Done:')
    if str(x) == str('Done'):
        y = float(y) * float(tax) + float(y)
        z = round(y, 2)
        a3 = z/a
        a4 = round(a3, 2)
        print('---------------------------------------------------')
        print('Your total is $',z)
        print('The Average Price of your order is $',a4,'.')
        print('You ordered',a, 'items.')
        break
    elif str(x) == str('done'):
     y = float(y) * float(tax) + float(y)
     z = round(y, 2)
     a3 = z/a
     a4 = round(a3, 2)
     print('---------------------------------------------------')
     print('Your total is $',z)
     print('The Average Price of your order is $',a4,'.')
     print('You ordered',a, 'items.')
     break
    if float(x) > 0:
        a2 = a + 1
        a = a2
    
    y = float(z) + float(x)            
    z = y
    x = 0
    print(y)