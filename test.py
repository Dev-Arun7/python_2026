from typing import Any

def list_words(words: list[str]) -> None:
    for i, word in enumerate(words):
        print(i, word)

class ListWords:
    def __call__(self, words: list[str]) -> Any:
        for i, word in enumerate(words):
            print(i, word)

def main() -> None:
    words = ["python", "ai", "code", "program", "work"]
    # my_function = list_words
    # my_function(words)
    list_words_fn = ListWords()
    list_words_fn(words)


if __name__ == "__main__":
    main()
