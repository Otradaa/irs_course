def Rabin_Karp_matcher(T, P, d, q):
    n = len(T)
    m = len(P)
    h = d ^ (m) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(P[i])) % q
        t = (d * t + ord(T[i])) % q
    for s in range(n - m + 1):
        if p == t and P == T[s:s + m]:
            print("Substring located with shift ", s)
        if s < n - m:
            t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q
