import markovify

wrestlers = '/Users/osentand/PycharmProjects/stone_cold_jane_austen/stone_cold_quotes.txt'
pride = '/Users/osentand/PycharmProjects/stone_cold_jane_austen/pride.txt'


def create_model(pth):
    with open(pth) as f:
        text = f.read()
        f.close()
    return markovify.Text(text)


wrestler_model, austen_model = create_model(wrestlers), create_model(pride)
combined_model = markovify.combine([wrestler_model, austen_model],[10,0.5])

combined_model.make_short_sentence(140)