# Compute p(k) for all k
# memo = {};
# W(k):
# if k in memo: return memo[k]
# if k == 0:
# x = 0
# else:
# x = max{W(k-1), w(k) + W(p(k))}
# memo[k] = x
# return x

import random

memo = {}
# compute irgednwaas

def paper_submission(k, d):
    if k in memo:
        return memo[k]
    if k == 0:
        x = 0
    else:
        x = max(paper_submission(k-1,d), 1+ paper_submission(p(k), d-t))


def generate_P(n):
    P = []
    for i in range(n):
        t =  random.randint(1, 20)
        d =  random.randint(1, 20)
        if t <= d:
            P.append([t,d])
    return P

if __name__ == "__main__":
    print(generate_P(10))

