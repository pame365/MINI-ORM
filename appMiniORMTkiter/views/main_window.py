import tkinter as tk
from tkinter import messagebox
from database.connection import  DatabaseConnection

from views.cliente_view import ClienteView
from views.restaurante_view import RestauranteView
from views.repartidor_view import RepartidorView

class MainWindow: 
    """ventana principal"""

    def __init__(self,root):

    #constructor colocamos ventana raiz
    self.root=root
    self.root.title("🍔 FoodieGO - Sistema de Gestión ")
    self.root.geometry("900x600")
    self.root.configure(bg= "f0f0f0")
    
    #Inicializar las bases de datos
    DatabaseConnection.initialize_tables()

    #Generamos Interfaz
    self.crear_menu()
    self.crear_pantalla_inicio()

def _crear_menu(self):
    #Crear barra de menu superior
    barra_menu=tk.Menu(self.root)
    
    