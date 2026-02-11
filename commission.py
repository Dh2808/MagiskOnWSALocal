NO_WIDTH = 3
PERSON_WIDTH = 15
COMMISSION_WIDTH = 7
TIER1_THRESHOLD = 10000
TIER2_THRESHOLD = 20000
TIER1_RATE = 0.05
TIER2_RATE = 0.075
TIER3_RATE = 0.085


def commission(amount):
    """
    Calculate tiered commission from a numeric amount.

    Rates:
    - Up to TIER1_THRESHOLD: TIER1_RATE
    - From TIER1_THRESHOLD to TIER2_THRESHOLD: TIER1_RATE on first tier + TIER2_RATE on the remainder
    - Above TIER2_THRESHOLD: previous tiers + TIER3_RATE on the rest

    Raises:
        ValueError: if amount is not numeric.

    Returns:
        float: commission rounded to 2 decimal places.
    """
    try:
        amt = float(amount)
    except (TypeError, ValueError) as exc:
        raise ValueError("amount must be a numeric value") from exc
    if amt < 0:
        raise ValueError("amount must be non-negative")
    if amt <= TIER1_THRESHOLD:
        total = amt * TIER1_RATE
    elif amt <= TIER2_THRESHOLD:
        total = TIER1_THRESHOLD * TIER1_RATE + (amt - TIER1_THRESHOLD) * TIER2_RATE
    else:
        total = (
            TIER1_THRESHOLD * TIER1_RATE
            + (TIER2_THRESHOLD - TIER1_THRESHOLD) * TIER2_RATE
            + (amt - TIER2_THRESHOLD) * TIER3_RATE
        )
    return round(total, 2)


def apply_commission(old_dict):
    """
    Return a new dictionary with commissions applied to each amount.

    Args:
        old_dict (dict): mapping of people/keys to numeric amounts.

    Returns:
        dict: mapping of the same keys to computed commissions.

    Raises:
        ValueError: if any amount cannot be converted to float.
    """
    return {person: commission(amount) for person, amount in old_dict.items()}


def print_dictionary(commission_dict):
    """
    Print dictionary contents formatted with numbered rows.

    Expects a dictionary mapping person identifiers to numeric commission
    values and outputs rows formatted as:
    |No (width 3)|Person (width 15, truncated if longer)|Commission (min width 7, 2 decimals)|
    Commission values >= 10000.00 will naturally expand beyond 7 characters.
    """
    for idx, (person, comm_value) in enumerate(commission_dict.items(), start=1):
        print(
            f"|{idx:>{NO_WIDTH}}|"
            f"{str(person)[:PERSON_WIDTH]:<{PERSON_WIDTH}}|"
            f"{comm_value:{COMMISSION_WIDTH}.2f}|"
        )
