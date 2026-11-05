def fractional_knapsack(weights, profits, capacity):

    n = len(weights)
    items = []

    # Calculate profit/weight ratio
    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i]))

    # Sort items by decreasing ratio
    items.sort(reverse=True)

    total_profit = 0

    # Select items greedily
    for ratio, weight, profit in items:

        if capacity >= weight:
            total_profit += profit
            capacity -= weight

        else:
            fraction = capacity / weight
            total_profit += profit * fraction
            break

    return total_profit


# Main Program
n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    w = float(input("Enter weight: "))
    p = float(input("Enter profit: "))

    weights.append(w)
    profits.append(p)

capacity = float(input("Enter knapsack capacity: "))

if n <= 0 or any(w <= 0 for w in weights) or capacity < 0:
    print("Invalid input")
else:
    result = fractional_knapsack(weights, profits, capacity)
    print("Maximum Profit =", result)


'''
Enter number of items: 3

Enter weight of item 1: 10
Enter profit of item 1: 60

Enter weight of item 2: 20
Enter profit of item 2: 100

Enter weight of item 3: 30
Enter profit of item 3: 120

Enter knapsack capacity: 50

Maximum Profit = 240.0
















## Fractional Knapsack – Theory

### 1. What is Fractional Knapsack?

Fractional Knapsack is an optimization problem in which we are given a set of items, each having a weight and profit, and a knapsack with limited capacity.

The objective is to select items in such a way that the total profit is maximized without exceeding the knapsack capacity.

In this method, we can take either the complete item or a fraction of an item.

It uses the Greedy Strategy to obtain the maximum profit.

### 2. Important Terminology

1\. Greedy Algorithm: An algorithm that selects the best possible option at each step to achieve an optimal solution.

2\. Knapsack Capacity: The maximum weight that the knapsack can carry.

3\. Weight: The amount of space or capacity occupied by an item.

4\. Profit: The value or benefit obtained by selecting an item.

5\. Profit-to-Weight Ratio: The ratio of profit to the weight of an item. It helps determine which item should be selected first.

Formula:

\\[ Ratio = \frac{Profit}{Weight} \\]

6\. Fractional Selection: The process of selecting a portion of an item when its complete weight cannot fit into the remaining capacity.

### 3. How Fractional Knapsack Works

The Fractional Knapsack problem follows the Greedy Strategy.

1. Input: Accept the number of items, their weights, profits and knapsack capacity.
2. Calculate Ratio: Calculate the profit-to-weight ratio for each item.
3. Sorting: Sort all items in descending order of their profit-to-weight ratio.
4. Select Items: Select the item having the highest ratio first.
5. Check Capacity: If the complete item fits, take the entire item.
6. Fractional Selection: If the item does not fit, take only the required fraction of it.
7. Calculate Profit: Add the profit of selected items to get the maximum total profit.

### 4. Example

Consider the following items:

| Item   | Weight | Profit | Ratio (Profit/Weight) |
| ------ | ------ | ------ | --------------------- |
| Item 1 | 10     | 60     | 6                     |
| Item 2 | 20     | 100    | 5                     |
| Item 3 | 30     | 120    | 4                     |

Knapsack Capacity = 50

Step 1: Calculate the profit-to-weight ratio of each item.

Step 2: Sort items in descending order of their ratios.

Order: Item 1 → Item 2 → Item 3.

Step 3: Select items according to their ratios.

- Take complete Item 1: Weight = 10, Profit = 60.
- Take complete Item 2: Weight = 20, Profit = 100.
- Remaining capacity = 20.
- Take 20/30 fraction of Item 3.

Step 4: Calculate total profit.

\\[ Maximum\ Profit = 60 + 100 + (120 \times \frac{20}{30}) \\]

\\[ \boxed{Maximum\ Profit = 240} \\]

Maximum Profit = 240

### 5. Advantages of Fractional Knapsack

- Provides maximum profit using a Greedy Strategy.
- Simple and easy to implement.
- Efficient sorting-based approach.
- Allows fractional selection of items.
- Suitable for resource allocation problems.

### 6. Time and Space Complexity

| Operation                     | Time Complexity |
| ----------------------------- | --------------- |
| Calculate Profit/Weight Ratio | O(n)            |
| Sort Items                    | O(n log n)      |
| Select Items                  | O(n)            |

Overall Time Complexity: \\(O(n\log n)\\)

Space Complexity: \\(O(n)\\), including storage of item details.

Where `n` = Number of items.

### 7. Difference Between Fractional and 0/1 Knapsack

| Fractional Knapsack                       | 0/1 Knapsack                                           |
| ----------------------------------------- | ------------------------------------------------------ |
| Uses Greedy Method.                       | Commonly uses Dynamic Programming.                     |
| Items can be divided.                     | Items cannot be divided.                               |
| Complete or partial item can be selected. | Complete item or no item is selected.                  |
| Greedy strategy gives optimal solution.   | Greedy strategy does not always give optimal solution. |

### 8. Result

The Fractional Knapsack problem is successfully solved using the Greedy Method by selecting items according to their profit-to-weight ratios to obtain maximum profit within the given knapsack capacity.

Main concept to remember: Always select the item having the highest profit-to-weight ratio first. Take a fraction of the item when its complete weight cannot fit into the remaining capacity.
'''