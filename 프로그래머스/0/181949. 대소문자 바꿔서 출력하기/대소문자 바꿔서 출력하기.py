input_str = input()

def convert_case(input_str):
    result = []
    for char in input_str:
        if char.islower():
            result.append(char.upper())
        else:
            result.append(char.lower())
    return ''.join(result)

converted_str = convert_case(input_str)

print(converted_str)