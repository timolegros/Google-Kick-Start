T = int(input())
case = 0
while T > 0:
    N, B = map(int, input().split())
    A = list(map(int, input().split()))

    # O(N log N)
    # could have used count sort to reduce time complexity but would lose valuable time coding it
    A.sort()

    counter = 0

    # O(N)
    for price in A:
        if price <= B:
            B -= price
            counter += 1

    case += 1
    print('Case #{}: {}'.format(case, counter))
    T -= 1

