class ObjectEncoder(object):
	"""docstring for ObjectEncoder"""
	def guardarJSON(self,d,archivo):
		with archivo.open("w",encoding="UTF-8") as destino:
			json.dump(d,destino,indent=4)
			destino.close()
		