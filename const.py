TOKEN = ''

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'  # для личного пользования, а вебхукис для массового

SEND_METH = 'sendMessage'
MY_ID = 

UPDATE_ID_FILE_PATH = 'update_id.txt'
with open(UPDATE_ID_FILE_PATH) as file:
    data = (file.readline())
    if data:
        data = int(data)
    UPDATE_ID = data

WEATHER_TOKEN = ''
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
