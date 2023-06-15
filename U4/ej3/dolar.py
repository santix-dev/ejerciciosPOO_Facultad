import requests
import json
class Dolar():
	def __init__(self):
		self.__response = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
		self.__text=self.__response.json()
		self.__venta=self.__text[0]["casa"]["venta"]
		self.__oficial=self.__text[0]["casa"]["compra"]
	def venta(self):
		return round(float(self.__venta.replace(",",".")),2)
	def oficial(self):
		return round(float(self.__oficial.replace(",",".")),2)
