class SerieMatematica:
    def __init__(self, reps: int):
        self.__reps = reps
        self.__first = True

    def get_reps(self):
        return self.__reps

    def set_reps(self, reps: int):
        self.__reps = reps

    def fibonacci(self, a: int, b: int):
        if self.__first:
            print("Série de Fibonacci")
            self.__first = False

        for i in range(self.__reps):
            a, b = b, a + b
            print(a)

        return a

    def fatorial(self):
        n = 1

        for i in range(1, self.__reps + 1):
            print(n)
            n *= i

        return n

    def fibonarial(self, a: int, b: int):
        result = self.fibonacci(a, b) * self.fatorial()
        print(result)
        return result

    def primo(self):
        if self.__reps == 1:
            print(False)
            return False
        for i in range(2, self.__reps):
            if self.__reps % i == 0:
                print(False)
                return False
        print(True)
        return True
