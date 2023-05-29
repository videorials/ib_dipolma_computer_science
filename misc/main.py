from helper import *

def main():

    int = 12345
    dgts = cnt_dgts(int)
    for pos in range(dgts, 0, -1):
        bse = 10 ** (pos -1)
        dgt = int // bse
        int = int - dgt * bse
        print(f"{dgt} {bse}'s")


if __name__ == "__main__":
    main()