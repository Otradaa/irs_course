def compute_transition_function(P):
    delta = {}
    m = len(P)
    for q in range(m):
        for a in range(256):
            k = min(m, q+1)
            while P[:k] not in P[:q]+chr(a):
                k=k-1
            delta[(q,chr(a))] = k #должен быть от 0 до m-1
    return delta


def finite_automaton_matcher(T, P):
    delta = compute_transition_function(P)
    m = len(P)
    n = len(T)
    q = 0
    for i in range(n):
        q = delta[(q, T[i])]
        if q == m:
            q = 0
            s = i-m+1
            print("Substring located with shift ", s)