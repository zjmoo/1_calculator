#! /usr/bin/env python3
from collections import namedtuple


Tax_Lookup_Item = namedtuple("Tax_Lookup_Item", ["income", "taxRate", "subNum"])


TAX_RATE_LOOKUP_TABLE = [
    Tax_Lookup_Item(80000, 0.45, 13505),
    Tax_Lookup_Item(55000, 0.35, 5505),
    Tax_Lookup_Item(35000, 0.30, 2755),
    Tax_Lookup_Item(9000,  0.25, 1005),
    Tax_Lookup_Item(4500,  0.20, 555),
    Tax_Lookup_Item(1500,  0.10, 105),
    Tax_Lookup_Item(0,     0.03, 0),
]

TAX_START_POINT = 3500


def main():
    import sys
    try:
        if len(sys.argv) != 2:
            raise ValueError()
        income = int(sys.argv[1])
        income_for_tax = income - 3500
        for item in TAX_RATE_LOOKUP_TABLE:
            if income_for_tax >= item.income:
                tax = income_for_tax * item.taxRate - item.subNum
                print(format(tax, ".2f"))
                break
    except (IndexError, ValueError):
        print("Parameter Error!")


if __name__ == "__main__":
    main()
