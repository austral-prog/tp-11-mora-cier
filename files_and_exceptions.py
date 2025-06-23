def read_file_to_dict(files_name):
	ventas_dict = dict()
	with open (files_name, "r") as file:
		linea = file.reader().strip()
		ventas = linea.split("";"")

		for venta in ventas:
			if ventas:
				producto, valor = venta.split("":"")
				valor = float(valor)
				if producto not i nventas_dict:
					ventas_dict[producto] = []
					ventas_dict[producto].append(valor)
					return ventas_dict

def process_dict():
	for producto in sorted(data.keys()):
		lista_ventanas = data[producto]
		total = sum(lista_ventanas)
		promedio = total / len(lista_ventanas)
		print(f"{producto}: ventas totales ${total: .2f}, promedio ${promedio: .2f}")
