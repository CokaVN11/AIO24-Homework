def letters_count(word: str) -> dict:
    count = {}
    for letter in word:
        count[letter] = count.get(letter, 0) + 1
    return count


if __name__ == "__main__":
    print(letters_count("happiness"))
    print(letters_count("smiles"))
