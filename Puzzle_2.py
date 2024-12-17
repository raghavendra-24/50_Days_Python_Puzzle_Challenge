def sum_if_less_than_fifty(num_one: int, num_two: int) -> int | None:
    sum = num_one+num_two
    if(sum<50):
        return sum
    else:
        return None
    
print(sum_if_less_than_fifty(10,30))
print(sum_if_less_than_fifty(50,0))