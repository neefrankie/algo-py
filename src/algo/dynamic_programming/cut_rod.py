from typing import Dict, List


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



def cut_rod(prices: List[int], n: int):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, prices[i] + cut_rod(prices, n - i))
    return q

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


if __name__ == '__main__':
    print(cut_rod(lenght_to_price, 4))

    print(memoized_cut_rod(lenght_to_price, 4))