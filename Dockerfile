FROM python:3.9

# Install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Download and install Chromedriver 123 Version
RUN wget -q -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.86/linux64/chromedriver-linux64.zip \
    && unzip /tmp/chromedriver.zip -d /tmp \
    && cp /tmp/chromedriver-linux64/chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip \
    && rm -rf /tmp/chromedriver-linux64 \
    && chmod +x /usr/local/bin/chromedriver

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python","main.py"]