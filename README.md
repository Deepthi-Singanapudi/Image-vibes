# 🎵 Image Vibes

**Image Vibes** is a smart web application that takes an image, generates a caption using AI, detects the mood from the caption, and recommends music based on that mood.



## 🔍 Features

- 📸 Upload any image
- 🧠 Generate meaningful captions using AI (BLIP model)
- 😊 Detect emotional mood from the caption
- 🎧 Get music recommendations that match the mood
- 🧪 Simple UI with Flask backend



## 🛠️ Tech Stack

- Python
- Flask
- HTML & CSS (Jinja templates)
- BLIP (Bootstrapped Language Image Pretraining) model
- Mood analysis
- Music recommendation logic (based on detected mood)

---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/Deepthi-Singanapudi/image-vibes.git
   cd image-vibes
````

2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**

   ```bash
   python app.py
   ```

5. Open browser and go to `http://127.0.0.1:5000`

---

## 📁 Folder Structure

```
image-vibes/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   ├── result.html
│   └── settings.html
├── utils/
│   ├── caption_generator.py
│   ├── mood_detector.py
│   └── music_recommender.py
└── static/
```

---

## ✨ Future Improvements

* Add user authentication
* Support for multiple moods
* Spotify/Youtube music player integration
* Improve UI/UX

---

## 🙋‍♀️ Made with ❤️ by Deepthi Singanapudi

```

---

## 📌 To Add This to GitHub:

1. In your project folder, create a file:
```

README.md

````

2. Paste the above content in that file.

3. Save it, then run these Git commands:

```bash
git add README.md
git commit -m "Added README file"
git push
````

