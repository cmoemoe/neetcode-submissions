#DFS iterate through letters to find first letter 
#from first letter, look at NESW coords for next letter
#if a word is backwards (not left to right) does it count? YES
#only check down and right? And track if curr str == target or target backwards? try later
#keep curr = C - CB, CD, CA - CAA, CAT, CAA (can break early at cat)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, i): #can we match word[i:] starting from (r, c)?
            #don't search up if 1. prev dir was down, 2. row = 0
            #don't search down if 1. prev dir was up, 2. row = len(board)
            #don't search left if 1. prev dir was right, 2. col = 0
            #don't search right if 1. prev dir was left, 2. col = len(board[0])
            #prev dir condition -> temp change to '#'

            if i == len(word):
                return True

            if (r<0 or c<0 or r>=len(board) or c>=len(board[0]) or word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            #just set res as recursive call - will be bool
            board[r][c] = word[i] 
            #restore coord to letter before returning res 
            #the very first call will reach this
            #recall we run a single dfs on every coord in the board, changing it to '#' and reversing it in one run
            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True

        return False

