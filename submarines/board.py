import random

def matrix_size():
    return int(input('Matrix size: '))

def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    ships = [[fill for i in range(size)] for i in range(size)]
    return ships