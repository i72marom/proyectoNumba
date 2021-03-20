import medio_nivel as m

def main():
	exit = False

	m.imprimeAyuda()
	while not exit:
		exit = m.menu()

	print("Saliendo...")

if __name__ == "__main__":
	main()
