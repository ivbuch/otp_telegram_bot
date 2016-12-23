Telegram Bot for generating one-time passwords based on counter algorithm

To run application in docker container:

* build docker image

::

    docker build -t "ivbuch/otp_bot" . 

* run docker container

::
  
    docker run -t "ivbuch/otp_bot" -bot TOKEN  -secret BASE_32_SECRET_KEY -chat CHAT_ID 

where you provide:
 
 TOKEN - token of your bot which you want to use
 BASE_32_SECRET_KEY - secret key
 CHAT_ID - chat id. Only on request from that chat bot generates passwords


After running container you send a bot a command (default is "more") and bot replies with your password.
You can also set counter of your secret key and command you send to bot.
