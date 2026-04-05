import json
import os
import pickle
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .analyzer import extract_features

def home(request):
    return render(request, 'detector/index.html')

@csrf_exempt
@require_POST
def detect_api(request):
    try:
        data = json.loads(request.body)
        url = data.get('url', '')
        
        if not url:
            return JsonResponse({'error': 'URL is required'}, status=400)
            
        model_path = os.path.join(settings.BASE_DIR, 'model.pkl')
        if not os.path.exists(model_path):
            return JsonResponse({
                'error': 'Prediction model (model.pkl) not found. Please train and save the model first.'
            }, status=503)
            
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
            
        # Extract features and convert to list
        features_dict = extract_features(url)
        feature_values = list(features_dict.values())
        
        # Predict using the model
        prediction = model.predict([feature_values])[0]
        probabilities = model.predict_proba([feature_values])[0]
        
        # Interpret prediction (handles outputs like 1, 0, 'phishing', or 'legitimate')
        pred_str = str(prediction).lower()
        is_phishing = bool(pred_str == 'phishing' or pred_str == '1' or pred_str == 'true')
        
        confidence = round(float(max(probabilities)) * 100, 2)
        verdict = 'Phishing Detected' if is_phishing else 'Safe'
        
        return JsonResponse({
            'url': url,
            'is_phishing': is_phishing,
            'confidence': confidence,
            'verdict': verdict
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

