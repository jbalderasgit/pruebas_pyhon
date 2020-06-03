nombre= (input("Dame tu nombre: ")) 
c1= int(input("calificacion 1: ")) 
c2= int(input("calificacion 2: ")) 
c3= int(input("calificacion 3: ")) 
prom=(c1+c2+c3)/3
if prom >=7:
        print("Aprobaste la materia, felicidades. Promedio:",prom)
else:
        print("Reprobaste la materia, lo siento,  Promedio: ",prom)