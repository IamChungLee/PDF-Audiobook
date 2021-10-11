from google.cloud import texttospeech
import PyPDF2


#USE PyPDF2 to GRAB TEXT FROM PDF FILE-------------------------------------------------------------------

pdf_object = open('sample.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_object)

total_pages = pdf_reader.numPages

text = ""
for page in range(total_pages):
    page_object = pdf_reader.getPage(page)
    text += page_object.extractText()




#USE GOOGLE TEXT TO SPEECH API---------------------------------------------------------------------

client = texttospeech.TextToSpeechClient()

#TODO 1: Grab the text to be audiolized
text_synthesis = texttospeech.SynthesisInput(text=text)


#TODO 2:select the voice with language and gender params
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)


#TODO 3: select audio type MP3
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)



#TODO 4: Using all three, use the api request
response = client.synthesize_speech(
    input=text_synthesis, voice=voice, audio_config=audio_config
)

# TODO 5: Finally save the audio file:
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')