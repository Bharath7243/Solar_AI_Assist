import openai
import base64

openai.api_key = "YOUR_OPENAI_API_KEY"

def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode("utf-8")

def analyze_rooftop(image_file):
    image_base64 = encode_image(image_file)
    prompt = (
        "You are a solar installation expert. Analyze this rooftop image and return:\n"
        "- Roof suitability (flat, tilted, shaded)\n"
        "- Estimated usable area (in m²)\n"
        "- Recommended number of solar panels\n"
        "- Expected energy output per year (kWh)\n"
        "- Estimated ROI and payback period\n"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "You are a solar industry assistant."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
                ]
            }
        ],
        max_tokens=1000
    )
    return response['choices'][0]['message']['content']

def format_results(response_text):
    return f"### 📊 Analysis Result\n{response_text}"
