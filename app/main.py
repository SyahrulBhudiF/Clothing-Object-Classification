from flask import Flask, request, render_template
import os
from ultralytics import YOLO

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

model = YOLO("yolov8.pt")

@app.route("/", methods=["GET", "POST"])
def index():
    predictions = None
    image_path = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(image_path)

            results = model(image_path)
            predictions = [
                {
                    "class": model.names[int(box[5])],
                    "confidence": f"{box[4] * 100:.2f}%"
                }
                for box in results[0].boxes.data.tolist()
            ]

    return render_template("index.html", predictions=predictions, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)
