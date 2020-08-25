#!/usr/bin/env python3

#사각형 만들기
def form_square(n):
    arr = []
    for r in range(n+2):
        row = []
        for c in range(n+2):
            row.append(0)
        arr.append(row)

    return arr

#테두리 -1로 채우기
def init_square(sq):
    n = len(sq) - 2
    for r in range(n+2):
        for c in range(n+2):
            if (r == 0 or r == n+1) or (c == 0 or c == n+1):
                sq[r][c] = -1
    
    return sq


#숫자 채우기
def build_square(init_sq):
    n = len(init_sq) - 2
    x == 1, y == 1
    for num in range(1, n*n + 1):
        if init_sq[y-1][x] != 0 and init_sq[y][x+1] == 0:
            init_sq[y][x] = num
            x += 1
        if init_sq[y][x+1] != 0 and init_sq[y+1][x] == 0:
            init_sq[y][x] = num
            y += 1
        if init_sq[y][x+1] != 0 and init_sq[y][x-1] == 0:
            init_sq[y][x] = num
            x -= 1
        else:
            init_sq[y][x] = num
            y -= 1

    return init_sq

#줄 바꿔서 출력
def print_square(sp_sq):
    n = len(sp_sq) - 2
    for r in range(1, n+1):
        for c in range(1, n+1):
            print(sp_sq[r][c], end = "\t")
        print()

#
def main(n):
    form_square(n)
    init_square(sq)
    build_square(init_sq)
    print_square(sp_sq)

#
n = 5
sq = form_square(n)
init_sq = init_square(sq)
sp_sq = build_square(init_sq)

main(n)
