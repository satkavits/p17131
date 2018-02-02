


#dimiourgia sunartisis roman

def roman(num):
    #lista arithmon
        numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    #lista latinikon sumvolon
        romans = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        i = 0

        res = ""

        while num > 0:
            for j in range(num//numbers[i]):
                res += romans[i]
                num -= numbers[i]
            i += 1
        print (res)

    

        


n = input('grapse enan arithmo: ') 

try:         
#sto pythontutor.com to exept ValueError doulevei sto pc mou bgazei NameError roman(int(n)) to opoio den gnorizo apo ti prokaleitai

	roman(int(n))

except ValueError:
    print('den einai arihtmos')
