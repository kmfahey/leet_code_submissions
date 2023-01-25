#!/usr/bin/python3

# Is visible here:
# https://leetcode.com/problems/valid-sudoku/submissions/885309926/

class Solution:
    # A methodical solution was enough in this case. A private function
    # isValidSudoku() is defined that removes periods from a sequence then tests
    # the new sequence for duplicates, returning True if found.
    #
    # The method tests each row for duplicates, returning False if a row fails,
    # then each column, again returning False if a column fails. Then it uses 4
    # nested for loops to generate coordinate lists for each of the nine squares
    # on the board, and uses those coordinate sequences to extract each square's
    # sequence and test it for duplicates, returning False if a square fails. If
    # control flow makes it to the end of the method, returns True.
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def hasDupl(seq):
            seqSansPer = [elem for elem in seq if elem != "."]
            return not len(seqSansPer) == len(set(seqSansPer))
        if any(hasDupl(row) for row in board):
            return False
        elif any(hasDupl(row[index] for row in board) for index in range(9)):
            return False
        else:
            for outerIndexBase in range(0,9,3):
                for innerIndexBase in range(0,9,3):
                    coordPairs = list()
                    for outerAdtv in range(3):
                        for innerAdtv in range(3):
                            coordPairs.append((outerIndexBase+outerAdtv, innerIndexBase+innerAdtv))
                    if hasDupl(board[x][y] for x, y in coordPairs):
                        return False
        return True

solver = Solution()

print(solver.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                            ["6",".",".","1","9","5",".",".","."],
                            [".","9","8",".",".",".",".","6","."],
                            ["8",".",".",".","6",".",".",".","3"],
                            ["4",".",".","8",".","3",".",".","1"],
                            ["7",".",".",".","2",".",".",".","6"],
                            [".","6",".",".",".",".","2","8","."],
                            [".",".",".","4","1","9",".",".","5"],
                            [".",".",".",".","8",".",".","7","9"]]))
