from corpus_utils import Token, Sentence, Corpus


class Tagger:
    # So etwas würde man natürlich nicht machen. Wir lernen abstrakte Klassen, die an dieser Stelle geeigneter wären, später kennen.
    pass


class NounTagger(Tagger):
    def __str__(self) -> str:
        return "NounTagger"

    def tag(self, untagged_sentence: Sentence) -> Sentence:
        return Sentence([Token(token.form, "NOUN") for token in untagged_sentence])

    def __call__(self, untagged_sentence: Sentence):
        return self.tag(untagged_sentence)


class UnigramTagger:
    def __init__(self) -> None:
        self._counter: dict[str, dict] = dict()

    def __str__(self) -> str:
        return "UnigramTagger"

    @property
    def counter(self):
        return self._counter

    def train(self, corpus: Corpus) -> None:
        for sentence in corpus:
            for token in sentence:
                self.counter[token.form] = self.counter.get(token.form, {})
                self.counter[token.form][token.pos_tag] = (
                    self.counter[token.form].get(token.pos_tag, 0) + 1
                )

    def tag(self, untagged_sentence: Sentence) -> Sentence:
        return Sentence(
            [
                Token(
                    token.form,
                    max(self.counter[token.form], key=self.counter[token.form].get)
                    if token.form in self.counter
                    else "NOUN",
                )
                for token in untagged_sentence
            ]
        )

    def __call__(self, sentence):
        return self.tag(sentence)
