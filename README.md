[README.md](https://github.com/user-attachments/files/23809400/README.md)

# 🎨 Image Sketch App

[![Python](https://img.shields.io/badge/Python-3.8+-blue)]()
[![Flask](https://img.shields.io/badge/Flask-Web%20App-green)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![Status](https://img.shields.io/badge/Project-Active-brightgreen)]()

A lightweight Flask-based web application that converts images into sketch-style drawings and allows users to annotate them using an in-browser canvas.

---

## 🧾 Table of Contents
- [About](#about)
- [Features](#features)
- [Demo](#demo)
- [Snippets](#snippets)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run Locally](#run-locally)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contact](#contact)

---

## 📌 About

**Image Sketch App** is a Python (Flask) web app that:
- Accepts an image upload  
- Converts the image into a sketch (pencil-sketch style)  
- Allows drawing/editing on a canvas  
- Lets users save or download the edited image  

Uses:
- Flask backend  
- OpenCV / Pillow for image sketch effects  
- HTML / CSS / JavaScript Canvas for drawing tools  

---

## ✨ Features
- Upload images (PNG/JPG)
- Automatic image → sketch conversion
- Canvas drawing & annotation tools
- Adjustable brush
- Save/download the final result
- Clean and modern UI

---

## 🖼 Demo

Run locally and visit:

```
http://127.0.0.1:5000/
```

---

## 🧩 Snippets

### **1. Image Upload + Sketch Conversion (Flask)**

```python
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    img = Image.open(file.stream).convert('RGB')

    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)

    output_path = "static/output/sketch.png"
    cv2.imwrite(output_path, sketch)

    return render_template("index.html", sketch_image=output_path)
```


### **2. Canvas Drawing Logic (Frontend)**

```html
<canvas id="drawCanvas"></canvas>

<script>
const canvas = document.getElementById("drawCanvas");
const ctx = canvas.getContext("2d");

let drawing = false;

canvas.addEventListener("mousedown", () => drawing = true);
canvas.addEventListener("mouseup", () => drawing = false);
canvas.addEventListener("mousemove", draw);

function draw(e) {
    if (!drawing) return;

    ctx.lineWidth = 3;
    ctx.lineCap = "round";
    ctx.strokeStyle = "#000";
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
}
</script>
```


### **3. Save Final Annotated Image**

```javascript
function saveImage() {
    const link = document.createElement("a");
    link.download = "final_sketch.png";
    link.href = canvas.toDataURL();
    link.click();
}
```

---

## 🛠 Prerequisites
- Python 3.8+  
- pip  
- Virtual environment (recommended)

---

## 📥 Installation

```bash
git clone https://github.com/Saswat-Iare25/image-sketch-app.git
cd image-sketch-app

python -m venv venv
venv/Scripts/activate    # Windows
source venv/bin/activate # macOS/Linux

pip install -r requirements.txt
```

---

## 🚀 Run Locally

### Option 1 — Direct Run
```bash
python app.py
```

### Option 2 — Using Flask Environment
```bash
export FLASK_APP=app.py
flask run
```

Local app URL:
```
http://127.0.0.1:5000/
```

---

## 📂 Project Structure

```
image-sketch-app/
│── app.py
│── requirements.txt
│── LICENSE
│── templates/
│   └── index.html
│── static/
│   ├── css/
│   ├── js/
│   └── output/
└── README.md
```

---

## 🖱 Usage
1. Upload an image  
2. Convert it into a sketch  
3. Draw or annotate using canvas  
4. Save or download the result  

---

## ❗ Troubleshooting

| Issue | Solution |
|-------|----------|
| Flask not starting | Activate venv + reinstall dependencies |
| Port busy | `flask run --port 5001` |
| Sketch not showing | Ensure OpenCV installed correctly |
| Can't save image | Ensure `static/output/` has write permissions |

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 👤 Contact
**Author:** Saswat Rath  
**GitHub Repository:** https://github.com/Saswat-Iare25/image-sketch-app

---
