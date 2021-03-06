from searches.naive_string_matcher import naive_string_matcher
from searches.Rabin_Karp_matcher import Rabin_Karp_matcher
from searches.finite_automaton_matcher import finite_automaton_matcher
from searches.KMP_matcher import KMP_matcher
from searches.Boyer_Moore_matcher import Boyer_Moore_matcher

if __name__ == "__main__":
    T = "Today is a good day"
    P = "day"
    print("naive string matcher:")
    naive_string_matcher(T, P)

    d = 10;
    q = 13;
    print(f"\nRabin-Karp matcher (q={q}):")
    Rabin_Karp_matcher(T, P, d, q)

    print("\nfinite automatom matcher:")
    finite_automaton_matcher(T, P)

    print("\nKMP matcher:")
    KMP_matcher(T, P)

    print("\nBoyer Moore matcher:")
    Boyer_Moore_matcher(T, P)
