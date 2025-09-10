# boj 20422 퀼린드롬
import sys
input = sys.stdin.readline

mirror = {
    'A':'A','E':'3','3':'E','H':'H','I':'I','M':'M','O':'O','S':'2','2':'S',
    'T':'T','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z':'5','5':'Z',
    'b':'d','d':'b','i':'i','l':'l','m':'m','n':'n','o':'o','p':'q','q':'p',
    'r':'7','7':'r','u':'u','v':'v','w':'w','x':'x','0':'0','1':'1','8':'8'
}

def _cands(ch):
    return (ch, ch.swapcase()) if ch.isalpha() else (ch,)

def solution():
    s = input().strip()
    n = len(s)
    ans = [''] * n

    for i in range((n + 1) // 2):
        j = n - 1 - i
        ok = False
        for c1 in _cands(s[i]):
            if c1 in mirror:
                m = mirror[c1]
                for c2 in _cands(s[j]):
                    if c2 == m:
                        ans[i], ans[j] = c1, m
                        ok = True
                        break
            if ok:
                break
        if not ok:
            print(-1)
            return
    print(''.join(ans))

if __name__ == "__main__":
    solution()