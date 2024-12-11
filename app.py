from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# Folder containing images
IMAGE_FOLDER = "static/images"

@app.route("/")
def home():
    # Get a list of image filenames from the folder
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    return render_template("slider.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)
