#!/usr/bin/env python3
"""
Test file for commission calculation functions.
"""

import sys
from commission import commission, apply_commission, print_dictionary


def test_commission():
    """Test commission calculation with various amounts."""
    print("Testing commission() function...")
    
    # Test case 1: Amount up to 10000 (5% commission)
    assert commission(5000) == 250.0, "Failed for amount 5000"
    assert commission(10000) == 500.0, "Failed for amount 10000"
    
    # Test case 2: Amount between 10000 and 20000
    # 10000 * 0.05 + (15000 - 10000) * 0.075 = 500 + 375 = 875
    assert commission(15000) == 875.0, "Failed for amount 15000"
    assert commission(20000) == 1250.0, "Failed for amount 20000"  # 500 + 750
    
    # Test case 3: Amount over 20000
    # 10000 * 0.05 + 10000 * 0.075 + (25000 - 20000) * 0.085 = 500 + 750 + 425 = 1675
    assert commission(25000) == 1675.0, "Failed for amount 25000"
    assert commission(30000) == 2100.0, "Failed for amount 30000"  # 500 + 750 + 850
    
    print("✓ All commission() tests passed!")


def test_apply_commission():
    """Test apply_commission function."""
    print("\nTesting apply_commission() function...")
    
    # Test data
    sales_data = {
        "John": 5000,
        "Alice": 15000,
        "Bob": 25000
    }
    
    expected_result = {
        "John": 250.0,
        "Alice": 875.0,
        "Bob": 1675.0
    }
    
    result = apply_commission(sales_data)
    
    for person in sales_data.keys():
        assert person in result, f"Person {person} not in result"
        assert result[person] == expected_result[person], \
            f"Commission mismatch for {person}: expected {expected_result[person]}, got {result[person]}"
    
    print("✓ All apply_commission() tests passed!")


def test_print_dictionary():
    """Test print_dictionary function."""
    print("\nTesting print_dictionary() function...")
    
    commission_data = {
        "John": 250.0,
        "Alice": 875.0,
        "Bob": 1675.0
    }
    
    print("\nExpected output format:")
    print_dictionary(commission_data)
    print("✓ print_dictionary() executed successfully!")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Running Commission Calculation Tests")
    print("=" * 60)
    
    try:
        test_commission()
        test_apply_commission()
        test_print_dictionary()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
