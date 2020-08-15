import pandas as pd
import joblib

def getRating(test_case):
    empty_test = pd.read_csv("empty_test.csv")
    empty_test['year'] = test_case[0]
    empty_test['duration'] = test_case[1]
    empty_test['budget'] = test_case[2]
    empty_test[[c for c in empty_test if c.endswith(test_case[3])]] = 1
    empty_test[[c for c in empty_test if c.endswith(test_case[4])]] = 1

    movie_model = joblib.load("./ML Models/rf.sav")
    test_prediction = movie_model.predict(empty_test)
    # prediction = label_encoder.inverse_transform(test_prediction)

    if test_prediction[0] == 2:
        return "Good"
    elif test_prediction == 0:
        return "Bad"
    else:
        return "Excellent"

    