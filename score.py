import pickle



def score(essay, selected_model):
    name2path = {
    }
    model = pickle.load(name2path[selected_model])
    vectorizer = pickle.load(open('vectorizer.pkl'))
    features = vectorizer.transform(essay)
    score_ = model.predict(features)
    return score_
