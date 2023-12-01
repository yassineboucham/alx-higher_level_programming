#!/usr/bin/python3
# i = ((i % 10) * 10) + i // 10
for i in range(0, 100):
    if (i == 89):
        print(f"{i}")
        break
    for j in range(0, 100):
        if (i < j and i == ((j % 10) * 10) + j // 10):
            print(f"{i:02d}, ", end='')