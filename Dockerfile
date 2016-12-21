FROM python:3-onbuild
WORKDIR /usr/src/app/testbot
ENTRYPOINT [ "python", "./bot.py"]
