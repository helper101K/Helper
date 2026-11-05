def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # All queens are placed
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            # Backtrack
            board[row][col] = 0

    return False


def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))


if __name__ == "__main__":
    # Input
    n = int(input("Enter value of N: "))
    first_col = int(input(f"Enter column of first Queen (1-{n}): ")) - 1
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Place first Queen
    board[0][first_col] = 1

    # Start backtracking from second row
    if solve_n_queens(board, 1, n):
        print("\nFinal N-Queens Matrix:")
        print_board(board)
    else:
        print("No solution exists for the given first Queen position.")


'''
Enter value of N: 4
Enter column of first Queen (1-4): 1

Final N-Queens Matrix:
Q . . .
. . . Q
. Q . .
. . Q .










## N-Queens Problem Using Backtracking – Theory

### 1. What is the N-Queens Problem?

The N-Queens Problem is a classical problem in computer science in which we have to place N Queens on an N × N chessboard such that no two Queens attack each other.

A Queen can attack another Queen horizontally, vertically, and diagonally.

The objective is to place all N Queens safely on the chessboard.

It is solved using the Backtracking Technique.

In our program, the first Queen is already placed in a user-specified column, and the remaining Queens are placed using backtracking.

### 2. Important Terminology

1\. Backtracking: An algorithmic technique that builds a solution step by step. If a choice leads to an invalid solution, it goes back and tries another choice.

2\. N × N Matrix: A two-dimensional matrix representing the chessboard, where N represents the number of rows and columns.

3\. Queen: A chess piece that can move horizontally, vertically, and diagonally.

4\. Safe Position: A position where a Queen cannot attack any previously placed Queen.

5\. Recursion: A programming technique in which a function calls itself to solve smaller parts of a problem.

6\. Backtracking: Removing a previously placed Queen when no valid position is available and trying another position.

### 3. Conditions for Placing Queens

No two Queens should attack each other.

Three conditions must be satisfied:

1. Row Condition: Only one Queen should be placed in each row.
2. Column Condition: No two Queens should be in the same column.
3. Diagonal Condition: No two Queens should be on the same diagonal.

### 4. How N-Queens Works

The N-Queens problem follows the Backtracking Technique.

1. Input: Accept the value of N and the column position of the first Queen.
2. Create Matrix: Create an N × N chessboard and initialize all positions with 0.
3. Place First Queen: Place the first Queen in the specified column of the first row.
4. Check Safe Position: Check whether the next Queen can be placed safely by checking its column and diagonals.
5. Place Queen: If the position is safe, place the Queen and move to the next row.
6. Backtracking: If no safe position is available, remove the previously placed Queen and try another column.
7. Final Solution: Repeat until all N Queens are placed successfully.

### 5. Example

Consider N = 4.

The chessboard contains 4 rows and 4 columns, and the first Queen is placed in column 1.

Final N-Queens Matrix:

## 4 × 4 Chessboard

# ♛

# ·

# ·

# ·

# ·

# ·

# ·

# ♛

# ·

# ♛

# ·

# ·

# ·

# ·

# ♛

# ·

Each row and column contains exactly one Queen. No two Queens attack each other.

Matrix Representation:

```
1 0 0 0
0 0 0 1
0 1 0 0
0 0 1 0
```

Here:

- `1` represents the position of a Queen.
- `0` represents an empty position.

### 6. Advantages of Backtracking

- Finds valid solutions to constraint-based problems.
- Avoids unnecessary calculations by rejecting unsafe positions.
- Systematically explores possible solutions.
- Useful for puzzles and optimization problems.
- Can find a solution or determine that no solution exists.

### 7. Time and Space Complexity

| Complexity       | Value     |
| ---------------- | --------- |
| Time Complexity  | O(N × N!) |
| Space Complexity | O(N²)     |

Where:

- `N` = Number of Queens.
- `N × N` = Size of the chessboard.

The time complexity represents the upper bound for the row-by-row backtracking implementation.

### 8. Result

The N-Queens problem is successfully solved using the Backtracking Technique by placing the first Queen in the specified column and arranging the remaining Queens so that no two Queens attack each other.

Main concept to remember: Place a Queen only in a safe position. If no safe position is available, backtrack by removing the previously placed Queen and try another position.'''
