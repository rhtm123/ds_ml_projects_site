from django.urls import path
from demo.views import *

app_name = 'demo'
urlpatterns = [
    path('spam_detector_demo/', spam_detector_view),
    path('sentiment_analysis_demo/', sentiment_analysis_view),
    path('handwritten_recognition_demo/', handwritten_recognition_view)

]
