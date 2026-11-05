def knapsack(weights, profits, capacity):
    n = len(weights)
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


if __name__ == "__main__":
    # Input
    n = int(input("Enter number of items: "))
    weights = []
    profits = []
    for i in range(n):
        weights.append(int(input(f"Enter weight of item {i + 1}: ")))
        profits.append(int(input(f"Enter profit of item {i + 1}: ")))
    capacity = int(input("Enter knapsack capacity: "))

    # Find maximum profit
    max_profit = knapsack(weights, profits, capacity)
    print("Maximum Profit =", max_profit)


'''Enter number of items: 3
Enter weight of item 1: 10
Enter profit of item 1: 60
Enter weight of item 2: 20
Enter profit of item 2: 100
Enter weight of item 3: 30
Enter profit of item 3: 120
Enter knapsack capacity: 50

Maximum Profit = 220














## 0/1 Knapsack Using Dynamic Programming – Theory

### 1. What is 0/1 Knapsack?

0/1 Knapsack is an optimization problem in which we are given a set of items, each having a weight and profit, and a knapsack with limited capacity.

The objective is to select items in such a way that the total profit is maximized without exceeding the knapsack capacity.

In this problem, each item can either be selected completely (1) or not selected at all (0). Fractional selection is not allowed.

It is commonly solved using Dynamic Programming.

### 2. Important Terminology

1\. Dynamic Programming: An algorithmic technique that solves a complex problem by dividing it into smaller overlapping subproblems and storing their results to avoid repeated calculations.

2\. Knapsack Capacity: The maximum weight that the knapsack can carry.

3\. Weight: The amount of capacity occupied by an item.

4\. Profit: The value or benefit obtained by selecting an item.

5\. Optimal Solution: The solution that provides the maximum possible profit without exceeding the given capacity.

6\. DP Table: A table used to store the maximum profit for different numbers of items and knapsack capacities.

### 3. How 0/1 Knapsack Works

The 0/1 Knapsack problem is solved using Dynamic Programming.

1. Input: Accept the number of items, their weights, profits and knapsack capacity.
2. Create DP Table: Create a table of size `(n+1) × (W+1)` and initialize it with zero.
3. Check Each Item: Compare the weight of each item with the available capacity.
4. Include Item: If the item fits, calculate the profit by including it.
5. Exclude Item: Calculate the profit by not selecting the item.
6. Choose Maximum: Store the maximum profit between the two choices.
7. Final Result: The last cell of the DP table contains the maximum possible profit.

### 4. Mathematical Formula

Let `dp[i][w]` represent the maximum profit using the first `i` items with capacity `w`.

Base Condition:

\\[ dp[0][w] = 0 \\]

\\[ dp[i][0] = 0 \\]

If the item weight is less than or equal to capacity:

\\[ dp[i][w] = \max \begin{cases} profit[i-1] + dp[i-1][w-weight[i-1]]\\\ dp[i-1][w] \end{cases} \\]

If the item weight is greater than capacity:

\\[ dp[i][w] = dp[i-1][w] \\]

### 5. Example

Consider the following items:

| Item   | Weight | Profit |
| ------ | ------ | ------ |
| Item 1 | 10     | 60     |
| Item 2 | 20     | 100    |
| Item 3 | 30     | 120    |

Knapsack Capacity = 50

Step 1: Initially, the knapsack is empty.

Step 2: Check different item combinations:

- Item 1 + Item 2 = Weight 30, Profit 160.
- Item 1 + Item 3 = Weight 40, Profit 180.
- Item 2 + Item 3 = Weight 50, Profit 220.
- All three items = Weight 60, which exceeds capacity.

Step 3: Select Item 2 and Item 3.

Total Weight:

\\[ 20 + 30 = 50 \\]

Total Profit:

\\[ 100 + 120 = 220 \\]

Maximum Profit = 220

### 6. Advantages of 0/1 Knapsack

- Finds the optimal solution using Dynamic Programming.
- Avoids repeated calculations by storing subproblem results.
- Ensures the knapsack capacity is not exceeded.
- Each item is selected completely or rejected.
- Useful in resource allocation and budget optimization problems.

### 7. Time and Space Complexity

| Operation              | Complexity |
| ---------------------- | ---------- |
| Creating DP Table      | O(n × W)   |
| Filling DP Table       | O(n × W)   |
| Finding Maximum Profit | O(1)       |

Overall Time Complexity:

\\[ O(n \times W) \\]

Space Complexity:

\\[ O(n \times W) \\]

Where:

- `n` = Number of items.
- `W` = Knapsack capacity.

### 8. Difference Between 0/1 and Fractional Knapsack

| 0/1 Knapsack                                        | Fractional Knapsack                       |
| --------------------------------------------------- | ----------------------------------------- |
| Uses Dynamic Programming.                           | Uses Greedy Method.                       |
| Items cannot be divided.                            | Items can be divided.                     |
| Select complete item or reject it.                  | Complete or partial item can be selected. |
| Greedy method does not always give optimal results. | Greedy method gives optimal results.      |
| Time complexity: O(n × W).                          | Time complexity: O(n log n).              |

### 9. Result

The 0/1 Knapsack problem is successfully solved using Dynamic Programming by selecting items completely or rejecting them to obtain maximum profit within the given knapsack capacity.

Main concept to remember: For every item, there are only two choices: Include it (1) or Exclude it (0). Dynamic Programming selects the better choice and stores the result to find the maximum profit.'''