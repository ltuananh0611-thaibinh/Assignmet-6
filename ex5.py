def remove_odd_numbers(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


nums = [1, 2, 3, 4, 5, 6, 7, 8]

result = remove_odd_numbers(nums)

print("Original list:", nums)
print("List without odd numbers:", result)
