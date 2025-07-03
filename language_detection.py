
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Replace with your own subscription key and service region
key = "YOUR_LANGUAGE_KEY"
endpoint = "YOUR_LANGUAGE_ENDPOINT"

# Authenticate the client
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example text for language detection
documents = [
    "Olá, como você está?",
    "Hello, how are you?",
    "Bonjour, comment allez-vous?"
]

response = client.detect_language(documents=documents, country_hint="br")

for doc, detection in zip(documents, response):
    if not detection.is_error:
        print(f"Documento: {doc}\nIdioma detectado: {detection.primary_language.name}\nConfiança: {detection.primary_language.confidence_score:.2f}\n")
    else:
        print(f"Documento: {doc}\nErro: {detection.error.code} - {detection.error.message}\n")


