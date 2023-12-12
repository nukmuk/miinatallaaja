def show_results(file):
    with open(file) as target:
        for row in target.readlines():
            content = row.strip().split(",")
            print(content)
            print(f"{content[0]} {content[2]} - {content[3]} {content[1]}")


show_results("hemulencup.csv")
