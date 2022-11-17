import spacy
pro_list_count : list = []
integ_list_count : list = []
pro_list = []
integ_list = []
word : str = None
nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

def __readingTexts(data_form: str):

    with open(data_form, mode='r', encoding='UTF8') as text_of_file:
        reding_file = text_of_file.read()
        return reding_file


def tokenizingText(data_form):

    doc = nlp(__readingTexts(data_form))
    print(doc)
    for token in doc:
        print(f" format: {token.pos_}, {token}")
        if token.pos_ == 'PROPN':
            pro_list.append(token)


        elif token.pos_ == 'NUM':
            integ_list.append(token)

    for word in pro_list:
        pro_list_count.append((word, pro_list.count(word)))

    for number in integ_list:
        integ_list_count.append(( number  , integ_list.count(number)))

    return integ_list_count







