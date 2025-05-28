# Solar Industry AI Assistant

This tool analyzes rooftop satellite images to assess their solar panel installation potential using OpenAI Vision models.

## 🌐 Features

- Image upload and analysis
- Roof suitability and energy potential evaluation
- Installation and ROI recommendation

## 🛠 Setup Instructions

1. Clone or unzip this project
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key in `utils.py`:
   ```python
   openai.api_key = "your_api_key_here"
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

## 📁 Example

Upload any rooftop image from Google Maps or satellite view to test.

## 🚀 Future Improvements

- Automatic ROI calculators based on region
- Integration with solar panel databases
- Deployment to Hugging Face Spaces
