n = 5
for i in range(1, n+1):
  if i % 2 != 0:
    for j in range(1, i*2):
      print(j, end=' ')
  else:
    for j in range(ord('A'), ord('A') + i*2-1):
      print(chr(j), end=' ')
  print()
