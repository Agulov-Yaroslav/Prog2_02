from typing import Iterable

from corpus_utils import Sentence
from tagger_models import Tagger


class TaggerTester:
    def evaluate_tagger(self, corpus, tagger):
        correct = []
        for sentence in corpus:
            predictions = tagger(sentence)
            correct.extend(
                [
                    prediction.pos_tag == token.pos_tag
                    for prediction, token in zip(predictions, sentence)
                ]
            )
        print(f"Tagger: {str(tagger)}")
        print(f"Accuracy: {sum(correct)/len(correct)}")

    def compare_taggers(self, corpus, taggers) -> None:
        for tagger in taggers:
            self.evaluate_tagger(corpus, tagger)
            print("------")
