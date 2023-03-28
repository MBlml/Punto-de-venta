#FUNCIONES DE LA TABLA DE MERCANCIA
import psycopg2
from datetime import datetime


class Articulos:

	def abrir(self):
		conexion = psycopg2.connect(database="bd1",
		                            user="postgres",
		                            password="_password05_")
		return conexion

	def alta(self, datos):
		cone = self.abrir()
		cursor = cone.cursor()
		sql = "insert into Mercancia(codigo_barras, descr_mercancia, precio_venta, tipo, cantidad_existencia) values (%s,%s,%s,%s,%s,)"
		cursor.execute(sql, datos)
		cone.commit()

	def consulta(self, datos):
		cone = self.abrir()
		cursor = cone.cursor()
		sql = "select descr_mercancia, precio_venta from Mercancia where codigo_barras=%s"
		cursor.execute(sql, datos)
		return cursor.fetchall()

	def recuperar_todos(self):
		cone = self.abrir()
		cursor = cone.cursor()
		sql = "select codigo_barras, rpad(descr_mercancia, 30, ' '), precio_venta, tipo0, cantidad_existencia from Mercancia order by descr_mercancia"
		cursor.execute(sql)
		return cursor.fetchall()

	def baja(self, datos):
		cone = self.abrir()
		cursor = cone.cursor()
		sql = "delete from Mercancia where codigo_barras = $s"
		cursor.execute(sql, datos)
		cone.commit()
		return cursor.rowcount

	def modificacion(self, datos):
		cone = self.abrir()
		cursor = cone.cursor()
		sql = "update Mercancia set descr_mercancia = %s, precio_venta = %s where codigo_barras = %s"
		cursor.execute(sql, datos)
		cone.commit()
		return cursor.rowcount

	
