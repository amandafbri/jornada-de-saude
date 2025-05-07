from google import genai
from google.genai import types
import base64

from google.cloud import texttospeech

from configs import PROJECT_ID

client = genai.Client(
      vertexai=True,
      project=PROJECT_ID,
      location="us-central1",
)

def call_gemini(
      model: str,
      system_instructions: str,
      audios: list= [],
      images: list = [],
      pdfs: list = [],
      response_mime_type: str = None,
      response_schema: dict = None
) -> str:

  parts = [types.Part.from_text(text="Conteúdo:")]
  if audios:
    audio_list_obj = [types.Part.from_bytes(mime_type="audio/mp4", data=data) for data in audios]
    parts.extend(audio_list_obj)
  if images:
    image_list_obj = [types.Part.from_bytes(mime_type="image/jpeg", data=data) for data in images]
    parts.extend(image_list_obj)
  if pdfs:
    pdf_list_obj = [types.Part.from_bytes(mime_type="application/pdf", data=data) for data in pdfs]
    parts.extend(pdf_list_obj)
  parts.append(types.Part.from_text(text="Resultado:"))

  contents = [
    types.Content(
      role="user",
      parts=parts
    )
  ]
  generate_content_config = types.GenerateContentConfig(
    temperature = 0.1,
    top_p = 0.95,
    max_output_tokens = 8192,
    response_modalities = ["TEXT"],
    response_mime_type = response_mime_type,
    response_schema = response_schema,
    system_instruction=[types.Part.from_text(text=system_instructions)],
  )
  
  response = client.models.generate_content(
     model = model,
     contents = contents,
     config = generate_content_config)

  return response.text


def text_to_speech(text, output_filename = "output.mp3"):
    """
    Converts text to speech using Google Cloud's Text-to-Speech API.

    Args:
    text: The text to convert to speech.
    output_filename: The name of the output file.
    """

    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request
    voice = texttospeech.VoiceSelectionParams(
        language_code="pt-BR", name="pt-BR-Wavenet-D"
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        #speaking_rate=1.5
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open(output_filename, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f"Audio content written to file {output_filename}")
    
    return output_filename

