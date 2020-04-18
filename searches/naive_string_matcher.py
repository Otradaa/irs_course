def naive_string_matcher(T:str, P:str):
    n = len(T) # aadfgsgsg 9
    m = len(P) # aa 2
    for s in range(n-m+1):
        if P == T[s:s+m]:
            print("Substring located with shift ", s)
