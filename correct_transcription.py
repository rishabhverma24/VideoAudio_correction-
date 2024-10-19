import openai

def correct_transcription(transcription_text):
    # Set up the Azure OpenAI API key and endpoint
    openai.api_key = "22ec84421ec24230a3638d1b51e3a7dc"  # Update the API key here
    openai.api_base = "https://internshala.openai.azure.com"  # Base URL for Azure
    openai.api_type = "azure"
    openai.api_version = "2024-08-01-preview"  # Use the correct API version

    # Create a request to the Azure OpenAI ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        deployment_id="gpt-4o",  # Use the deployment ID for Azure
        messages=[
            {"role": "system", "content": "You are a transcription fixer."},
            {"role": "user", "content": f"Correct the following transcription:\n{transcription_text}"}
        ],
        max_tokens=1500
    )

    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    # Load the transcription from the file
    with open("transcription.txt", "r") as f:
        transcription = f.read()

    # Correct the transcription
    corrected_transcription = correct_transcription(transcription)

    # Print the corrected transcription to the terminal
    print("Corrected Transcription:")
    print(corrected_transcription)

    # Save the corrected transcription to a new file
    with open("corrected_text.txt", "w") as f:
        f.write(corrected_transcription)
