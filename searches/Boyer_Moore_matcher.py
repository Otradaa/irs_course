from .KMP_matcher import compute_prefix


def Boyer_Moore_matcher(T, P):
    n = len(T)
    m = len(P)
    lambd = compute_last_occurence(P, m)
    gamma = compute_good_suffix(P, m)
    s = 0
    while s <= n - m:
        j = m - 1
        while j > 0 and P[j] == T[s + j]:
            j = j - 1
        if j == 0:
            print("Substring located with shift ", s)
            s = s + gamma[0]
        else:
            s = s + max(gamma[j], j - lambd[ord(T[s + j])])


def compute_last_occurence(P, m):
    lambd = [0] * 256
    for j in range(m):
        lambd[ord(P[j])] = j
    return lambd


def compute_good_suffix(P, m):
    gamma = [0] * (m + 1)
    pi = compute_prefix(P)
    pi_inv = compute_prefix(P[::-1])
    for j in range(m + 1):
        gamma[j] = m - pi[m - 1] - 1
    for l in range(m):
        j = m - pi_inv[l] - 1
        if gamma[j] > l - pi_inv[l]:
            gamma[j] = l - pi_inv[l]
    return gamma
