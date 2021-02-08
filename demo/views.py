from django.shortcuts import render
import pickle

import numpy as np
# project 1
import pandas as pd


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


def flight_fare_prediction_view(request):
    context_dict = {}
    if request.method == 'POST':
        model = pickle.load(
            open('ml_models/flight_rf.pkl', 'rb'))
        date_dep = request.POST["Dep_Time"]
        Journey_day = int(pd.to_datetime(
            date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(
            date_dep, format="%Y-%m-%dT%H:%M").month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.POST["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(
            date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(
            date_arr, format="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)

        if dur_hour < 0:
            context_dict["prediction_text"] = "Something went wrong. Maybe you selected wrong date"
            return render(request, 'flight_fare_prediction.html', context_dict)

        Total_stops = int(request.POST["stops"])

        airline = request.POST['airline']

        airline_dict = {'Jet_Airways': 0, 'IndiGo': 0, 'Air_India': 0, 'Multiple_carriers': 0, "SpiceJet": 0, 'Vistara': 0, "GoAir": 0,
                        "Multiple_carriers_Premium_economy": 0, "Jet_Airways_Business": 0, "Vistara_Premium_economy": 0, "Trujet": 0}

        if(airline == 'Jet Airways'):
            airline_dict['Jet_Airways'] = 1
        elif (airline == 'IndiGo'):
            airline_dict['IndiGo'] = 1
        elif (airline == 'Air India'):
            airline_dict['Air_India'] = 1
        elif (airline == 'Multiple carriers'):
            airline_dict['Multiple_carriers'] = 1
        elif (airline == 'SpiceJet'):
            airline_dict['SpiceJet'] = 1
        elif (airline == 'Vistara'):
            airline_dict['Vistara'] = 1
        elif (airline == 'GoAir'):
            airline_dict['GoAir'] = 1

        Source = request.POST["Source"]
        s_dict = {'s_Delhi': 0, 's_Kolkata': 0, 's_Mumbai': 0, 's_Chennai': 0}

        if (Source == 'Delhi'):
            s_dict['s_Delhi'] = 1

        elif (Source == 'Kolkata'):
            s_dict['s_Kolkata'] = 1

        elif (Source == 'Mumbai'):
            s_dict['s_Mumbai'] = 1

        elif (Source == 'Chennai'):
            s_dict['s_Chennai'] = 1

        Source = request.POST["Destination"]
        d_dict = {'d_Cochin': 0, 'd_Delhi': 0,
                  'd_New_Delhi': 0, 'd_Hyderabad': 0, 'd_Kolkata': 0}
        if (Source == 'd_Cochin'):
            d_dict['d_Cochin'] = 1

        elif (Source == 'd_Delhi'):
            d_dict['d_Delhi'] = 1

        elif (Source == 'd_New_Delhi'):
            d_dict['d_New_Delhi'] = 1

        elif (Source == 'd_Hyderabad'):
            d_dict['d_Hyderabad'] = 1
        elif (Source == 'd_Kolkata'):
            d_dict['d_Kolkata'] = 1
        try:
            prediction = model.predict([[
                Total_stops,
                Journey_day,
                Journey_month,
                Dep_hour,
                Dep_min,
                Arrival_hour,
                Arrival_min,
                dur_hour,
                dur_min,
                airline_dict['Air_India'],  # Air_India,
                airline_dict['GoAir'],  # GoAir,
                airline_dict['IndiGo'],  # IndiGo,
                airline_dict['Jet_Airways'],  # Jet_Airways,
                airline_dict['Jet_Airways_Business'],  # Jet_Airways_Business,
                airline_dict['Multiple_carriers'],  # Multiple_carriers,
                # Multiple_carriers_Premium_economy,
                airline_dict['Multiple_carriers_Premium_economy'],
                airline_dict['SpiceJet'],  # SpiceJet,
                airline_dict['Trujet'],  # Trujet,
                airline_dict['Vistara'],  # Vistara,
                # Vistara, # Vistara_Premium_economy,
                airline_dict['Vistara_Premium_economy'],
                s_dict['s_Chennai'],
                s_dict['s_Delhi'],
                s_dict['s_Kolkata'],
                s_dict['s_Mumbai'],
                d_dict['d_Cochin'],
                d_dict['d_Delhi'],
                d_dict['d_Hyderabad'],
                d_dict['d_Kolkata'],
                d_dict['d_New_Delhi'],
            ]])
            output = round(prediction[0], 2)

            context_dict["prediction_text"] = "Your Flight price is Rs. {}".format(
                output)
        except:
            context_dict["prediction_text"] = "Something went wrong. Maybe selected wrong input"

        return render(request, 'flight_fare_prediction.html', context_dict)

    else:
        return render(request, 'flight_fare_prediction.html', context_dict)


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
