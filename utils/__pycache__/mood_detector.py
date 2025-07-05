from deepface import DeepFace

def detect_mood(image_path):
    try:
        result = DeepFace.analyze(image_path, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion']
    except:
        return "neutral" 