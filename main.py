from os import write


class WordPair:
    english: str
    german: str

    def __init__(self, english: str, german: str):
        self.english = english
        self.german = german

    def __repr__(self) -> str:
        return f"(e: {self.english}, d: {self.german})"


def load_tsv(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.read().splitlines()


def parse_tsv(lines: list[str]) -> list[WordPair]:
    word_pairs = []
    for line in lines:
        parts = line.split("\t")
        wp = WordPair(parts[2], parts[1])
        word_pairs.append(wp)
    return word_pairs


def main():
    print("Hello from deutsch-lernen!")

    raw_tsv_data: list[str] = load_tsv("../../../Downloads/german.tsv")
    word_pairs: list[WordPair] = parse_tsv(raw_tsv_data[1:])

    print(f"First word pair is: {word_pairs[0]}")

    with open("eng_deu.json", "w") as file:
        file.write('{\n  "word_pairs": [\n')
        file.writelines(
            f'    {{ "english": "{wp.english}", "german": "{wp.german}" }},\n'
            for wp in word_pairs
        )
        file.write("  ]\n}\n")


if __name__ == "__main__":
    main()
