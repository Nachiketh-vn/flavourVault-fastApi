from fastapi import FastAPI, Body
from pydantic import BaseModel
import os
from google import genai

gemini_client = genai.Client(api_key="AIzaSyC--gsEjV_QViU9VLd8u_kum0E8XLqmv2I")

app = FastAPI()

class Dish(BaseModel):
    name: str

@app.post("/get_description")
def read_root(dish: Dish = Body(...)):
    prompt = f"""Generate a professional three-line description for the dish '{dish.name}' suitable for an Indian restaurant menu. Use authentic Indian English and terminology.

    The description MUST:
    - Be EXACTLY three lines long   
    - Use professional, appealing culinary language with Indian terminology
    - Include key ingredients and cooking methods
    - Mention regional origin if relevant (North Indian, South Indian, etc.)
    - Highlight unique flavor profiles or textures using Indian descriptors
    - NOT mention any meat ingredients unless explicitly in the dish name
    - NOT include serving suggestions or pairing recommendations
    - NOT use Western culinary terms when Indian equivalents exist
        - Use Indian context for Indian dishes, only use foreign context if the dish is non-Indian in origin

        RETURN ONLY In THREE-LINE Paragraph DESCRIPTION WITH NO ADDITIONAL TEXT,Line Breaks, SUGGESTIONS, OR COMMENTARY."""
    response = gemini_client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt,
    )
    return {"response": response.text}
