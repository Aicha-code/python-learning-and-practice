def find_number(numbers, target, start_index=0):
    
    if numbers is None or len(numbers) == 0:
        return -1
    middle_index = len(numbers) // 2
    print(f"Middle index is: {middle_index}, Middle element is: {numbers[middle_index]}")

    if target == numbers[middle_index]:
        return middle_index+ start_index
    elif target < numbers[middle_index]:
        return find_number(numbers[0:middle_index], target, start_index)
    elif target > numbers[middle_index]:
        return find_number(numbers[middle_index+1:], target, start_index + middle_index + 1)
    else:
        return -1
def add_number(number, numbers):
    numbers.append(number)
    return numbers
    
if __name__ == "__main__":
    print("Welcome, this is a number finder program.\n You can search for a number in a list.")
    list_of_numbers = input("Enter an ordered list of numbers separated by spaces: ")
    numbers = list(map(int, list_of_numbers.split()))
    print("The list of numbers you entered is:", numbers)
    print(f"length of the list is: {len(numbers)}")

    target = int(input("Enter the number you want to find: "))
    result = find_number(numbers, target)
    if result != -1:
        print(f"Number found at index: {result}")
    else:
        print("Number not found, add? (y/n)")
        user_input = input()
        if user_input.lower() == 'y':
            new_array= add_number(target, numbers)
            print("New list of numbers:", new_array)
        else:
            print('exiting program...')