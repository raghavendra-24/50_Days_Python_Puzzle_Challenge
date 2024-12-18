def sum_even(input_num: list[int]) -> int:
    sum=0
    length = len(input_num)
    for i in range(length):
        if(input_num[i]%2==0):
            sum+=input_num[i]

    return sum

print(sum_even([1,2,3,4,5,6,7,8,9,10]))