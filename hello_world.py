
def end_of_world(string="End of World"):
    print(f"Hello {string}")


end_of_world()


# THIS FUCNRION
def avg_monthly_income(list_of_monthly_incomes):
    avg = 0

    for month in list_of_monthly_incomes:
        print('MONTH!', month)
    return avg

list = [
    1200,
    1400,
    561,
    2344
]
avg = avg_monthly_income(list)
print('AVG', avg)
