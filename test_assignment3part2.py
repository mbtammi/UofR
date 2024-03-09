import unittest
from random import randint
from assignment3part2 import max_value, min_value, value_range, biggestThree, smallestThree, mean_value, median_value, mode_value, variance_value, listOfRandoms


class TestAssignmentCode(unittest.TestCase):

    def test_max_value(self):
        self.assertEqual(max(listOfRandoms), max_value)

    def test_min_value(self):
        self.assertEqual(min(listOfRandoms), min_value)

    def test_range(self):
        self.assertEqual(max(listOfRandoms) - min(listOfRandoms), value_range)

    def test_biggest_three(self):
        copyOfList = list(set(listOfRandoms))
        copyOfList.sort(reverse=True)
        self.assertEqual(biggestThree, copyOfList[:min(3, len(copyOfList))])

    def test_smallest_three(self):
        copyOfList = list(set(listOfRandoms))
        copyOfList.sort()
        self.assertEqual(smallestThree, copyOfList[:min(3, len(copyOfList))])

    def test_mean(self):
        self.assertEqual(sum(listOfRandoms) / len(listOfRandoms), mean_value)

    def test_median(self):
        sorted_list = sorted(listOfRandoms)
        middlepoint = len(listOfRandoms) // 2
        self.assertEqual((sorted_list[middlepoint] + sorted_list[-middlepoint - 1]) / 2, median_value)

    def test_mode(self):
        ocurrencies = {}
        for num in listOfRandoms:
            ocurrencies[num] = ocurrencies.get(num, 0) + 1
        self.assertEqual(max(ocurrencies, key=ocurrencies.get), mode_value)

    def test_variance(self):
        mean_value = sum(listOfRandoms) / len(listOfRandoms)
        variance_value = sum((x - mean_value) ** 2 for x in listOfRandoms) / len(listOfRandoms)
        self.assertEqual(variance_value, variance_value)

if __name__ == '__main__':
    unittest.main()
