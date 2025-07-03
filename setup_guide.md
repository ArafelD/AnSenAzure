# Guia de Configuração e Uso

Este guia detalha como configurar seu ambiente e executar os exemplos de código fornecidos neste repositório.

## Pré-requisitos

Antes de começar, certifique-se de ter:

1.  **Uma conta Azure ativa**: Você precisará de uma assinatura Azure para criar os recursos necessários.
2.  **Recursos do Azure AI**: Crie os seguintes recursos no portal Azure:
    *   **Serviço de Fala (Speech Service)**: Para as funcionalidades de fala para texto e texto para fala. Anote sua `Chave de Assinatura` e `Região`.
    *   **Serviço de Linguagem (Language Service)**: Para as funcionalidades de processamento de linguagem natural, como detecção de idioma. Anote sua `Chave de Assinatura` e `Endpoint`.
3.  **Python 3.8+**: Certifique-se de ter o Python instalado em sua máquina.
4.  **pip**: O gerenciador de pacotes do Python.

## Configuração do Ambiente

1.  **Clone o repositório**:

    ```bash
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    cd SEU_REPOSITORIO
    ```

2.  **Crie um ambiente virtual (recomendado)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3.  **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração das Credenciais

Os exemplos de código (`src/speech_to_text.py`, `src/text_to_speech.py`, `src/language_detection.py`) contêm placeholders para suas chaves e endpoints do Azure. Você precisará substituí-los pelas suas credenciais reais.

*   **Para Speech Studio (speech_to_text.py e text_to_speech.py)**:

    Substitua `"YOUR_SPEECH_KEY"` e `"YOUR_SERVICE_REGION"` pelos valores obtidos do seu recurso de Serviço de Fala no Azure.

*   **Para Language Studio (language_detection.py)**:

    Substitua `"YOUR_LANGUAGE_KEY"` e `"YOUR_LANGUAGE_ENDPOINT"` pelos valores obtidos do seu recurso de Serviço de Linguagem no Azure.

## Executando os Exemplos

### Fala para Texto (Speech-to-Text)

Para executar o exemplo de fala para texto:

```bash
python src/speech_to_text.py
```

Fale algo no seu microfone quando solicitado.

### Texto para Fala (Text-to-Speech)

Para executar o exemplo de texto para fala:

```bash
python src/text_to_speech.py
```

Digite o texto que você deseja que seja sintetizado em fala.

### Detecção de Idioma (Language Detection)

Para executar o exemplo de detecção de idioma:

```bash
python src/language_detection.py
```

O script irá processar os textos predefinidos e exibir o idioma detectado.

## Próximos Passos

Explore a documentação oficial do Azure para Speech Studio e Language Studio para aprofundar seus conhecimentos e experimentar outras funcionalidades.

