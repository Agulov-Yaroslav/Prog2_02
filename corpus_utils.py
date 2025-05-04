class Token:
    def __init__(self, form, pos_tag=None):
        self.form = form
        self.pos_tag = pos_tag

    def __repr__(self):
        return f"Token(form='{self.form}', pos_tag='{self.pos_tag}')"


class Sentence:
    def __init__(self, tokens):
        self.tokens = tokens

    def __repr__(self):
        return ' '.join([tok.form for tok in self.tokens])

    def __len__(self):
        return len(self.tokens)

    def __iter__(self):
        return iter(self.tokens)


    def __getitem__(self, index):
        return self.tokens[index]


class Corpus:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sentences = []
        self.raw_text = []
        self._read_corpus()
        self.index = 0


    def __getitem__(self, index):
        return self.sentences[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.sentences):
            sentence =  self.sentences[self.index]
            self.index+=1
            return sentence
        else:
            raise StopIteration

    def __len__(self):
        return len(self.sentences)

    def _read_corpus(self):
        with open(self.file_path) as f:
            current_sentence = []
            for line in f:
                if line.split():
                    split_line = line.split("\t")
                    self.raw_text.append(split_line[0] + " ")
                    token = Token(*line.split("\t"))
                    current_sentence.append(token)

                else:
                    # self.raw_text.append("\n")
                    self.sentences.append(Sentence(current_sentence))
                    current_sentence = []
            if current_sentence:
                sentence = Sentence(current_sentence)
                self.sentences.append(sentence)
