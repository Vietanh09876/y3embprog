import random
#Exercise 1
#part a
# rainfall = []

# for x in range(1,8):
#     rainfall.append(float(input(f"rainfall in day {x} in mm: ")))
# 
# for x in rainfall:
#     if x < 5:
#         print("Dry day")
#     elif x > 20:
#         print("Heavy rain")
#     else:
#         print("Average rain")

#part b
# rainfall = []
# dry_day_count = 0
# average_day_count = 0
# heavy_day_count = 0
# 
# for x in range(30):
#     rainfall.append(random.randint(0,30)) 
# 
# for x in rainfall:
#     if x < 5:
#         dry_day_count += 1
#     elif x > 20:
#         heavy_day_count += 1
#     else:
#         average_day_count += 1
# 
# print(f"Dry day: {dry_day_count}, Average rainfall days: {average_day_count}, Wet days: {heavy_day_count}")

#Excercise 2
#part a
# cow_weights = []
# 
# for x in range(1,11):
#     cow_weights.append(float(input(f"cow {x} weight in kg: ")))
# 
# for x in cow_weights:
#     if x < 200:
#         print("Underweight cow")
#     elif x > 400:
#         print("Overweight cow")
#     else:
#         print("Healthy cow")

#part b
# cow_weights = []
# underweight_counter = 0
# healthy_counter = 0
# overweight_counter = 0
# 
# for x in range(1,11):
#     cow_weights.append(float(input(f"cow {x} weight in kg: ")))
# 
# for x in cow_weights:
#     if x < 200:
#         underweight_counter += 1
#     elif x > 400:
#         overweight_counter += 1
#     else:
#         healthy_counter += 1
#         
# print(f"Underweight cows: {underweight_counter}, Healthy Cows: {healthy_counter}, Overweight Cows: {overweight_counter}")
# 
# if healthy_counter > 6:
#     print("The overall heard is good")
# else:
#     print("The herd needs attention")

#part c
# num_cows = int(input("Number of cows you have: "))
# cow_weights = []
# underweight_counter = 0
# healthy_counter = 0
# overweight_counter = 0
# 
# for x in range(1,num_cows+1):
#     cow_weights.append(float(input(f"cow {x} weight in kg: ")))
# 
# for x in cow_weights:
#     if x < 200:
#         underweight_counter += 1
#     elif x > 400:
#         overweight_counter += 1
#     else:
#         healthy_counter += 1
#         
# print(f"Underweight cows: {underweight_counter}, Healthy Cows: {healthy_counter}, Overweight Cows: {overweight_counter}")
# 
# if healthy_counter > 6:
#     print("The overall heard is good")
# else:
#     print("The herd needs attention")