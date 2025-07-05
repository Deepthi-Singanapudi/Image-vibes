import os
from flask import Flask, render_template, request, session, redirect, url_for,flash
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey123'  # Required for session management

# Load the BLIP captioning model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


# Dummy authentication function (you can replace this with DB logic)
def is_valid_user(username, password):
    return username == "Harshitha_somu" and password == "harshi1234"


# Route for homepage
@app.route("/")
def index():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))
    return render_template("index.html", username=username)


# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if is_valid_user(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')


# Route for logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


# Route for handling image upload and caption/music generation
@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return "No image uploaded", 400

    file = request.files["image"]
    if file.filename == "":
        return "No selected file", 400

    if file:
        filename = file.filename
        filepath = os.path.join("static/uploads", filename)

        # Save uploaded image
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        file.save(filepath)

        # Generate caption
        caption = generate_caption(filepath)

        # Detect mood
        mood = detect_mood(caption)

        # Recommend music
        songs = get_music(mood)

        return render_template("result.html", caption=caption, image_path=filepath, mood=mood, songs=songs)


# Generate caption using BLIP
def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption


# Simple mood detection
def detect_mood(caption):
    caption = caption.lower()
    if "happy" in caption or "smile" in caption:
        return "Happy"
    elif "sad" in caption or "lonely" in caption:
        return "Sad"
    elif "sunset" in caption or "love" in caption:
        return "Romantic"
    elif "party" in caption or "dance" in caption:
        return "Energetic"
    else:
        return "Calm"


# Music recommendation based on mood
def get_music(mood):
    music_library = {
        "Happy": ["Happy - Pharrell Williams", "Best Day of My Life - American Authors"],
        "Sad": ["Someone Like You - Adele", "Fix You - Coldplay"],
        "Romantic": ["Perfect - Ed Sheeran", "All of Me - John Legend"],
        "Energetic": ["Can't Stop - Red Hot Chili Peppers", "Titanium - David Guetta ft. Sia"],
        "Calm": ["Weightless - Marconi Union", "Bloom - ODESZA"]
    }
    return music_library.get(mood, ["Let It Be - The Beatles"])




'''@app.route('/register', methods=['POST'])
def register():
    # Get form data
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Example validation
    if password != confirm_password:
        return "Passwords do not match"  # Replace with flash and return template in real app

    # Save user logic here...

    session['username'] = username  # Log user in
    return redirect(url_for('index'))'''

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # process registration here...
        # if success:
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)