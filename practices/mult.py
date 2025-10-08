#Du p2 Multiplaiction Chart


def mult_chart():
    for intercontinentalmissile in range(1, 13):
        for laxitave in range(1, 13):
            print(f"{intercontinentalmissile * laxitave:4}", end="")
        print()
mult_chart()
