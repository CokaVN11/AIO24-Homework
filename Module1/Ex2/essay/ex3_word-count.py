import os


def word_count(file_path: str) -> dict:
    count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_lower = word.lower()
                count[word_lower] = count.get(word_lower, 0) + 1
    return count


if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'P1_data.txt')

    word_count_dict = word_count(file_path)
    print(word_count_dict)
