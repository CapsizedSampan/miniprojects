
w = "Wrong! Please try again."

def one_response(input_text):
    user_message = str(input_text.lower())

    if user_message in ("md 6", "md6"):
        return "Correct! Location 1 is MD 6."

    elif user_message == "/start":
        return "Cannot restart lah just answer my qn!!"

    else:
        return w

def two_response(input_text):
    user_message = str(input_text.lower())
    user_message.split()
    #print(user_message)

    if user_message in ("finefood @ utown", "finefood") :
        return "Correct! Location 2 is Finefood@Utown. "

    else:
        return w

def three_response(input_text):
    user_message = str(input_text.lower())
    #user_message.split()
    #print(user_message)

    if user_message in ("pgp", "prince george park", "nus pgp", "prince george's park residences") :
        return "Correct! Location 3 is PGP."

    else:
        return w


    return
def four_response(input_text):
    user_message = str(input_text.lower())
    #user_message.split()
    #print(user_message)
    user_message = user_message.replace(" ","")
    print (user_message)
    if user_message == "sde2er1" :
        return "Correct! Location 4 is SDE2 ER1. And that's the location for Station 3!"

    else:
        return w
