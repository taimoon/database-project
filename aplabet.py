alphabetDict ={}
starting = 10
for i, alphabet in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 10):
    alphabetDict[alphabet] = i % 11
    starting = starting + 1
    if starting%11 == 0:
        starting = starting + 1

expected = {'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38}