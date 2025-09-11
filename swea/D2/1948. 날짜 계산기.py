t = int(input())

d = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

prefix = [0] * 13

for i in range(1, 13):
    prefix[i] = prefix[i - 1] + d[i]

for i in range(1, t + 1):
    f_m, f_d, s_m, s_d = map(int, input().split())

    f = prefix[f_m] - (d[f_m] - f_d)
    s = prefix[s_m] - (d[s_m] - s_d)

    print(f"#{i} {s - f + 1}")
