def get_book_text(f):
    with open(f) as text:
        return text.read()

def get_word_count(f):
    final_cnt = f.split()
    return len(final_cnt)

def main():
    the_text = get_book_text("books/frankenstein.txt")
    the_cnt = get_word_count(the_text)
    print(f"{the_cnt} words found in the document")
main()
