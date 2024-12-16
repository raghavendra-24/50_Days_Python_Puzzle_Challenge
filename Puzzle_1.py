# Task
# Define a function filter_strings_containing_a that takes one
# parameter:
# Name Type Example Input
# input_strs list of str ["apple", "banana", "cherry", "date"]
# When called, the function should return a new list containing only
# strings that contain the letter “a”.


def filter_strings_containing_a(input_Strings: list[str]) -> list[str]:
    result = []
    for word in input_Strings:
        if 'a' in word:
            result.append(word)


    return result

print(filter_strings_containing_a(['apple','banana','pie']))