def run():
    cuadrados = []
    for x in range(1,101):
        cuadrados.append(x**2)
    print(cuadrados)
    
# Creo mi entrypoint
if __name__ == "__main__":
    run()