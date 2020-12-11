#first oefening

group_of_people = ['Alex', 'Eliot', 'Veronica', 'Lucy', 'Wouter', 'Bart']

first_chars = [i[0][:1] for i in group_of_people]
print(first_chars)

first_chars_two = list(i[0][:1] for i in group_of_people)
print(first_chars_two)

#second oefening

numbers = list(range(100))

#using a for loop:

def sum_numbers(numbers_list):
    sum = 0
    for i in numbers_list:
        sum+= i
    return sum

print(sum_numbers(numbers))

#using the sum mechanic:

sum_numbers_two = sum(numbers)
print(sum_numbers_two)