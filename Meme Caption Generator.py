import os, random, re
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("labels.csv")
print(f"Loaded {len(df)} meme entries.")

# Pick a random meme
row = df.sample(1).iloc[0]
img_filename = row['image_name']
img_path = os.path.join("images", "images", img_filename)
sentiment = row.get("overall_sentiment", "neutral")
ocr_text = str(row.get("text_ocr", "")).strip()

# Load image
img = Image.open(img_path)

# ------------------------
# Text Cleanup & Filtering
# ------------------------
def extract_meme_line(text):
    lines = re.split(r"[.\n!?]", text)
    candidates = [l.strip() for l in lines if 10 < len(l.strip()) < 80]

    # Priority to uppercase meme-style lines
    upper = [l for l in candidates if l.isupper()]
    keywords = [l for l in candidates if any(kw in l.lower() for kw in ["when", "me", "that", "why", "how", "first"])]

    if upper:
        return random.choice(upper)
    elif keywords:
        return random.choice(keywords)
    elif candidates:
        return random.choice(candidates)
    else:
        return ""  # No good line

meme_line = extract_meme_line(ocr_text)

# ------------------------
# Rule-Based Captioning
# ------------------------
humor_templates = {
    "school": ["Me in class like '{}'", "When the teacher says '{}'", "Homework be like '{}'", "POV: '{}' in school"],
    "sleep": ["When all you want is '{}'", "Me dreaming of '{}'", "Sleep level: '{}'", "Nap time = '{}'"],
    "work": ["Corporate life: '{}'", "When your boss says '{}'", "9-to-5 be like '{}'", "Zoom meeting: '{}'"],
    "food": ["Me looking at food: '{}'", "When you're hungry and see '{}'", "That first bite: '{}'"],
    "default": ["That moment when '{}'", "POV: '{}'", "Meme logic: '{}'", "Relatable? '{}'", "Plot twist: '{}'"]
}

# Keyword matching
def detect_topic(text):
    text = text.lower()
    if any(kw in text for kw in ["school", "exam", "teacher", "class"]): return "school"
    if any(kw in text for kw in ["sleep", "nap", "tired", "bed"]): return "sleep"
    if any(kw in text for kw in ["work", "meeting", "boss", "deadline"]): return "work"
    if any(kw in text for kw in ["food", "eat", "hungry", "pizza"]): return "food"
    return "default"

topic = detect_topic(meme_line)
template = random.choice(humor_templates[topic])

# Fallback if line is blank
if not meme_line:
    meme_line = "life hit you with a plot twist 😩"
    template = "POV: '{}'"

caption = template.format(meme_line)

# ------------------------
# Show Meme + Caption
# ------------------------
plt.figure(figsize=(10, 6))
plt.imshow(img)
plt.axis("off")
plt.title(caption, fontsize=12)
plt.tight_layout()
plt.show()

# ------------------------
# Terminal Print
# ------------------------
print("🧠 OCR Extracted Line:", meme_line)
print("🎯 Detected Topic:", topic)
print("😂 Generated Caption:")
print(caption)
