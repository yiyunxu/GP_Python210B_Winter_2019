#!/usr/bin/env python3

# series 1

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
# response1 = input("Please add another fruit to the list: ")
# response1 = response1.capitalize()
# fruits.append(response1)
# print(fruits)
# fruit_count = len(fruits)
# response2 = input("Pick a number between 1 and {}: ".format(fruit_count))
# num = int(response2)
# y = num - 1
# name_fruit = fruits[y]
# print("{} is {}".format(num, name_fruit))
# response3 = input("Add another fruit to the list: ")
# fruits = [response3.capitalize()] + fruits
# print(fruits)
# response4 = input("Give me one more fruit: ")
# fruits.insert(0, response4.capitalize())
# print(fruits)
# print("The fruits that start with the letter P are:")
# for p_fruit in fruits:
#     if p_fruit[0] == 'P':
#         print(p_fruit)


# series 2

# fruits2 = fruits
# print(fruits2)
# print("The last fruit will be removed")
# fruits2.pop()
# print(fruits2)
# bye_fruit = input("Pick one more fruit from the list to remove: ")
# fruits2.remove(bye_fruit)
# print(fruits2)


# series 3

fruits3 = fruits
list_length = len(fruits3)
n = 0
while n < list_length:
    tasty = input("Do you like {}? ".format(fruits3[n].lower()))
    n = n + 1 


    # while tasty == "no" or tasty == "yes": 
    #     if tasty == "no":
    #         fruits3.remove()
    #     else:
    #         continue
    # if tasty != "no" and tasty != "yes":        
    #     print("Please try again and enter yes or no") 

    


# series 4

fruits4 = fruits[:]
for rev_fruit in fruits4:
    print(rev_fruit[::-1])
fruits.pop()
print("This is the original list")
print(fruits)
print("This is the copy of the list")
print(fruits4)    