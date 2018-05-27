segundos = int(input("Segundos: "))

horas = segundos//3600
segundos -= horas*3600

minutos = segundos//60
segundos -= minutos*60

print("%i:%i:%i"%(horas,minutos,segundos))
