import markovify

wrestlers = './data/stone_cold_quotes.txt'
pride = './data/pride.txt'


def create_model(pth):
    with open(pth) as f:
        text = f.read()
        f.close()
    return markovify.Text(text)


if __name__ == "__main__":
    wrestler_model, austen_model = create_model(wrestlers), create_model(pride)
    combined_model = markovify.combine([wrestler_model, austen_model],[10,0.5])

    print combined_model.make_short_sentence(140)
