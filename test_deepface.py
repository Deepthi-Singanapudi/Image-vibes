from deepface import DeepFace

# Path to your test image
img_path = "202.jpg"

# Analyze the image
analysis = DeepFace.analyze(img_path, actions=['age', 'gender', 'race', 'emotion'])

print("Analysis results:")
print(analysis)