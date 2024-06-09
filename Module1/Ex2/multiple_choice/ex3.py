import os


def count_word(file_path: str) -> dict:
    counter = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_lower = word.lower()
                counter[word_lower] = counter.get(word_lower, 0) + 1
    return counter


if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'P1_data.txt')

    result = count_word(file_path)
    assert result['who'] == 3
    print(result['man'])
