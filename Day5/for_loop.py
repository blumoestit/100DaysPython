### SIMPLEST EXERCISES :) ####

number_of_sth = [34, 45, 52, 55, 24, 33]
number_of_items = 0
sum_of_items = 0
for item in number_of_sth:
    number_of_items += 1
    sum_of_items += item
    
print(number_of_items)
print(sum_of_items)


###
scores = input("Input a list of scores using only spaces between the numbers ").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])
print(scores)

highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score
    # print(highest_score)
    
print(f"The highest score is: {highest_score}")


###
for number in range(0, 11, 2):
    print(number)
    

###
total = 0

for number in range(0, 11, 2):
    total += number
    print(total)
    
print(total)


### Adding even numbers
even_sum = 0
for i in range(0, 11, 2):
    even_sum += i
    
print(even_sum)

# alternative
alternative_even_sum = 0
for i in range(1, 11):
    if i % 2 == 0:
    # print(number)
        alternative_even_sum += i
        
print(alternative_even_sum)



    
    
    
    