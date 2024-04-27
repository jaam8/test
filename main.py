import operator


def calc(txt: str) -> int | float:
    def transform(txt: str) -> list:
        ll = [int(x) if x.isdigit() else x for x in txt.split()]
        return ll

    def priority(ex: list) -> list:
        for x in range(len(ex)):
            if ex[x] == "*" or ex[x] == "/":
                ex[x] = operators[ex[x]](ex[x - 1], ex[x + 1])
                ex[x - 1] = ""
                ex[x + 1] = ""
        return [x for x in ex if x != ""]

    def bil(ex: list) -> int | float:
        x = 0
        while len(ex) != 1:
            if ex[x] == "+" or ex[x] == "-":
                ex[x] = operators[ex[x]](ex[x - 1], ex[x + 1])
                del ex[x + 1]
                del ex[x - 1]
            else:
                x += 1
        return ex[0]

    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    return bil(priority(transform(txt)))


print(calc(input()))
