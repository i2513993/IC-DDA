from models.cliente import Cliente

def crear_cliente(nombre, edad, saldo):
    # Validaciones de nombre
    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío")

    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre solo puede contener letras")
    
    # Validaciones de edad
    if edad < 18:
        raise ValueError("El cliente debe ser mayor de edad (mínimo 18 años)")
    
    # Validaciones de saldo
    if saldo < 0:
        raise ValueError("El saldo no puede ser un valor negativo")

    # Si pasa las validaciones, creamos el objeto
    nuevo_cliente = Cliente(nombre, edad, saldo)

    # Lógica para el mensaje de retorno
    if saldo == 0:
        mensaje = "Registro exitoso: El cliente no cuenta con fondos iniciales."
    else:
        mensaje = f"Registro exitoso: Fondos iniciales de {saldo} detectados."
    
    return nuevo_cliente, mensaje