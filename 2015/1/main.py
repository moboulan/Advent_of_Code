
def parse(f_name: str) -> str:
    with open(f_name) as f:
        return f.read().rstrip('\n')


def main():
    instructions = parse("input.txt")
    floor = 0

    for c in instructions:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

    print(floor)


if __name__ == "__main__":
    main()
