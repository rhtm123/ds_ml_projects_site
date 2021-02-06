from django.shortcuts import render
import pickle

# project 1


def spam_detector_view(request):

    context_dict = {}
    if request.method == 'POST':
        with open('ml_models/spam_detector.pkl', 'rb') as file:
            model = pickle.load(file)

        with open('ml_models/spam_detector_vector.pkl', 'rb') as file:
            count_vect = pickle.load(file)
        msg_input = request.POST.get('msg', None)
        msg = [msg_input]

        if msg:
            n = count_vect.transform(msg)
            predictions = model.predict(n)
            prediction = 'spam' if list(predictions)[
                0] == 'spam' else 'not spam'
            context_dict['msg'] = prediction

        return render(request, 'spam_detector_view.html', context_dict)

    else:
        return render(request, 'spam_detector_view.html', context_dict)

# project 2


def sentiment_analysis_view(request):

    context_dict = {}
    if request.method == 'POST':
        with open('ml_models/sentiment_analysis_model.pkl', 'rb') as file:
            model = pickle.load(file)

        with open('ml_models/sentiment_analysis_vector.pkl', 'rb') as file:
            count_vect = pickle.load(file)
        msg_input = request.POST.get('msg', None)
        msg = [msg_input]

        if msg:
            n = count_vect.transform(msg)
            predictions = model.predict(n)
            prediction = 'Positive' if list(predictions)[
                0] == 1 else 'Negative'
            context_dict['msg'] = prediction

        return render(request, 'sentiment_analysis_view.html', context_dict)

    else:
        return render(request, 'sentiment_analysis_view.html', context_dict)

# project 3


def handwritten_recognition_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'handwritten_recognition_view.html', {})


# project 4
def car_sale_price_prediction_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'car_sale_price_prediction.html', {})


def churn_prediction_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'churn_prediction.html', {})


def credit_card_fraud_detector_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'credit_card_fraud_detector.html', {})


def gender_age_prediction_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'gender_age_prediction.html', {})


def movie_recommendation_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'movie_recommendation.html', {})


def speech_emotion_prediction_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'speech_emotion_prediction.html', {})
