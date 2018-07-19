#！/usr/bin/env python3
from collections import namedtuple

Insurance_Table_Dic = {
    "YangLao"   : 0.08,
    "YiLiao"    : 0.02,
    "ShiYe"     : 0.005,
    "GongShang" : 0,
    "ShengYu"   : 0,
    "GongJiJin" : 0.06
}

Tax_Lookup_Item = namedtuple("Tax_Lookup_Item", ["income_level", "tax_rate", "sub_num"])


TAX_LOOKUP_TABLE = [
    Tax_Lookup_Item(80000, 0.45, 13505),
    Tax_Lookup_Item(55000, 0.35, 5505),
    Tax_Lookup_Item(35000, 0.30, 2755),
    Tax_Lookup_Item(9000 , 0.25, 1005),
    Tax_Lookup_Item(4500 , 0.20, 555),
    Tax_Lookup_Item(1500 , 0.10, 105),
    Tax_Lookup_Item(0    , 0.03, 0)
]


INCOME_START_POINT = 3500


def calc_income_after_tax(income_before_tax):
    income_for_tax = income_before_tax - income_before_tax * sum(Insurance_Table_Dic.values()) - INCOME_START_POINT
    if income_for_tax < 0:
        income_for_tax = 0
    for item in TAX_LOOKUP_TABLE:
        if income_for_tax >= item.income_level:
            tax = income_for_tax * item.tax_rate - item.sub_num
            income_after_tax = income_before_tax - income_before_tax * sum(Insurance_Table_Dic.values()) - tax
            return income_after_tax


def main():
    import sys
    for employ_item in sys.argv[1: ]:
        employ_income_after_tax = calc_income_after_tax(int(employ_item.strip().split(":")[1]))
        print(employ_item.strip().split(":")[0] + ":" + str(employ_income_after_tax))

if __name__ == "__main__":
    main()