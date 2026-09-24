
def parse(f_name: str) -> str:

    with open(f_name) as f:
        return f.readline()

def solve() -> int:
    moves = parse("test.txt")

    houses = {(0, 0)}

    r, c = (0, 0)
    for m in moves:
        if m == '>':
            c += 1
        elif m == '<':
            c -= 1
        elif m == '^':
            r -= 1
        elif m == 'v':
            r += 1
        houses.add((r, c))

    return len(houses)

def main():
    result = solve()
    print(result)


if __name__ == "__main__":
    main()
