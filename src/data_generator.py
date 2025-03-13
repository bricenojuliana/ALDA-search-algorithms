import random

def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def generate_sorted_list(size):
    return sorted(generate_random_list(size))