import random

# minimizes set S of intervalls, that covers X with (a, a+1)
def A(X: list):
    S = []
    # sort X in ascending order
    X = sorted(X)
    # while X is not empty
    while X:
        a = 0
        highest_cover = 0

        for i in X:
            # sum the coverage from intervall (a, a+1) of elements in X and replace intervall with better intervall
            cover_count = sum(1 for x in X if i <= x <= i + 1)
            if highest_cover < cover_count:
                highest_cover = cover_count
                a = i

        # add intervall to set S and remove covered elements from X
        S.append([a,a+1])
        X = [x for x in X if not (a <= x <= a + 1)]
    return S

# Hauptprogramm
if __name__ == "__main__":
    X = [0.5,1.0,1.5,2.0,2.5,3.0]
    i = 0
    random.shuffle(X)
    print(f"gemixtes X: {X}")
    S = A(X)
    print(f"fertiges S: {S}")
