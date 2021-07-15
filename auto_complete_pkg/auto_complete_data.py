class AutoCompleteData:
    def __init__(self,completed_sentence,source_text,line,offset, score):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.line = line
        self.offset = offset
        self.score = score


    def set_score(self, score):
        self.score = score


    def get_data(self):
        return (self.completed_sentence) ,( self.source_text ,  self.line, self.offset), self.score

    # def __str__(self):
    #     return self.completed_sentence + "(" + self.source_text + self.offset + ")"