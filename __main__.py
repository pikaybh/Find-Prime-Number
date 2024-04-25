from functools import lru_cache, wraps
from typing import Callable, Iterator
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--start", default=1, type=int, help="Start number (default : 1)")
parser.add_argument("--end", default=None, type=int, help="End number")
parser.add_argument("--show-list", default=False, type=bool, help="소수 보여줌.")
args = parser.parse_args()

sys.setrecursionlimit(10_000)

@lru_cache(maxsize=1_000)
def is_prime_num(num : int, i : int = 2) -> bool:
    if i > num:
        raise ValueError(f"{num} cannot be smaller than {i}.")
    return True if num == i else False if num % i == 0 else is_prime_num(num, i+1)

def find_prime_num(end : int, start : int = 2) -> Iterator:
    prime_num = []
    for i in range(start, end+1):
        if is_prime_num(i):
            prime_num.append(i)
    return iter(prime_num)

def count_prime_num(prime_numbers : list) -> dict:
    dec, L, D = 1, [], {}
    for num in prime_numbers:
        if num < 10**dec:
            L.append(num)
        else:
            D[f"{dec-1}"] = L
            L = [num]
            dec += 1
        if num >= prime_numbers[-1]:
            D[f"{dec-1}"] = L
    return D

def main() -> None:
    num = args.end if args.end else int(input("Type integer: "))
    for v, i in count_prime_num([i for i in find_prime_num(num)]).items():
        if args.show_list: print(f"{int(v)+1} 자리 소수의 갯수: {len(i)}. {i}")
        else: print(f"{int(v)+1} 자리 소수의 갯수: {len(i)}")


if __name__ == "__main__":
    main()