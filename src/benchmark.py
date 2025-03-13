import matplotlib.pyplot as plt
from search_algorithms import linear_search, binary_search, ternary_search
from data_generator import generate_random_list, generate_sorted_list
from executor import measure_time

def plot_performance_sorted():
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    linear_times = []
    binary_times = []
    ternary_times = []

    for size in sizes:
        arr = generate_sorted_list(size)
        x = arr[-1]  # Buscamos el último elemento (peor caso para búsqueda lineal)

        _, time_linear = measure_time(linear_search, arr, x)
        _, time_binary = measure_time(binary_search, arr, x)
        _, time_ternary = measure_time(ternary_search, arr, x)

        linear_times.append(time_linear)
        binary_times.append(time_binary)
        ternary_times.append(time_ternary)

    plt.plot(sizes, linear_times, label='Linear Search')
    plt.plot(sizes, binary_times, label='Binary Search')
    plt.plot(sizes, ternary_times, label='Ternary Search')
    plt.xlabel('Tamaño del array')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Rendimiento en arrays ordenados (mediana de 100 ejecuciones)')
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
def plot_performance_unsorted():
    sizes = [10, 100, 1000, 10000, 100000]
    linear_times = []

    for size in sizes:
        arr = generate_random_list(size)
        x = arr[-1]  # Buscamos el último elemento

        _, time_linear = measure_time(linear_search, arr, x)
        linear_times.append(time_linear)

    plt.plot(sizes, linear_times, label='Linear Search')
    plt.xlabel('Tamaño del array')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Rendimiento en arrays desordenados (mediana de 100 ejecuciones)')
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
def plot_performance_by_position():
    size = 100000
    arr = generate_sorted_list(size)
    positions = [0, size // 4, size // 2, 3 * size // 4, size - 1]
    linear_times = []
    binary_times = []
    ternary_times = []

    for pos in positions:
        x = arr[pos]

        _, time_linear = measure_time(linear_search, arr, x)
        _, time_binary = measure_time(binary_search, arr, x)
        _, time_ternary = measure_time(ternary_search, arr, x)

        linear_times.append(time_linear)
        binary_times.append(time_binary)
        ternary_times.append(time_ternary)

    plt.plot(positions, linear_times, label='Linear Search')
    plt.plot(positions, binary_times, label='Binary Search')
    plt.plot(positions, ternary_times, label='Ternary Search')
    plt.xlabel('Posición del elemento buscado')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Rendimiento según la posición del elemento (mediana de 100 ejecuciones)')
    plt.legend()
    plt.show()
    
def plot_average_vs_worst_case():
    sizes = [10, 100, 1000, 10000, 100000]
    linear_avg_times = []
    linear_worst_times = []
    binary_avg_times = []
    binary_worst_times = []
    ternary_avg_times = []
    ternary_worst_times = []

    for size in sizes:
        arr = generate_sorted_list(size)

        # Caso promedio: buscar un elemento en el medio
        x_avg = arr[size // 2]
        _, time_linear_avg = measure_time(linear_search, arr, x_avg)
        _, time_binary_avg = measure_time(binary_search, arr, x_avg)
        _, time_ternary_avg = measure_time(ternary_search, arr, x_avg)

        # Peor caso: buscar el último elemento
        x_worst = arr[-1]
        _, time_linear_worst = measure_time(linear_search, arr, x_worst)
        _, time_binary_worst = measure_time(binary_search, arr, x_worst)
        _, time_ternary_worst = measure_time(ternary_search, arr, x_worst)

        linear_avg_times.append(time_linear_avg)
        linear_worst_times.append(time_linear_worst)
        binary_avg_times.append(time_binary_avg)
        binary_worst_times.append(time_binary_worst)
        ternary_avg_times.append(time_ternary_avg)
        ternary_worst_times.append(time_ternary_worst)

    plt.plot(sizes, linear_avg_times, label='Linear Search (avg)')
    plt.plot(sizes, linear_worst_times, label='Linear Search (worst)')
    plt.plot(sizes, binary_avg_times, label='Binary Search (avg)')
    plt.plot(sizes, binary_worst_times, label='Binary Search (worst)')
    plt.plot(sizes, ternary_avg_times, label='Ternary Search (avg)')
    plt.plot(sizes, ternary_worst_times, label='Ternary Search (worst)')
    plt.xlabel('Tamaño del array')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de casos promedio y peor caso (mediana de 100 ejecuciones)')
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()