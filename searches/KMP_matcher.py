def KMP_matcher(T,P):
    n = len(T)
    m = len(P)
    pi = compute_prefix(P)
    q = 0
    for i in range(n):
        while q>0 and P[q] != T[i]:
            q = pi[q]
        if P[q] == T[i]:
            q = q + 1
        if q==m:
            print("Substring located with shift ", i-m+1)
            q = pi[q-1]


def compute_prefix(P):
    m = len(P)
    pi = []
    pi.append(0)
    k = 0
    for q in range(1, m):
        k = pi[q-1]
        while k>0 and P[k] != P[q]:
            k = pi[k-1]
        if P[k]==P[q]:
            k = k + 1
        pi.append(k)
    return pi
