# AI Implementation Guide

This document outlines the technical details for integrating AI functionality into the project. It provides instructions on the model, API, and implementation strategies to replicate the "Nutritional Analysis" feature.

## 1. Core AI Specifications

*   **Model:** `gemini-2.5-flash`
    *   **Capabilities:** Multimodal (Text + Vision). Optimized for speed and cost-efficiency.
*   **Provider:** Google DeepMind (via Gemini API).
*   **SDK Library:** `google-genai`
    *   **Version:** `>=1.0.0` (Note: This is the newer SDK, distinct from the legacy `google-generativeai`).
    *   **Language:** Python.

## 2. Authentication & Configuration

The application requires a valid API key from Google AI Studio.

*   **Environment Variable:** `GEMINI_API_KEY`
*   **Client Initialization:**

```python
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
```

## 3. Implementation Details

The core functionality is an `analyze` feature that accepts an image and returns structured JSON data.

### 3.1 Input Handling
*   Accepts image files (JPEG/PNG).
*   Reads the image as raw bytes for transmission to the API.

### 3.2 Prompt Engineering
*   **Source File:** The prompt is loaded from a text file to allow for easy iteration without changing code.
*   **Strategy:**
    *   **Persona:** "Data Entry Specialist and Clinical Nutritionist".
    *   **Tasks:** Extract UPC/EAN, OCR Nutrition Label, Perform Nutritional Rating.
    *   **Output Constraint:** Strict JSON only. No markdown. No conversation.
*   **Example Prompt:** See `prompts_examples/learning.txt`.

### 3.3 API Call
To prevent blocking the main thread (especially in async frameworks like FastAPI), the synchronous SDK call should be wrapped in `asyncio.to_thread`.

**Code Example:** See `python_tool/ai_example.py` for a complete implementation.

```python
response = await asyncio.to_thread(
    client.models.generate_content,
    model='gemini-2.5-flash',
    contents=[
        prompt_text,
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")
    ]
)
```

### 3.4 Response Parsing
The raw text response from the model must be cleaned and parsed:
1.  **Strip Markdown:** Remove ```json` code blocks if present.
2.  **Parse JSON:** Convert the string to a Python dictionary.
3.  **Error Handling:** Gracefully handle `json.JSONDecodeError` if the model fails to output valid JSON.

## 4. Developer Checklist

To replicate this feature in a new environment:

1.  [ ] **Google Cloud/AI Studio:** Create a project and enable the Gemini API.
2.  [ ] **API Key:** Generate an API key and add it to `.env` as `GEMINI_API_KEY`.
3.  [ ] **Dependencies:** Install the SDK: `pip install google-genai`.
4.  [ ] **Prompt File:** Copy `prompts_examples/learning.txt` to your project's `prompts/` directory.
5.  [ ] **Code:** Use `python_tool/ai_example.py` as a reference for the integration logic.
