
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True,
# }
# print(customer["age"])
# print(customer.get("age"))
# print(customer["birth_date"]) #gives error as birth_date is not in customer
# print(customer.get("birth_date")) #gives None as birth_date is not in customer
# print(customer.get("birth_date","Jan 1 1980")) # if key exist in dictionary then returns it else returns the second argument

# phone = input("Phone: ")
# spell = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
# words = ""
# for item in phone:
#     words += f" {spell[item]}"
# print(words)

message = input(">")
words = message.split(" ")
print(words)