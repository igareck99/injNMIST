import telebot
from flask import request
from app import app
from res_im import *
from cv2 import imread,IMREAD_GRAYSCALE
from keras.models import load_model


token = '1640615902:AAE2ahiOEmr5Se2URoLDYO4WF_k5eWsx0nM'
bot = telebot.TeleBot(token)


@app.route('/', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте. Пришлите фотографию')

@bot.message_handler(func=lambda message: True, content_types=['photo'])
def start(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'photo.png'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    model_load = load_model('lenet.h5')
    resize_image(input_image_path='photo.png',
                 output_image_path='caterpillar_small.png',
                 size=(28, 28))
    img = imread('caterpillar_small.png', IMREAD_GRAYSCALE)
    output = img.copy()
    img = img.reshape(-1, 28, 28, 1)
    img = img.astype('float32')
    y_pred = model_load.predict_classes(img)
    bot.reply_to(message, "Метка предсказанная {}".format(str(y_pred[0])))