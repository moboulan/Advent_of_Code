
def parse(f_name: str) -> str:
    with open(f_name) as f:
        return f.readline()


def solve() -> int:
    instructions = parse("input.txt")
    floor = 0

    for i, c in enumerate(instructions):
        if floor == -1:
            return i
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

    return -1

def main():
    result = solve()
    print(result)


if __name__ == "__main__":
    main()
