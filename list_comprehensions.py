def run():
    # cuadrados = []
    # for x in range(1,101):
    #     if x % 3 != 0:
    #         cuadrados.append(x**2)
    # print(cuadrados)

    # Usando list comprehensions
    cuadrados = [x**2 for x in range(1, 101) if x % 3 != 0]
    print(cuadrados)
    
# Creo mi entrypoint
if __name__ == "__main__":
    run()