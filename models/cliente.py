import streamlit as st

#--------------------------
#CLASE POO                  

class cliente:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
    
    #GETTERS (EMCAPSULAMIENTO)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_saldo(self):
        return self.__saldo


    # METODO
    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Edad: {self.edad}, Saldo: {self.saldo}"
