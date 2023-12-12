def prompt_input(msg, err):
    """
    Prompts the user for an integer using the prompt parameter.
    If an invalid input is given, an error message is shown using
    the error message parameter. A valid input is returned as an
    integer."""

    result = 0
    while not result:
        try:
            result = int(input(msg))
        except:
            print(err)
    return result


number = prompt_input("Give an integer: ", "You did not give an integer")
print(f"You gave the {number} integer! Good job!")
moogles = prompt_input(
    "How many moogles are in the Moogle Village? ",
    "This is not a valid number of moogles!",
)
print(f"There are {moogles} moogles in the village.")
