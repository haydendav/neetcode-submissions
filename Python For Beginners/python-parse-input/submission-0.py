from typing import List

def read_integers() -> List[int]:
    numbers = input()
    return [int(x) for x in numbers.split(",")]
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())