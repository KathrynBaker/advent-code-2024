from sys import argv
from functools import cache

@cache
def count_stones(number: str, depth: int) -> int:
    if depth==0: return 1
    if number=="0" or number=="": return count_stones("1", depth-1)
    if len(number)%2: return count_stones(str(int(number)*2024), depth-1)
    l = len(number)//2
    return count_stones(number[:l], depth-1)+count_stones(number[l:].lstrip("0"), depth-1)


#with open(argv[1], "r") as f: l = f.readline()
l = "3935565 31753 437818 7697 5 38 0 123"

print(sum(count_stones(s, 25) for s in l.split()))
print(sum(count_stones(s, 75) for s in l.split()))