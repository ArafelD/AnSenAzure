
import azure.cognitiveservices.speech as speechsdk

# This example requires the Speech SDK as listed in the setup section.

# Please replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "YOUR_SPEECH_KEY", "YOUR_SERVICE_REGION"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# The default language for the specified voice.
speech_config.speech_synthesis_voice_name = 'pt-BR-FranciscaNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Get text from the console and synthesize to the default speaker.
print("Digite o texto que deseja sintetizar:")
text = input()

result = speech_synthesizer.speak_text_async(text).get()

# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Síntese de fala concluída para o texto [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Síntese de fala cancelada: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Detalhes do erro: {}".format(cancellation_details.error_details))
        print("Você definiu a chave de recurso e a região da fala?")


