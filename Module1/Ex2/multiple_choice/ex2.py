def character_count(word):
    character_statistic = {}
    # Your Code Here
    for char in word:
        character_statistic[char] = character_statistic.get(char, 0) + 1
    # End Code Here
    return character_statistic


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
