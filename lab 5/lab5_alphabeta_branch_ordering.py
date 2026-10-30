
import math
scores = [0, 7, 3, 5, 0, 0, 2, 9]
treeDepth = int(math.log2(len(scores)))
count = 0
def minimax(depth, index, maxTurn):
    global count
    if depth == treeDepth:
        count += 1
        return scores[index]
    if maxTurn:
        return max(
            minimax(depth + 1, index * 2, False),
            minimax(depth + 1, index * 2 + 1, False)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True),
            minimax(depth + 1, index * 2 + 1, True)
        )
result = minimax(0, 0, True)
print("Minimax Value:", result)
print("Minimax Leaf Evaluations:", count)
count = 0
def alpha_beta(depth, index, maxTurn, alpha, beta):
    global count
    if depth == treeDepth:
        count += 1
        return scores[index]
    if maxTurn:
        value = float("-inf")
        for i in range(2):
            value = max(value, alpha_beta(
                depth + 1, index * 2 + i, False, alpha, beta
            ))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for i in range(2):
            value = min(value, alpha_beta(
                depth + 1, index * 2 + i, True, alpha, beta
            ))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
result = alpha_beta(0, 0, True, float("-inf"), float("inf"))
print("Alpha-Beta Value:", result)
print("Alpha-Beta Leaf Evaluations:", count)
