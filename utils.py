import google.generativeai as genai
from typing import Optional

def generate_motivational_quote(mood: str, api_key: str) -> str:
    """
    Generate a motivational quote using Google's Gemini AI based on the user's mood.
    
    Args:
        mood (str): The user's current mood
        api_key (str): The API key for Google Gemini
        
    Returns:
        str: A motivational quote
    """
    # Configure the Gemini API with the provided key
    genai.configure(api_key=api_key)

    # Select the appropriate model (using gemini-1.5-pro as requested)
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    # Create prompt based on mood
    if mood == "General (No specific mood)":
        prompt = """
        Generate a short, powerful motivational quote that can inspire someone today.
        The quote should be concise (1-3 sentences), impactful, and uplifting.
        Focus on themes like perseverance, growth, or positivity.
        Don't include attribution - just the quote itself.
        Format it nicely with proper capitalization and punctuation.
        """
    else:
        prompt = f"""
        Generate a short, powerful motivational quote for someone who is feeling {mood} today.
        The quote should be concise (1-3 sentences), impactful, and specifically address this emotional state.
        Focus on transforming this feeling into positive action or perspective.
        Don't include attribution - just the quote itself.
        Format it nicely with proper capitalization and punctuation.
        """
    
    # Generate the quote
    try:
        response = model.generate_content(prompt)
        quote = response.text.strip()
        
        # Clean the quote if needed (remove quotation marks if AI added them)
        if quote.startswith('"') and quote.endswith('"'):
            quote = quote[1:-1].strip()
            
        return quote
    except Exception as e:
        # Log the error and raise it for handling in the main app
        print(f"Error generating quote: {str(e)}")
        raise e
