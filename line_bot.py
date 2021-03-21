# -*- coding: utf-8 -*-
"""line_bot

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i3lqxXYJM9PTxQ6a7y8XQh6WFmVB-ZNc
"""

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import pya3rt

app = Flask(__name__)

line_
bot_api = LineBotApi("A4IsKYRZAeC+vuLkL5jL81bbC2/6f7K2kgsWyzDqGj2BUSMH3JGMI\
yRSQms/Nz59WZjH/aCKEaegsjamR2/881YjxROP1ddeO/teqNEvaEgrcjkzdn/7ARO9DBWk/UFCFF1L\
veZYMpoEnWZ1yG2vagdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler('8cd39fed484ff78b5c906f4721944392')

@app.route("/callback", methods=['POST'])
def callback():
  signature = request.headers["X-Line-Signature"]
  body = request.get_data(as_text=True)

  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)

  return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  ai_message = talk_ai(event.message.text)
  line_bot_api.reply_message(event.reply_token, TextSendMessage(text=ai_message))

def talk_ai(word):
  apikey = "DZZwt98DRyDjksrlHMjDHt7QPaOrFfpa"
  client = pya3rt.TalkClient(apikey)
  reply_message = client.talk(word)
  return reply_message['results'][0]['reply']

if __name__ == '__main__':
  app.run()