number_of_massage = int(input())

for message in range(number_of_massage):
    current_massage = int(input())
    mess = ""
    if current_massage == 88:
        mess = "Hello"
    elif current_massage == 86:
        mess = "How are you?"
    elif current_massage < 88:
        mess = "GREAT!"
    elif current_massage > 88:
        mess = "Bye."

    print(mess)