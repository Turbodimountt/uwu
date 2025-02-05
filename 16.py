num1 = float(input("numero del caballo "))
num2 = float(input("numero del caballo "))
num3 = float(input("numero del caballo"))
#Determinar el mayor de los tres numeros
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
     mayor = num2
    
else:
    mayor = num3
            
#####Determinar el menor de los tres numeros
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
        menor = num2
else:
            menor = num3
            
######Imprimir los resultados
print(f"el caballo ganador es: {mayor}")
print(f"el caballo perdedor es: {menor}")