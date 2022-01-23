class Fizzbuzz:
    modulos = [
        (3, "fizz"),
        (5, "buzz"),
    ]
    @staticmethod
    def run(numbers: list=range(1, 101)):
        output = ""
        for i in numbers:
            output += Fizzbuzz.evaluate(i)+"\n"
        return output
    @staticmethod
    def evaluate(input: int):
        evaluation = ""
        for modulo in Fizzbuzz.modulos:
            if input % modulo[0] == 0:
                evaluation += modulo[1]
        if evaluation == "":
            evaluation += str(input)
        return evaluation
