from typing import Dict, List, NamedTuple

# See a more freiendly implementation explations:
# https://youkre.github.io/engineering-wisdom/2026-03-29/

lenght_to_price = [
    0,
    1,
    5,
    8,
    9,
    10,
    17,
    17,
    20,
    24,
    30
]


# Topd-down recursive implementation.
def cut_rod(prices: List[int], n: int):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, prices[i] + cut_rod(prices, n - i))
    return q

# Top-down  with memorization.
def memoized_cut_rod_aux(prices: List[int], n: int, revenue: Dict[int, float]):
    if n in revenue:
        print(f"  Reuse max reveue for {n} cut: {revenue[n]}")
        return revenue[n]
    
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, prices[i] + memoized_cut_rod_aux(prices, n-i, revenue))

    revenue[n] = q
    print(f"Save max reveue for {n} cut: {q}")
    return q

def memoized_cut_rod(prices: List[int], n: int):
    revenues: Dict[int, float] = {} # n to price
    print("Init max revenues...")
    return memoized_cut_rod_aux(prices, n, revenues)

# Bottom-up method
def buttom_up_cur_rod(prices: List[int], n: int):
    revenues: Dict[int, float] = {
        0: 0
    }
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            q = max(q, prices[i] + revenues[j-i])
        revenues[j] = q

    return revenues[n]

# Bottom-up method with solution
class OptimalRod(NamedTuple):
    """
    For a rod of length j, the best first cut length,
    and optimal total revenue.
    """
    best_first_cut: int
    total_revenue: float

def extended_bottom_cut_rod(prices: List[int], n: int):
    revenues: Dict[int, float] = {
        0: 0
    }
    solution: Dict[int, int] = {
        0: 0
    }

    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            if q < prices[i] + revenues[j-i]:
                q = prices[i] + revenues[j-i]
                # For a rod of length j, the best first cut position i.
                solution[j] = i

        revenues[j] = q

    return revenues, solution

def print_cut_rod_solution(solution: Dict[int, int], n: int):
    while n > 0:
        # Print in reverse order
        print(solution[n])
        n = n - solution[n]


if __name__ == '__main__':
    print(cut_rod(lenght_to_price, 4))

    print("Memoized cut rod:")
    print(memoized_cut_rod(lenght_to_price, 4))

    print("Buttom up cut rod:")
    print(buttom_up_cur_rod(lenght_to_price, 4))

    print("Extended buttom up cut rod:")
    r, s = extended_bottom_cut_rod(lenght_to_price, 4)
    print_cut_rod_solution(s, 4)