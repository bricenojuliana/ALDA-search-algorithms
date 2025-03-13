import time
import numpy as np

def measure_time(search_function, arr, x, repetitions=100):
    times = []
    for _ in range(repetitions):
        start_time = time.time()
        result = search_function(arr, x)
        end_time = time.time()
        times.append(end_time - start_time)
    return result, np.median(times)