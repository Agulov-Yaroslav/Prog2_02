from corpus_utils import Corpus
from tagger_models import UnigramTagger, NounTagger
from eval_utils import TaggerTester

if __name__ == "__main__":
    train_corpus = Corpus("train.tsv")
    test_corpus = Corpus("test.tsv")

    # my_tagger = UnigramTagger()
    # my_tagger.train(train_corpus)
    # noun_tagger = NounTagger()
    #
    # tester = TaggerTester()
    # tester.compare_taggers(
    #     test_corpus, [my_tagger, noun_tagger],
    # )