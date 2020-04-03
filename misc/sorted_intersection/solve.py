# find an intersection of two sorted int arrays

f = open("input.txt")
inp = f.read().split("\n")
first = list(map(int, inp[1].split()))
second = list(map(int, inp[3].split()))
fi = 0
si = 0
result = []
while fi < len(first) and si < len(second):
  f = first[fi]
  s = second[si]
  if f == s:
    result.append(f)
    fi += 1
  elif f < s:
    fi += 1
  elif f > s:
    si += 1
print(result)