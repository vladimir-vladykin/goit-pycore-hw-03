import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1 or min > max:
        return []
    if max < min or max > 1000:
        return []
    if max - min < quantity:
        # in this case we're never fill set with enoght random numbers
        return []
    
    # set guaranties unique numbers
    numbers_set = set()

    while len(numbers_set) < quantity:
        random_number = random.randint(min, max)
        numbers_set.add(random_number)

    result = list(numbers_set)
    result.sort()
    return result

lottery_numbers = get_numbers_ticket(1, 49, 6)
print(lottery_numbers)
