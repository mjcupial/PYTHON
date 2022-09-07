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


    def even_seq(self, sequence):
        print([even for even in sequence if even%2==0])
        print(f"There are {} even elements:\n{}")

    # def odd_seq(self):


fibo1 = FiboSeq()
fibo1.create_Fibo(0,8)
fib = fibo1.create_Fibo(3,8)
fibo1.even_seq(fib)


