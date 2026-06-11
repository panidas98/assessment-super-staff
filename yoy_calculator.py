def calculate_yoy_change(spending_data):
    # sort the years so we always go in chronological order
    sorted_years = sorted(spending_data.keys())
    changes = {}

    # start at index 1 — the first year has nothing before it to compare against
    for i in range(1, len(sorted_years)):
        current_year = sorted_years[i]
        previous_year = sorted_years[i - 1]

        current_spending = spending_data[current_year]
        previous_spending = spending_data[previous_year]

        # can't divide by zero, so if the previous year had no spending just mark it as None
        if previous_spending == 0:
            changes[current_year] = None
        else:
            # using abs() on the denominator so that a negative base year
            # doesn't flip the direction of the percentage — e.g. going from -100 to 1600
            # should be a positive 1700% change, not negative
            change = (current_spending - previous_spending) / abs(previous_spending) * 100
            changes[current_year] = change

    return changes


import unittest

class TestCalculateYoYChange(unittest.TestCase):

    def test_yoy_positive_increase(self):
        spending_data = {2020: 1000, 2021: 1200, 2022: 1300, 2023: 1600}
        expected = {2021: 20.0, 2022: 8.333333333333332, 2023: 23.076923076923077}
        self.assertEqual(calculate_yoy_change(spending_data), expected)

    def test_yoy_with_zero_previous(self):
        spending_data = {2020: 0, 2021: 500}
        expected = {2021: None}
        self.assertEqual(calculate_yoy_change(spending_data), expected)

    def test_yoy_negative_spending(self):
        spending_data = {2020: 1000, 2021: 1200, 2022: -100, 2023: 1600}
        expected = {
            2021: 20.0,
            2022: -108.33333333333333,
            2023: 1700.0
        }
        self.assertEqual(calculate_yoy_change(spending_data), expected)


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.makeSuite(TestCalculateYoYChange))
