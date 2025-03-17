def calScore(a,b,c,d,e):
    is_safe = 0
    is_at1 = 0
    is_at2 = 0
    if c >= 1:
        is_safe = 2 * c
    if d >= 1:
        is_at1 = 1 * d
    if e >= 1:
        is_at2 = 2 * e
    score = 6 * a + 3*b + is_safe + is_at1 + is_at2
    return score

ft, ff ,fs, fp, fc = map(int, input().split())
st, sf, ss, sp, sc = map(int, input().split())

print(calScore(ft, ff ,fs, fp, fc), calScore(st, sf, ss, sp, sc))