import random
flag= False
m = 0
numb=[0 for i in range(100)]
pin=[[0 for i in range(5)] for j in range(100)]
r=[0 for k in range(10)]
while (m < 1000):
    n=0
    while (n < 2): 
        p=0
        print("grapse 5 arithmous apo to 1 ws to 80")
        while True:
            a = input()
            if int(a) < 80 and int(a) > 0:
                
                pin[n][p] = a 
                break
        while True:        
            b = input()
            if int(b) < 80 and int(b) > 0:
                p=p+1
                pin[n][p] = b
                break
	while True: 
            c = input()
            if int(c) < 80 and int(c) > 0:
                p=p+1
                pin[n][p] = c
                break	
	while True:
	    d=input()
            if int(d) < 80 and int(d) > 0:
                p=p+1
                pin[n][p] = d
                break
        while True:    
            e = input()
            if int(e) < 80 and int(e) > 0:
                p=p+1
                pin[n][p] = e
                break  
        n=n+1
	while flag == False : 
	    rand=random.randint(1,80)   
	    for n in range (100):
        	r[m]=1
	        for j in range (5):
	            
	            r[m]=r[m]+1
	            if int(pin[n][j])==rand:
	                
	                numb[n]=numb[n]+1
	                if int(numb[n])==5:
	                    print ('BINGO!!!!')
			    flag = True	
	                    break
	                    break
    m=m+1

s = 0
for k in range (1,1000):
    s = s+r[k]

mo=s/1000




		
