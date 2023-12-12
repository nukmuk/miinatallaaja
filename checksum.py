def check_bust(hand_total):
    if hand_total > 21:
        return True
    else:
        return False

total = int(input("Enter hand total: "))
if check_bust(total):
    print("You lost")
else:
    print("You didn't lose, at least not yet...")
