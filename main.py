import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from datetime import datetime
import manejo_de_productos
import manejo_de_usuarios
import ventas

fecha = datetime.today()
bandera_global = 0
nombre_empleado = "Error"
total_venta = 0.00
