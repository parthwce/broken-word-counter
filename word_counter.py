# Broken Word Counter Example
import sys

def count_words(filename):
    with open(filename, "r") as f:
        data = f.readlines()
        return len(data)  # Bug: counts lines only!

def main():
    if len(sys.argv) < 2:
        print("Missing argument: filename")
        return
    filename = sys.argv[1]
    print("Total lines in file:", count_words(filename))  # Wrong output message

if __name__ == "__main__":
    main()
