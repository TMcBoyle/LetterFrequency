import json
import os
import sys

def build_length_file():
    # Load words
    with open("./words.json") as f:
        words = json.load(f)

    # Create word length lookup
    lengths = {}
    for k in words:
        l = len(k)
        if not l in lengths:
            lengths[l] = [k]
        else:
            lengths[l].append(k)

    # Save to new file
    with open("lengths.json", "w") as f:
        json.dump(lengths, f)

def main(length):
    if not os.path.exists("./lengths.json"):
        build_length_file()

    with open("./lengths.json") as f:
        lengths = json.load(f)

    letters = { c : 0 for c in "abcdefghijklmnopqrstuvwxyz" }
    for word in lengths[length]:
        for letter in word:
            letters[letter] += 1
    
    letters_sorted = sorted(((v, k) for k, v in letters.items()), reverse=True)
    with open("./result.txt", "w") as f:
        f.writelines([f"{k}: {v}\n" for v, k in letters_sorted])

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("usage: python main.py [word length]")
