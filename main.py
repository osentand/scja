import markovify
import nltk
import re

wrestlers = './data/stone_cold_quotes.txt'
pride = './data/pride.txt'
yogi = './data/yogi.txt'
powers = './data/ap.txt'

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        if len(words) > 1:
            return [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        else:
            return []

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


def create_model(pth):
    with open(pth) as f:
        text = f.read()
        f.close()
    return POSifiedText(text)


if __name__ == "__main__":
    austen_model = create_model(pride)
    wrestler_model = create_model(wrestlers)

    combined_model = None
    while True:
        try:
            # Input weight for wrestler model vs Jane Austen model
            # Hit enter to resuse previous weight (faster)
            inp = raw_input("SC: ")
            if inp != '':
                combined_model = markovify.combine([austen_model, wrestler_model],
                        [1, float(inp)])
            for i in xrange(10):
                print combined_model.make_short_sentence(140)
                print ''
        except KeyboardInterrupt:
            break
