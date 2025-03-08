def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    words = book_text.split()
    print(f"{len(words)} words found in the document")


main()
