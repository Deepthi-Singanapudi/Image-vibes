from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load the BLIP-2 processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16
).to("cuda" if torch.cuda.is_available() else "cpu")

# Function to generate a caption for the input image


def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt", text="a short photo caption")
    out = model.generate(**inputs, max_new_tokens=20)
    caption = processor.decode(out[0], skip_special_tokens=True)

    # Optional: trim to 1 sentence or 10 words max
    caption = caption.split('.')[0]  # or use caption.split()[:10]
    return caption.strip() + '.'

