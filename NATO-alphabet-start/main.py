import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary={row.letter: row.code for (index,row)  in data.iterrows()}

def generate_phonetic_alphabet():
    word=input("Enter a word: ").upper()
    try:
        output_list=[phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed.")
        generate_phonetic_alphabet()
    else:
        print(output_list)

generate_phonetic_alphabet()


















