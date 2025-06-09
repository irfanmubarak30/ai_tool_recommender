#!/usr/bin/env python
"""
Simple test script to verify Groq API is working
"""
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

def test_groq_connection():
    """Test if Groq API is working properly."""
    try:
        # Get API key
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            print("❌ GROQ_API_KEY not found in environment!")
            return False
            
        print(f"✅ API Key found: {api_key[:10]}...")
        
        # Initialize Groq client
        client = Groq(api_key=api_key)
        
        # Test API call
        print("🔄 Testing Groq API connection...")
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": "Say hello in one sentence."}
            ],
            model="llama-3.1-8b-instant",
            max_tokens=50
        )
        
        print("✅ Groq API test successful!")
        print(f"Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ Groq API test failed: {e}")
        return False

if __name__ == "__main__":
    test_groq_connection()