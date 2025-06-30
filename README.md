# AI Meme Caption Generator

## Overview
This project generates meme captions without using LLMs! Instead, it uses a smart rule-based approach that analyzes OCR-extracted text from each meme and applies handcrafted humor templates to generate funny, relatable captions.

## Objective
- Simulate AI-powered meme captioning without relying on heavy language models.
- Generate humor using text pattern detection, keywords, and rules.
- Display and annotate meme images with the generated captions.

## Dataset & Inputs
- **Images**: Folder of meme images located at `images/images/`
- **Metadata**: `labels.csv` containing columns like `image_name`, `text_ocr`, and `overall_sentiment`

## Technologies Used
- Python
- pandas, matplotlib, PIL
- Regex and string processing

## How to Run

### 1. File Structure
```
day 9/
  ├── AI Meme Caption Generator.py
  ├── labels.csv
  └── images/
        └── images/
             ├── meme_1.jpg
             ├── meme_2.jpg
             └── ...
```

### 2. Install Requirements
```bash
pip install pandas matplotlib pillow
```

### 3. Run the Script
```bash
python "AI Meme Caption Generator.py"
```

## Workflow
- Load meme metadata from `labels.csv`
- Randomly sample a meme
- Extract meaningful lines from OCR text
- Detect topic category (school, sleep, work, food, etc.)
- Generate captions using predefined humor templates
- Display meme with the caption in matplotlib

## Example Captions
- "POV: sleep level: coma"
- "Corporate life: Zoom fatigue again?"
- "Me in class like ‘what page are we on again?’"

## Future Enhancements
- Add batch caption generation
- Include emoji or text overlay on saved memes
- Allow user-defined templates or themes
