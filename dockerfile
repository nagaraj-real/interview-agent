FROM python:3.12.4

RUN apt update && apt install git -y

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY pyproject.toml .

COPY ./agentbuilder ./agentbuilder

RUN pip install .

COPY ./start-gradio-ui.sh ./log_config.yml README.md .

EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["sh","-c","./start-gradio-ui.sh"]
