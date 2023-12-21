FROM --platform=linux/amd64 python:3.9-slim 

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /st_app

COPY app.py app.py
COPY load_data.py load_data.py
COPY requirements.txt requirements.txt
COPY search.py search.py
COPY emojibest_com_AnimatedSticker.gif emojibest_com_AnimatedSticker.gif

RUN pip3 install --default-timeout=100 -r requirements.txt
RUN python3 load_data.py

EXPOSE 8501
ENTRYPOINT [ "streamlit", "run" ]
CMD [ "app.py", "--server.headless", "true", "--server.fileWatcherType", "none", "--browser.gatherUsageStats", "false"]
