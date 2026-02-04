import os
import asyncio
import json
from google import genai
from google.genai import types

# Initialize the client
# Ensure GEMINI_API_KEY is set in your environment variables
# In a production environment, you might want to initialize this lazily or in a startup event.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def analyze_image(image_bytes: bytes, prompt_path: str = "prompts_examples/learning.txt") -> dict:
    """
    Analyzes an image using the Gemini 2.5 Flash model.

    Args:
        image_bytes: The raw bytes of the image file (JPEG/PNG).
        prompt_path: Path to the text file containing the prompt.

    Returns:
        A dictionary containing the parsed JSON response from the model.
    """

    # Load the prompt
    try:
        with open(prompt_path, "r") as f:
            prompt_text = f.read()
    except FileNotFoundError:
        return {"error": f"Prompt file not found at {prompt_path}"}

    # Prepare the API call
    # We use asyncio.to_thread to avoid blocking the event loop (important for FastAPI/async apps)
    try:
        response = await asyncio.to_thread(
            client.models.generate_content,
            model='gemini-2.5-flash',
            contents=[
                prompt_text,
                types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")
            ]
        )
    except Exception as e:
        return {"error": f"API call failed: {str(e)}"}

    # Parse the response
    try:
        response_text = response.text.strip()

        # Clean potential markdown formatting (e.g. ```json ... ```)
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        elif response_text.startswith("```"):
             response_text = response_text[3:]

        if response_text.endswith("```"):
            response_text = response_text[:-3]

        response_text = response_text.strip()

        # Parse JSON
        result = json.loads(response_text)
        return result

    except json.JSONDecodeError:
        # Handle cases where the model returns invalid JSON
        return {
            "error": "Failed to parse JSON response",
            "raw_response": response.text if response else "No response"
        }
    except Exception as e:
        return {"error": f"Unexpected error during parsing: {str(e)}"}

# Example usage (if running directly)
if __name__ == "__main__":
    # This block is for demonstration purposes.
    # In a real app, you would call analyze_image from your API endpoint.
    print("This module provides the 'analyze_image' function.")
    print("Ensure you have 'google-genai' installed and GEMINI_API_KEY set.")
