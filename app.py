from flask import Flask, render_template, request, send_file
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    image = request.files["image"]
    img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)

    # Resize for consistency (optional)
    img = cv2.resize(img, (600, 600))

    # 1. Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Invert gray image
    inverted = 255 - gray

    # 3. Blur the inverted image
    blur = cv2.GaussianBlur(inverted, (25, 25), 0)

    # 4. Dodge blend (sharp pencil effect)
    pencil = cv2.divide(gray, 255 - blur, scale=256)

    # Convert to 3 channels so we can add color
    pencil_rgb = cv2.cvtColor(pencil, cv2.COLOR_GRAY2BGR)

    # 5. Light pastel color (5–10% only)
    pastel = cv2.bilateralFilter(img, d=9, sigmaColor=40, sigmaSpace=40)

    # 6. Blend pencil + very soft color
    final = cv2.addWeighted(pencil_rgb, 0.90, pastel, 0.10, 0)

    # 7. Optional sharpening for outlines
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    final = cv2.filter2D(final, -1, kernel)

    # Save output
    cv2.imwrite("static/final.png", final)
    return send_file("static/final.png", mimetype="image/png")



if __name__ == "__main__":
    app.run(debug=True)
