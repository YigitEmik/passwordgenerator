import random
from loading import loading
file = open("/Users/Yigit Emik/Desktop/sifreler.txt", "a")

chars = "abcdefghijkLMONPRSTUVYZQ1234567890!@#$%^&*()_-+[]}{;/,.?"

def passwordgenerator():
    while True:
        password_len = int(input("What length would you like your password to be: "))
        print("Creating 5 different passwords for you")
        loading("Creating")
        for x in range(0, 5):
            password = ""
            for x in range(0, password_len):
                password_char = random.choice(chars)
                password = password + password_char
            print("Here is your password: ", password)
        break


def mainpass():

    passwordgenerator()
    while True:
        answer = input("Would you like to generate again ?\nYes(Y) or No(N): ")
        if answer == "y".lower():
            passwordgenerator()
        elif answer == "n".lower():
            chosen_pass = input("Please enter the password you choose (copy/paste): ")
            purpose = input("What are you going to use the password for: ")
            name = input("What is the user name you are going to use with this password: ")
            file.write("\n")
            file.write(purpose)
            file.write("\n")
            file.write("-------------------------")
            file.write("\n")
            file.write("User name: ")
            file.write(name)
            file.write("\n")
            file.write("Password: ")
            file.write(chosen_pass)
            file.write("\n")
            file.write("-------------------------")
            loading("Saving")
            print("Saved Successfully.")
            file.close()
            exit()
        else:
            print("Invalid Input")



mainpass()





