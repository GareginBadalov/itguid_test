def marco_polo(value: int):
    result = []
    digits_list = [int(digit) for digit in str(value)]
    divisible_by_3 = sum(digits_list) % 3 == 0
    divisible_by_5 = digits_list[-1] == 0 or digits_list[-1] == 5
    divisible_by_5_and_3 = divisible_by_3 and divisible_by_5
    match [divisible_by_3, divisible_by_5, divisible_by_5_and_3]:
        case [True, True, True]:
            print("МаркоПолло")
            result.append("МаркоПолло")
        case [True, False, False]:
            print("Марко")
            result.append("Марко")
        case [False, True, False]:
            print("Полло")
            result.append("Полло")
        case _:
            print(value)
            result.append(value)
    return result
