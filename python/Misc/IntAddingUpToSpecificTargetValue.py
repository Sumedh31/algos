# def find_two_numbers(lst, target):
#     diff_dict = {}  # Dictionary to store the difference between target and each element of the list
#     targets =[]
#
#     for i, num in enumerate(lst):
#         if num in diff_dict:  # If the element exists in the dictionary, return the corresponding pair
#             targets.append([lst[diff_dict[num]], num])
#         else:  # Otherwise, add the difference to the dictionary
#             diff_dict[target - num] = i
#
#     return targets  # If no such pair exists, return an empty list
#
#
# # Test the function
# lst = [3, 7, 1, 2, 8, 4, 5]
# target = 10
# print(find_two_numbers(lst, target))  #

# def find_two_numbers(lst,target):
#     numbers = []
#     already_included = {}
#     for i,num in enumerate(lst):
#         for j in range(len(lst)):
#             if not j == i:
#                 if (num+lst[j]) == 10 and (num and lst[j] not in already_included.keys()):
#                     numbers.append([num, lst[j]])
#                     already_included[num], already_included[lst[j]] = num, lst[j]
#     return numbers
#
def find_two_numbers(lst, target):
    pairs = {}
    final_numbers = []
    for i, num in enumerate(lst):
        if num not in pairs.keys():
            pairs[target-num] = i
        else:
            final_numbers.append([num, lst[pairs[num]]])

    return final_numbers

lst = [3, 7, 1, 2, 8, 4, 5]
target = 10
print(find_two_numbers(lst, target))




