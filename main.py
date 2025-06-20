# Mude o valor de x ou z e veja a magica!
x = 5  
z = 10 

if x == 1 or z == 1:
    if x * x + z * z - 1 == 100:
        print('true')
    else:
        print('false')
elif x * x + z * z == 100:
    print('true')
else:
    print('false')