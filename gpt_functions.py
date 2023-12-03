from openai import OpenAI

def generate_prompt(Hotels, Hotel_A, Hotel_B, initial_prompt=''):
  result = 'Name Hotel_A: {Hotel_A} \nHotel_A reviews:\n'.format(Hotel_A=Hotel_A)
  for i, reviews in enumerate(Hotels[Hotel_A]['Reviews']):
    result += '{i}) '.format(i=i+1) + reviews['Comment'] +'\n'
  result += '-------------------------\n'
  result += 'Name Hotel_B: {Hotel_B} \nHotel_B reviews:\n'.format(Hotel_B=Hotel_B)
  for i, reviews in enumerate(Hotels[Hotel_B]['Reviews']):
    result += '{i}) '.format(i=i+1) + reviews['Comment'] +'\n'

  return initial_prompt + result

def build_client(api_key):
  return OpenAI(api_key=api_key)

def generate(client, prompt):
  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": prompt,
          }
      ],
      model="gpt-3.5-turbo",
  )
  return chat_completion.choices[0].message.content