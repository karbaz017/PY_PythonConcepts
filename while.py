# i = 1
# while i<=5:
#     print("*"*i)
#     i+=1
# print("Done")

# #Guess Game

# secret_number = 9
# i = 0
# while i<3:
#     number = int(input("Guess: "))
#     i+=1
#     if number == secret_number:
#         print("You Win")
#         break
# else:
#     print("Sorry you failed!")


# # Car Game

# text = ""
# started = False
# stopped = True
# while text != "quit":
#     text = input("> ").lower()
#     if text == "help":
#         print("start -  starts the car")
#         print("stop - stops the car")
#         print("quit - exit")
#     elif text == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             stopped = False
#             print("Car Started")
#     elif text == "stop":
#         if stopped:
#             print("Car is already stopped")
#         else:
#             stopped = True
#             started = False
#             print("Car Stopped")
#     elif text == "quit":
#         break
#     else:
#         print("I don't understand that")
