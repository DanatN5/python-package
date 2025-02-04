import sys

from my_lib import half


def main():
    print(half(float(sys.argv[-1])))


if __name__ == "__main__":
    main()
