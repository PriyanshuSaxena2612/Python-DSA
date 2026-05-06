class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])
        for r in range(rows):
            i = cols - 1
            for c in reversed(range(cols)):
                if boxGrid[r][c] == '#':
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    i -= 1
                elif boxGrid[r][c] == '*':
                    i = c - 1
        boxGrid = [list(row) for row in zip(*boxGrid[::-1])]
        return boxGrid
