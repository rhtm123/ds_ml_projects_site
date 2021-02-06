from django.shortcuts import render
import pickle

import numpy as np
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
    context_dict = {}

    Fuel_Type_Diesel = 0
    if request.method == 'POST':
        model = pickle.load(
            open('ml_models/rf_car_prediction_model.pkl', 'rb'))
        Year = int(request.POST['Year'])
        Present_Price = float(request.POST['Present_Price'])
        Kms_Driven = int(request.POST['Kms_Driven'])
        if Kms_Driven == 0:
            Kms_Driven = 1
        Kms_Driven2 = np.log(Kms_Driven)
        Owner = int(request.POST['Owner'])
        Fuel_Type_Petrol = request.POST['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol == 'Petrol'):
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        Year = 2021-Year
        Seller_Type_Individual = request.POST['Seller_Type_Individual']
        if(Seller_Type_Individual == 'Individual'):
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0
        Transmission_Mannual = request.POST['Transmission_Mannual']
        if(Transmission_Mannual == 'Mannual'):
            Transmission_Mannual = 1
        else:
            Transmission_Mannual = 0
        prediction = model.predict([[Present_Price, Kms_Driven2, Owner, Year, Fuel_Type_Diesel,
                                     Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
        output = round(prediction[0], 2)
        print(output)
        if output < 0:
            context_dict['prediction_text'] = "Sorry you cannot sell this car"
        else:
            context_dict['prediction_text'] = "You Can Sell The Car at {} lakhs".format(
                output)

        return render(request, 'car_sale_price_prediction.html', context_dict)

    else:
        return render(request, 'car_sale_price_prediction.html', context_dict)


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
