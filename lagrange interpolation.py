import numpy as np
import matplotlib.pyplot as mpl

x = [1.0,1.5,2.0]
x = np.array(x)
k = np.array(x)
a = np.arange(1.0,2.0,0.01)
h = 0.00
def f(x):
    return np.log(x)


for i in range (0,3):
    t = 1.00
    y = f(x[i])
    print('\nf(x) = ',y)
    for j in range (0,3):
        
        print('\nlagrange expansion:')
        if x[j] == x[i]:
            h = 0.00
            print('h=',h,'xi=',x[i],'xj=',x[j])
            
        else:
            print('xi=',x[i],'xj=',x[j])
            t = t*(k[i] - x[j])/(x[i] - x[j])
            h = y*t
            print('x',x[i],'h={:.3f}'.format(h))
            mpl.plot(x[i],h,'rx')
    
mpl.xlim(0.5,2.2)
mpl.ylim(-0.1,1.0)
mpl.plot(a,f(a),'y-')
mpl.ylabel('f(x)')
mpl.xlabel('x')
mpl.show()