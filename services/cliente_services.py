from models.cliente import Cliente

def crear_cliente(nombre, edad, saldo):
    
    #Validaciones de nombre
    if nombre == "":
        raise ValueError ("El nombre no puede estar vacio")
    
    #Validaciones de edad
    if edad < 18:
        raise ValueError ("El cliente debe ser mayor de edad")
    
    #Validaciones de saldo
    if saldo < 0:
        raise ValueError ("El saldo es invalido")

    cliente = Cliente (nombre, edad, saldo)

    if saldo == 0:
        mensaje = "Cliente sin saldo"
    else:
        mensaje = "Cliente con saldo"
    
     return cliente, mensaje