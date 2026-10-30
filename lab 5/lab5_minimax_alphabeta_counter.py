
import math
scores = [3, 5, 2, 9, 0, 7]
treeDepth = math.ceil(math.log2(len(scores)))
scores += [0] * (2**treeDepth - len(scores))
count = 0
def minimax(currentDepth, nodeIndex, isMaxTurn):
    global count
    if currentDepth == treeDepth:
        count += 1
        return scores[nodeIndex]
    if isMaxTurn:
        return max(
            minimax(currentDepth + 1, nodeIndex * 2, False),
            minimax(currentDepth + 1, nodeIndex * 2 + 1, False)
        )
    else:
        return min(
            minimax(currentDepth + 1, nodeIndex * 2, True),
            minimax(currentDepth + 1, nodeIndex * 2 + 1, True)
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

