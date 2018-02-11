


def rot13(s):
#lista mikrwn gramatwn
    abcl ='abcdefghijklmnopqrstuvwxyz'
#lista kefalaivn grammatwn
    abcu='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ns=''

    for char in s :
        
        if char in abcl:
            p = abcl.find(char)
            np = (p+13)%26     
            nchar=abcl[np]
            ns += nchar

        elif char in abcu:
            p = abcu.find(char)
            np = (p+13)%26     
            nchar=abcu[np]
            ns += nchar 

        else:
            ns += char
    return ns


s=raw_input('grapse kati:')




print "to kodikopoihmeno kimeno einai :",rot13(s) 

