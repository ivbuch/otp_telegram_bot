FROM python:3-onbuild
WORKDIR "/usr/src/app/otp_bot"
ENTRYPOINT [ "python", "./bot.py"]
