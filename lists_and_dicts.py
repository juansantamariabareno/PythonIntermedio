def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Juan", "lastname": "Santamaria"}

    # Esta sera una lista que contenga diccionarios (lista de diccionarios)
    super_list = [
        {"firstname": "Juan", "lastname": "Santamaria"},
        {"firstname": "Diego", "lastname": "Bareño"},
        {"firstname": "Julieth", "lastname": "Garnica"},
        {"firstname": "Marylight", "lastname": "Patiño"},
        {"firstname": "Juan", "lastname": "Perez"}
    ]

    # Diccionario que contiene listas (diccionario de listas)
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    # Hacemos un ciclo for para recorrer el diccionario
    # Recorremos las llaves y valores en un mismo ciclo con .items()
    for key, value in super_dict.items():
        print(key, "-", value)

    # Hacemos un ciclo for para recorrer la lista
    for values_list in super_list:
        # Ahora que ya recorremos la lista, imprimimos los valores del diccionario
        for key, value in values_list.items():
            print(key, "-", value)

# entrypoint que ejecuta la función al cargar el codigo de python
if __name__ == '__main__':
    run()