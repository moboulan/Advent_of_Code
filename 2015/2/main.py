
def parse(f_name: str) -> list[tuple[int, int, int]]:
    result = []
    with open(f_name) as f:
        for line in f.read().splitlines():
            a, b, c = line.split("x")
            result.append((int(a) ,int(b), int(c)))
    return result


def solve() -> int:
    boxes = parse("input.txt")
    total_paper = 0
    for l, h, w in boxes:
        total_paper += 2*(l*w) + 2*(w*h) + 2*(h*l) + min((l*w), (w*h), (h*l))

    return total_paper

def main():
    result = solve()
    print(result)


if __name__ == "__main__":
    main()
