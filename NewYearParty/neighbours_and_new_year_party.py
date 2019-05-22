import math


class Ticket:
    sum = 0
    numbers = []
    maxLen = 10

    # variable to store states of dp
    dp = [0 for i in range(maxLen)]

    # variable to check if a given state
    # has been solved
    v = [0 for i in range(maxLen)]

    def __init__(self, sum, numbers):
        self.sum = sum
        self.numbers = numbers

    def reverse(self):
        self.numbers.reverse()

    def number(self):
        self.reverse()
        return "".join([str(i) for i in self.numbers])

    # 4 5 4 3 -2 -2 -2 4 5 4 3
    def max_array(self):
        max_include = [0 for s in self.numbers]  # 0
        max_include[0] = self.numbers[0]  # 4
        max_exclude = [0 for s in self.numbers]  # 0
        n_max = self.numbers[0]  # 4
        i = 1
        while i < len(self.numbers):  # 1
            max_include[i] = max(max_exclude[i - 1] + self.numbers[i], self.numbers[i])
            max_exclude[i] = max(max_include[i - 1], max_exclude[i - 1])
            n_max = max(max_include[i], max_exclude[i])
            i += 1
        return n_max

    def sum_for_combination(self, combination):
        sum = 0
        for idx in combination:
            sum += self.numbers[idx]
        return sum


def possibleCombinations(n):
    arr = range(0, n, 1)
    opsize = math.pow(2, n)
    combinations = []
    for counter in range(1, (int)(opsize)):
        print(f"combining...{counter}")
        combination = []
        break_flag = 0
        for j in range(0, n):

            if counter & (1 << j):
                if len(combination) > 1 and combination[-1] + 1 == arr[j]:
                    break_flag = 1
                    break
                elif len(combination) == 1 and combination[0] + 1 == arr[j]:
                    break_flag = 1
                    break
                combination.append(arr[j])

        if not break_flag:
            combinations.append(combination)
    return combinations


def main():
    n_test_cases = int(input())
    i = 0

    while i < n_test_cases:
        n_houses = int(input())
        ticket_list = str(input())
        tickets = [int(j) for j in ticket_list.split()]
        ticket = Ticket(sum(tickets), tickets)
        pc = possibleCombinations(n_houses)
        max_sum = 0
        max_combo = []
        for c in pc:
            print("calculating...")
            n_sum = ticket.sum_for_combination(c)
            if max_sum < n_sum:
                max_sum = n_sum
                max_combo = [c]
            elif max_sum == n_sum:
                max_combo.append(c)
        numbers = []
        for combo in max_combo:
            print("finalizing...")
            number_list = [str(ticket.numbers[k]) for k in combo]
            number_list.reverse()
            numbers.append("".join(number_list))
        print(f"{max(numbers)}")

        i += 1


if __name__ == '__main__':
    main()
