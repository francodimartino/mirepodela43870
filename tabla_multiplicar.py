import sys

if len(sys.argv)==2:
        
    
    numero=int(sys.argv[1])


    for i in range(1,11):
        print(f"{numero}x{i}={numero*i}")
else:
    print("che te equivocaste de cantidad de argumentos ")