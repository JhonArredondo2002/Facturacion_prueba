import random
import string

nCadenas=40

cu=""
def generaCadena():
    global cu
    for i in range(1, nCadenas+1):
        MiCadena = string.ascii_letters + string.digits   
        caraf="".join(random.choice(MiCadena)  for j in range(1))
        
        if(cu==""):
            cu=caraf
            i+=1
        else:
            cu=cu+caraf
            i+=1
        print(cu)
    return cu.lower() 


    #guardamos datos

