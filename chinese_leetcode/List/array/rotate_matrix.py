def rotate(m):
    # i = j = 2
    # (0,0) = (2,0)/ (0,1) = (1,0),/ (0,2) = (0,0) => (n-j,i)

    n = len(m)
    new_m = [[None]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_m[i][j] = m[n-j-1][i]
            # pass

    return new_m


print(rotate([[1,2,3],[4,5,6],[7,8,9]]))



