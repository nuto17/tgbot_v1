import requests

prompt = {
    "modelUri": "gpt://b1gr568vlh0l85uak3os/yandexgpt-lite",
    "completionOptions": {
        "stream": True,
        "temperature": 0.6,
        "maxTokens": "1000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Ты ассистент дроид, способный помочь в галактических приключениях."
        },
        {
            "role": "user",
            "text": "Привет, Дроид! Мне нужна твоя помощь, чтобы узнать больше о Силе. Как я могу научиться ее использовать?"
        },
        {
            "role": "assistant",
            "text": "Привет! Чтобы овладеть Силой, тебе нужно понять ее природу. Сила находится вокруг нас и соединяет всю галактику. Начнем с основ медитации."
        },
        {
            "role": "user",
            "text": "Хорошо, а как насчет строения светового меча? Это важная часть тренировки джедая. Как мне создать его?"
        }
    ]
}
url="https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

headers={
     "Content-Type": "application/json",
    "Authorization": "APi-Key AQVNwjHkC2q66txhFSIzOSBpEYMlKnnDT2s3FlmW"
}

response=requests.post(url,headers=headers,json=prompt)
result= response.text
print(result)