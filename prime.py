def prompt_input(msg, err):
    """
    Prompts the user for an integer using the prompt parameter.
    If an invalid input is given, an error message is shown using
    the error message parameter. A valid input is returned as an
    integer."""

    result = False
    while not result:
        try:
            result = int(input(msg))
        except:
            print(err)
        if result < 2:
            result = False
            # print(err)
    return result


def check_prime(n):
    """Checks whether an integer is a prime number. Returns False
    if the number isn't a prime; if it is a prime, returns True"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


prime = check_prime(
    prompt_input("Give an integer that's bigger than 1: ", "You had one job")
)
if prime:
    print("This is a prime")
else:
    print("This is not a prime")
