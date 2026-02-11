#!/usr/bin/env python3
"""
Example usage of commission calculation functions.
"""

from commission import commission, apply_commission, print_dictionary


def main():
    """Demonstrate the commission calculation functions."""
    
    print("Commission Calculator Demo")
    print("=" * 60)
    
    # Demo 1: Calculate individual commissions
    print("\n1. Individual Commission Calculations:")
    print("-" * 60)
    
    amounts = [5000, 10000, 15000, 20000, 25000, 30000]
    for amount in amounts:
        comm = commission(amount)
        print(f"Sales: €{amount:8.2f}  ->  Commission: €{comm:8.2f}")
    
    # Demo 2: Process a sales team dictionary
    print("\n\n2. Sales Team Commission Report:")
    print("-" * 60)
    
    sales_team = {
        "John Smith": 8500,
        "Alice Johnson": 12300,
        "Bob Williams": 22500,
        "Carol Davis": 18900,
        "David Brown": 31200
    }
    
    print("\nOriginal Sales Data:")
    for person, amount in sales_team.items():
        print(f"{person:20s}: €{amount:8.2f}")
    
    # Apply commission calculation
    commissions = apply_commission(sales_team)
    
    print("\n\nCommission Report:")
    print_dictionary(commissions)
    
    # Calculate totals
    total_sales = sum(sales_team.values())
    total_commission = sum(commissions.values())
    commission_rate = (total_commission / total_sales) * 100
    
    print("\n" + "-" * 60)
    print(f"Total Sales:      €{total_sales:10.2f}")
    print(f"Total Commission: €{total_commission:10.2f}")
    print(f"Average Rate:     {commission_rate:10.2f}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
