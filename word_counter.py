
import sys

def count_words(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        return None
    word_list = data.split()
    return len(word_list)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 word_counter.py <filename>")
        return
    filename = sys.argv[1]
    result = count_words(filename)
    if result is not None:
        print("Total words in file:", result)

if __name__ == "__main__":
    main()
