from models.cliente import Cliente

def crear_cliente(nombre, edad, saldo):

    #Validación 1:Nombre
    if nombre == "":
        raise ValueError("El nombre es obligatorio")

    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre solo debe de contener letras")

    #Validación 2:Edad
    if edad < 18:
        raise ValueError ("El cliente debe ser mayor de edad")

    #Validación 3:Saldo
    if saldo < 0:
        raise ValueError("El saldo no puede ser negativo")

    
    cliente = Cliente(nombre, edad, saldo)

    if saldo == 0:
        mensaje = "Cliente sin saldo"
    else:
        mensaje = "Cliente con saldo"
    
    return cliente, mensaje