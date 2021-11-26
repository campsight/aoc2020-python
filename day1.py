# Using readlines()
file = open('data/input-day1.txt', 'r')
lines = file.readlines()

input_list = [int(x) for x in lines]

# part 1
for i in range(len(input_list)):
    number = input_list[i]
    for j in range((i+1), len(input_list)):
        number2 = input_list[j]
        if (number + number2) == 2020:
            print(f"{i}th number {number} + {j}th number {number2} is 2020. Their product: {number*(number-2020)}")
            break
    else:
        continue
    break

# alt part 1 (faster?)
for i in range(len(input_list)):
    number = input_list[i]
    if (2020 - number) in input_list[i+1:len(input_list)]
        print(f"{i}th number {number} + {2020 - i} is 2020. Their product: {number * number2}")
        break

# part 2
for i in range(len(input_list)):
    number = input_list[i]
    for j in range((i+1),len(input_list)):
        number2 = input_list[j]
        for k in range((j + 1), len(input_list)):
            number3 = input_list[k]
            if (number + number2 + number3) == 2020:
                print(f"{i}th number {number} + {j}th number {number2} + {k}th number {number3} is 2020. Their product: {number*number2*number3}")
                break
        else:
            continue
        break
    else:
        continue
    break
