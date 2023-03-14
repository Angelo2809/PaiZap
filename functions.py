import openai


def chat(mensagem):
    API_KEY = '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'

    openai.api_key = API_KEY

    model_engine = 'text-davinci-003'

    prompt = mensagem

    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        temperature = 0.7
    )

    response = completion.choices[0].text

    return response