class FiboSeq:
    def __init__(self):
        self.__name = "Fibonacci"

    def __repr__(self):
        return f"This is a {self.__name} sequence"

    def create_Fibo(self, f0=0, fn=50):
        sequence = []
        a, b = 0, 1
        while len(sequence) < fn:
            sequence.append(b)
            a, b = b, a + b
        seq = sequence[f0:]
        print(f"That's your {self.__name} sequence:\n{seq}")
        return seq

    def even_seq(self, seq):
        even_seq = [even for even in seq if even % 2 == 0]
        print(f"There are {len(even_seq)} even element(s):\n{even_seq}")
        return even_seq

    def odd_seq(self, seq):
        odd_seq = [even for even in seq if even % 2 != 0]
        print(f"There are {len(odd_seq)} even element(s):\n{odd_seq}")
        return odd_seq


fibo1 = FiboSeq()
fib = fibo1.create_Fibo(4)
fibo1.even_seq(fib)
fibo1.odd_seq(fib)

