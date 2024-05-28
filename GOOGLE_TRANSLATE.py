import pandas as pd
from googletrans import Translator
import time

# Sample DataFrame
df = pd.DataFrame({
    'Names': ['John', 'Alice', 'Bob']
})

# Function to translate names from English to Telugu with retry mechanism
def translate_to_telugu(name):
    translator = Translator()
    max_retries = 5
    for _ in range(max_retries):
        try:
            translation = translator.translate(name, src='en', dest='te')
            return translation.text
        except AttributeError as e:
            print(f"Failed to retrieve TKK code. Retrying... Error: {e}")
            time.sleep(2)  # Wait for 2 seconds before retrying
    print("Translation failed after multiple attempts.")
    return None  # Return None if translation fails

# Apply translation function to the 'Names' column
df['Telugu_Names'] = df['Names'].apply(translate_to_telugu)

# Display the DataFrame with translated names
print(df)
