def commission(amount):
    """
    Calculate the commission for a sales department based on the sales amount.
    
    Commission structure:
    - Up to 10000 Euro: 5% commission
    - 10000 to 20000 Euro: 5% on first 10000 + 7.5% on amount exceeding 10000
    - Over 20000 Euro: 5% on first 10000 + 7.5% on next 10000 + 8.5% on amount exceeding 20000
    
    Args:
        amount: The sales figure in Euro
        
    Returns:
        The calculated commission amount
    """
    commission_total = 0
    
    if amount <= 10000:
        commission_total = amount * 0.05
    elif amount <= 20000:
        commission_total = 10000 * 0.05 + (amount - 10000) * 0.075
    else:
        commission_total = 10000 * 0.05 + 10000 * 0.075 + (amount - 20000) * 0.085
    
    return commission_total


def apply_commission(old_dict):
    """
    Process a dictionary of Person:Amount pairs and create a new dictionary with Person:Commission pairs.
    
    Args:
        old_dict: Dictionary with Person:Amount pairs
        
    Returns:
        New dictionary with Person:Commission pairs
    """
    new_dict = {}
    
    for person, amount in old_dict.items():
        new_dict[person] = commission(amount)
    
    return new_dict


def print_dictionary(dict):
    """
    Print a dictionary with formatted columns.
    
    Format:
    | No (3 characters) | Person (15 characters) | Commission (7 positions, 2 decimal digits) |
    
    Args:
        dict: Dictionary with Person:Commission pairs
    """
    # Print header
    print("| No  | Person          | Commission |")
    print("|-----|-----------------|------------|")
    
    # Print each entry
    counter = 1
    for person in dict.keys():
        commission_value = dict[person]
        print(f"| {counter:3d} | {person:15s} | {commission_value:7.2f} |")
        counter += 1
