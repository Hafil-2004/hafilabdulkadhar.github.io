from flask import Flask, request, render_template, jsonify
import torch
import torchvision.transforms as transforms
from PIL import Image
import io
from model import load_model  # Ensure this function exists in model.py

app = Flask(__name__)

# Load trained model
model = load_model("cifar10_model.pth")

# Define CIFAR-10 class labels
class_labels = ["Airplane", "Automobile", "Bird", "Cat", "Deer", 
                "Dog", "Frog", "Horse", "Ship", "Truck"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    try:
        image = Image.open(io.BytesIO(file.read())).convert("RGB")
        
        transform = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])
        
        image = transform(image).unsqueeze(0)  # Add batch dimension
        output = model(image)
        _, predicted_class = torch.max(output, 1)
        prediction = class_labels[predicted_class.item()]
        
        return jsonify({"prediction": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
