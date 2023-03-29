class Solution:
    def fib(self, n: int) -> int:

        fib_list, idx = [0, 1], 1

        while idx <= n:
            fib_list.append(fib_list[-2] + fib_list[-1])
            idx += 1
        
        return fib_list[n]