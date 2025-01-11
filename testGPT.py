from openai import OpenAI

client = OpenAI(
  api_key="REDACTED"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {
        "role": "developer", 
        "content": "You are classifying group chat messages as either 'Proactive' or 'Reactive' on the nature of the content. Any message that seems to be providing unseen content and insights to the chat should be classified as Proactive. Some pre-processing has been done such that images and vidoes have been replaced with the text [IMAGE/VIDEO]. Images (NOT EMOJIS) should almost always be considered proactive when some other supporting content is provided (brief captions / text ). Try think about wether or not it seems as though a message is a direct response to someone's previous content (these types of messages are reactive!). Remember, proactive / reactive is not about the tone of the message or if it's 'uplifting' it's only about proactivity in terms of content generation. Reply with only 1 word."
    },
    {
        "role": "user", 
        "content": "[IMAGE/VIDEO] Hello family, ... and I went down to brighton this weekend"
    }
  ]
)

print(str(completion.choices[0].message).split("content='")[1].split("'")[0])

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {
        "role": "developer", 
        "content": "You are classifying group chat messages as either 'Proactive' or 'Reactive' on the nature of the content. Any message that seems to be providing unseen content and insights to the chat should be classified as Proactive. Some pre-processing has been done such that images and vidoes have been replaced with the text [IMAGE/VIDEO]. Images (NOT EMOJIS) should almost always be considered proactive when some other supporting content is provided (brief captions / text ). Try think about wether or not it seems as though a message is a direct response to someone's previous content (these types of messages are reactive!). Remember, proactive / reactive is not about the tone of the message or if it's 'uplifting' it's only about proactivity in terms of content generation. Reply with only 1 word."
    },
    {
        "role": "user", 
        "content": "65 and going strong 💪 congrats team"
    }
  ]
)

print(str(completion.choices[0].message).split("content='")[1].split("'")[0])


completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {
        "role": "developer", 
        "content": "You are classifying group chat messages as either 'Proactive' or 'Reactive' on the nature of the content. Any message that seems to be providing unseen content and insights to the chat should be classified as Proactive. Some pre-processing has been done such that images and vidoes have been replaced with the text [IMAGE/VIDEO]. Images (NOT EMOJIS) should almost always be considered proactive when some other supporting content is provided (brief captions / text ). Try think about wether or not it seems as though a message is a direct response to someone's previous content (these types of messages are reactive!). Remember, proactive / reactive is not about the tone of the message or if it's 'uplifting' it's only about proactivity in terms of content generation. Reply with only 1 word."
    },
    {
        "role": "user", 
        "content": "[GIF/STICKER] [GIF/STICKER] ..."
    }
  ]
)

print(str(completion.choices[0].message).split("content='")[1].split("'")[0])



completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {
        "role": "developer", 
        "content": "You are classifying group chat messages as either 'Proactive' or 'Reactive' on the nature of the content. Any message that seems to be providing unseen content and insights to the chat should be classified as Proactive. Some pre-processing has been done such that images and vidoes have been replaced with the text [IMAGE/VIDEO]. Images (NOT EMOJIS) should almost always be considered proactive when some other supporting content is provided (brief captions / text ). Try think about wether or not it seems as though a message is a direct response to someone's previous content (these types of messages are reactive!). Remember, proactive / reactive is not about the tone of the message or if it's 'uplifting' it's only about proactivity in terms of content generation. Reply with only 1 word."
    },
    {
        "role": "user", 
        "content": "Thank you for the birthday messages family!! Special shout-out to ... for sending me 2 cards. Each were dearly appreciated. [IMAGE/VIDEO] Birthday dinner"
    }
  ]
)

print(str(completion.choices[0].message).split("content='")[1].split("'")[0])





completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {
        "role": "developer", 
        "content": "You are classifying group chat messages as either 'Proactive' or 'Reactive' on the nature of the content. Any message that seems to be providing unseen content and insights to the chat should be classified as Proactive. Some pre-processing has been done such that images and vidoes have been replaced with the text [IMAGE/VIDEO]. Images (NOT EMOJIS) should almost always be considered proactive when some other supporting content is provided (brief captions / text ). Try think about wether or not it seems as though a message is a direct response to someone's previous content (these types of messages are reactive!). Remember, proactive / reactive is not about the tone of the message or if it's 'uplifting' it's only about proactivity in terms of content generation. Reply with only 1 word."
    },
    {
        "role": "user", 
        "content": "... because whoever they get will miss out At Christmas and that won’t work x"
    }
  ]
)

print(str(completion.choices[0].message).split("content='")[1].split("'")[0])


