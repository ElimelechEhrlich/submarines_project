import random

def matrix_size():
    return int(input('Matrix size: '))

def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    ships = [[fill for i in range(size)] for i in range(size)]
    return ships

def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    shots = [[fill for i in range(size)] for i in range(size)]
    return shots

def in_bounds(size: int, x: int, y: int) -> bool:
    return 0 <= x < size and 0 <= x < size

