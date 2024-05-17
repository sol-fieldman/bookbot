def main():
    with open('books/frankenstein.txt') as f:
        book = f.read()
        print(book)
        print(f"document has {wc(book)} words")

        letter_dict = letter_count(book)
        letters = sorted(letter_dict)
        print("============ Begin Letter Report ============")
        for i in letters:
            print(f"{i} appeared {letter_dict[i]} times")
        print("=============== End of Report ===============")




def wc(text):
    words = text.split()
    return len(words)

def letter_count(text):
    lowercase_text = text.lower()
    alphabet = {}
    for char in lowercase_text:
        if char.isalpha():
            if not (char in alphabet):
                alphabet[char] = 1
            else:
                alphabet[char] += 1
    return alphabet

main()
