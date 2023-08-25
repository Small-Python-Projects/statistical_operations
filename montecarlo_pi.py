import random

def isInTheCircle():
    
    inthecircle = 0
    
    x = random.uniform(-1,1)
    
    y = random.uniform(-1,1)
    
    if(x**2 + y**2 <= 1):
    
        inthecircle = True
        
    return inthecircle;
        
ndarts = int(input("Enter the number of darts to throw at the board: "))

n = 0

nhit = 0

while(n <= ndarts):
    
    incircle = isInTheCircle()
    
    if(incircle == True):
        
        nhit = nhit + 1
        
    n = n + 1
        
pi = str(4.0*nhit/ndarts)

print("pi works out to be... "+pi)