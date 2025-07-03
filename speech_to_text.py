import azure.cognitiveservices.speech as speechsdk

# This example requires the Speech SDK as listed in the setup section.

# Please replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "YOUR_SPEECH_KEY", "YOUR_SERVICE_REGION"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a speech recognizer for the specified language, using the default microphone as audio input.
# Replace "en-US" with the language you want to recognize, e.g. "pt-BR" for Brazilian Portuguese.
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="pt-BR")

print("Fale algo no seu microfone...")
result = speech_recognizer.recognize_once_async().get()

# Checks result.
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Reconhecido: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("Não foi possível reconhecer a fala: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Reconhecimento cancelado: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Detalhes do erro: {}".format(cancellation_details.error_details))
        print("Você definiu a chave de recurso e a região da fala?")


