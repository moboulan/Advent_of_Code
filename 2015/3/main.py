
def parse(f_name: str) -> str:

    with open(f_name) as f:
        return f.readline().rstrip('\n')

def get_moves(moves: list[str]):

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

    return houses


def solve() -> int:
    moves = parse("test.txt")
    santa_moves = []
    santabot_moves = []

    for i, c in enumerate(moves):
        if i % 2 == 0:
            santa_moves.append(c)
        else:
            santabot_moves.append(c)
  
    return len(get_moves(santa_moves) | get_moves(santabot_moves))


def main():
    result = solve()
    print(result)


if __name__ == "__main__":
    main()
