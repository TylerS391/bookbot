def word_count():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
        return len(words)
    
def count_characters():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        text = text.lower()

        char_count = {}
        for char in text:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        return char_count

def sort_by_count(item):
    return item[1]

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{word_count()} words found in the document\n")

    char_count_result = count_characters()
    sorted_char_counts = sorted(char_count_result.items(), key=sort_by_count, reverse=True)

    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    main()