tax_renewal = {"yay": 0, "nay": 0, "idk": 0, "error": 0}
pooh_for_president = {"yay": 12, "nay": 0, "idk": 5, "error": 4}

b = 666


def vote(d_i):
    i = input("vote: ").lower()
    try:
        d_i[i] += 1
    except:
        d_i["error"] += 1


def show_results(d_i):
    for key in d_i:
        print(f"{key}:", "#" * d_i[key])


vote(tax_renewal)
show_results(tax_renewal)
vote(pooh_for_president)
show_results(pooh_for_president)
