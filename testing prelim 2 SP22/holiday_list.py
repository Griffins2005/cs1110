def num_holidays(holiday_list):
    """Returns the number of days off, given a non-empty list of holidays, holiday_list
       that has no duplicate holidays and no overlapping holidays

    A holiday is a list of 2-3 items:
        * a non-empty string, the name of the holiday
        * a start date
        * an optional end date (if the holiday lasts longer than 1 day).
          This is the last day the holiday is celebrated.
    A date is a list with 2 items:
        * a non-empty string, the month
        * an int, the day of the month (assume valid number for the month)

    You may assume that all holidays start and end in the same month.

    Examples:
        SU22 = [["Juneteenth",  ["Jun", 20]]]                # 1 day holiday
        num_holidays(SU22) --> returns 1

        FA21 = [["Labor Day",  ["Sep", 6]],                  # 1 day holiday
                ["Fall Break", ["Oct", 9], ["Oct", 12]],     # 4 day holiday
                ["Thanksgiving", ["Nov", 24], ["Nov", 28]]]   # 5 day holiday
        num_holidays(FA21) --> returns 10
    """


if __name__ == '__main__':
    SP22 = []
    SU22 = [["Juneteenth",  ["Jun", 20]]]
    FA21 = [["Labor Day",  ["Sep", 6]],
            ["Fall Break", ["Oct", 9], ["Oct", 12]],
            ["Thanksgiving", ["Nov", 24], ["Nov", 28]]
            ]

    testcases = [[SP22, 0],
                 [SU22, 1],
                 [FA21, 10]
                 ]

    for item in testcases:
        holiday_list = item[0]
        expected = item[1]

        result = num_holidays(holiday_list)
        assert result == expected, \
        "Bad result on list starting with " + holiday_list[0][0] + ": " + str(result)
    print("Tests ran without crashing")

