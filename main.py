import requests
import json
import time
from pprint import pprint
import const


def answer_user_bot(data):
    data = {'chat_id': const.MY_ID,
            'text': data
            }
    url = const.URL.format(
        token=const.TOKEN,
        method=const.SEND_METH
    )
    response = requests.post(url, data=data)
    # print(response)


def parse_weather_data(data):
    for elem in data['weather']:
        weather_state = elem['main']
    temp = round(data['main']['temp'] - 273.15, 2),
    feels_like = round(data['main']['feels_like'] - 273.15, 2),
    city = data['name']
    country = data['sys']['country']

    msg = f'the weather in {city}: Temp is {temp}, feels like {feels_like}, State is {weather_state}, country is {country}'
    return (msg)
    # pprint(msg)


def get_weather(location):
    url = const.WEATHER_URL.format(city=location, token=const.WEATHER_TOKEN)
    response = requests.get(url)
    if response.status_code != 200:
        return 'city not found'
    data = json.loads(response.content)

    # pprint(data)
    return parse_weather_data(data)


def get_message(data):
    return data['message']['text']


def save_update_id(update):
    with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
        const.UPDATE_ID = update['update_id']
    return True


def main():
    while True:
        url = const.URL.format(token=const.TOKEN, method=const.UPDATE_METH)
        content = requests.get(url).text
        data = json.loads(content)
        result = data['result'][::-1]
        needed_part = None
        for elem in result:
            if elem['message']['chat']['id'] == const.MY_ID:
                needed_part = elem
                break
        #pprint(elem)
        if const.UPDATE_ID != needed_part['update_id']:
            # print(const.UPDATE_ID)

            message = get_message(needed_part)
            msg = get_weather(message)
            answer_user_bot(msg)

            save_update_id(needed_part)

        time.sleep(1)
        # break
    # pass


if __name__ == '__main__':
    main()

# url = URL.format(TOKEN=TOKEN, method=updates)
# response = requests.get(url)
# data = {
#    'chat_id':'203114139',
#    'text':'hello from bot'
# }
# url = URL.format(TOKEN=TOKEN, method=send)
# response=requests.post(url, data=data)
# print(response.text)

# print(response.text)
# print(type(response.text))
# json_content = json.loads(response.text)
# print(json_content)
# print(type(json_content))

# print(dir(response))

# json.loads()
# json.dumps()

# json.load()
# json.dump()
