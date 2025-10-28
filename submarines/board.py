import random

def matrix_size():
    return int(input('Matrix size: '))

def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    ships = [[fill for i in range(size)] for i in range(size)]
    return ships

def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    shots = [[fill for i in range(size)] for j in range(size)]
    return shots

def in_bounds(size: int, x: int, y: int) -> bool:
    return 0 <= x < size and 0 <= x < size

def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    counter = 0
    for i in range(len(shots)):
        for j in range(len(shots)):
            if ships[i][j] == 0 and shots[i][j]:
                counter += 1
    return counter  

def number_of_submarines() -> int:
    return int(input('How many submarines? ')) 

def check_number_of_submarines(size):
    if number_of_submarines() > size*size or number_of_submarines() <= 0:
        amount = number_of_submarines()
    return amount

def random_index(size):
    num = random.randrange(range(len(size)))
    return num

def add_submarines_in_metrix(metrix: list[list[int]], submarines: int, size: int):
    counter = submarines
    while counter > 0:
        x = random_index(size)
        y = random_index(size)
        if metrix[x][y] == False:
            metrix[x][y] == True
            counter -= 1
    return metrix
