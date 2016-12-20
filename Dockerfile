FROM python:2-onbuild
WORKDIR /usr/src/app/testbot
ENTRYPOINT [ "python", "./bot.py"]
