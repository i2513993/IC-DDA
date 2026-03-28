class Cliente:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
    
    # METODO PARA MOSTRAR INFORMACIÓN
    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Edad: {self.edad}, Saldo: {self.saldo}"

    # MÉTODO PARA VALIDAR MAYORÍA DE EDAD INTERNAMENTE
    def es_mayor_de_edad(self):
        return self.edad >= 18

    # MÉTODO PARA CLASIFICAR SEGÚN EL SALDO
    def clasificar_cliente(self):
        if self.saldo > 1000:
            return "Cliente Premium"
        return "Cliente Regular"