def commission(amount):
    """Calculate tiered commission from a numeric amount."""
    amt = float(amount)
    if amt <= 10000:
        total = amt * 0.05
    elif amt <= 20000:
        total = 10000 * 0.05 + (amt - 10000) * 0.075
    else:
        total = 10000 * 0.05 + 10000 * 0.075 + (amt - 20000) * 0.085
    return round(total, 2)


def apply_commission(old_dict):
    """Return a new dictionary with commissions applied to each amount."""
    return {person: commission(amount) for person, amount in old_dict.items()}


def print_dictionary(dict_):
    """Print dictionary contents formatted with numbered rows."""
    for idx, (person, comm_value) in enumerate(dict_.items(), start=1):
        print(f"|{idx:>3}|{str(person)[:15]:<15}|{comm_value:6.2f}|")
