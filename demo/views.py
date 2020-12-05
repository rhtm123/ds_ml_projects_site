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
    if request.method == 'POST':
        pass
    else:
        return render(request, 'sentiment_analysis_view.html', {})

# project 3


def handwritten_recognition_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'handwritten_recognition_view.html', {})
