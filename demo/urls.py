from django.urls import path
from demo.views import *

app_name = 'demo'
urlpatterns = [
    path('spam_detector_demo/', spam_detector_view),
    path('sentiment_analysis_demo/', sentiment_analysis_view),
    path('handwritten_recognition_demo/', handwritten_recognition_view),
    path('churn_prediction_demo/', churn_prediction_view),
    path('credit_card_fraud_detector_demo/', churn_prediction_view),
    path('gender_age_prediction_demo/', gender_age_prediction_view),
    path('movie_recommendation_demo/', movie_recommendation_view),
    path('car_sale_price_prediction_demo/', car_sale_price_prediction_view),
    path('speech_emotion_prediction_demo/', speech_emotion_prediction_view),
    path('flight_fare_prediction_demo/', flight_fare_prediction_view),
    path('diabetes_prediction_demo/', diabetes_prediction_view),
]
