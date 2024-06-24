import streamlit as st


def load_vocab(file_path: str) -> list:
    with open(file_path, "r") as f:
        lines = f.readlines()

    try:
        vocab = sorted(set([line.strip().lower() for line in lines]))
        return vocab
    except Exception as e:
        print(f"Error: {e}")
        return []


def levenshtein_distance(token1: str, token2: str) -> int:
    distances = [[0 for _ in range(len(token2) + 1)]
                 for _ in range(len(token1) + 1)]

    for i in range(len(token1) + 1):
        distances[i][0] = i

    for j in range(len(token2) + 1):
        distances[0][j] = j

    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                insert_cost = distances[i][j - 1]
                delete_cost = distances[i - 1][j]
                replace_cost = distances[i - 1][j - 1]
                distances[i][j] = 1 + \
                    min(insert_cost, delete_cost, replace_cost)

    return distances[-1][-1]


def levenshtein_list(token: str, vocab: list) -> dict:
    distances = {}
    for word in vocab:
        distances[word] = levenshtein_distance(token, word)

    sorted_distances = dict(sorted(distances.items(), key=lambda x: x[1]))
    return sorted_distances


def main():
    vocabs = load_vocab("vocab.txt")
    st.title("Word Correction App")
    word = st.text_input("Enter a word:")

    if st.button("Compute"):
        leven_distances = levenshtein_list(word, vocabs)
        corrected_word = list(leven_distances.keys())[0]

        st.write(f"Did you mean: {corrected_word}")

        col1, col2 = st.columns(2)
        with col1:
            st.write("Vocabulary:")
            st.write(vocabs)

        with col2:
            st.write("Distance:")
            st.write(leven_distances)


if __name__ == "__main__":
    main()
