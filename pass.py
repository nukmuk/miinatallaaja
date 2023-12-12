def prompt_password():
    """asd"""
    result = ""
    while len(result) < 8:
        result = input()
    return result


print(prompt_password())
