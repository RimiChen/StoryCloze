from gensim import models

stringTest = "some";
sentence = models.doc2vec.LabeledSentence(
    words=[u'some' , u'words', u'here'], tags=["SENT_0"])
sentence1 = models.doc2vec.LabeledSentence(
    words=[u'here', u'we', u'go'], tags=["SENT_1"])


sentences = [sentence, sentence1]
#print(sentences)

class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        for uid, line in enumerate(open(filename)):
            yield LabeledSentence(words=line.split(), labels=['SENT_%s' % uid])
            
model = models.Doc2Vec(alpha=.025, min_alpha=.025, min_count=1)
model.build_vocab(sentences)

for epoch in range(10):
    model.train(sentences)
    model.alpha -= 0.002  # decrease the learning rate`
    model.min_alpha = model.alpha  # fix the learning rate, no decay

model.save("my_model.doc2vec")
model_loaded = models.Doc2Vec.load('my_model.doc2vec')


print(model_loaded.docvecs.most_similar([model_loaded.infer_vector("astronaut kisses moon".split())]))
#print(model_loaded.docvecs.similarity("SENT_0", "SENT_1"))
#print(model_loaded.docvecs.similarity("SENT_1", "SENT_2"))
#print(model_loaded.docvecs.similarity("SENT_2", "SENT_0"))

#print(model_loaded.infer_vector("astronaut kisses moon".split()))