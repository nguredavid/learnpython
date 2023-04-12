#!/usr/bin/python3


#define function

def stores(words=[]):
    for char in words:
        

        store = ""
        length = len(char)
 

        if length % 2 != 0:
            store += char
            print(store)
            #print('names with odd',char)
        


names = ["David", "Ngure", "Ngonyo"]
print(names)
stores(names)

    

