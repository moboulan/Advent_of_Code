
def parse(f_name: str) -> list[tuple[int, int, int]]:
    result = []
    with open(f_name) as f:
        for line in f.read().splitlines():
            a, b, c = line.split("x")
            result.append((int(a) ,int(b), int(c)))
    return result


def solve() -> int:
    boxes = parse("input.txt")
    total_ribbon = 0
    for l, h, w in boxes:
        s = list(sorted((l,h,w)))
        total_ribbon += s[0] + s[0] + s[1] + s[1] + l * w * h

    return total_ribbon

def main():
    result = solve()
    print(result)


if __name__ == "__main__":
    main()
