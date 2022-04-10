import sys
import problem


def file_main():
    sys.stdin = open("data.txt", "r")
    for i in sys.stdin.readlines():
        a, b = map(int, i.rstrip("\n").split())
        result = problem.problem(a, b)
        for r in result:
            print(r)


def main():
    n, m = map(int, input().split())
    result = problem.problem(n, m)
    for r in result:
        print(r)


if __name__ == "__main__":
    main()

# def test_problem():
# assert problem.problem(1, 2, 3) == 4
