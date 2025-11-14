FROM nikolaik/python-nodejs:python3.10-nodejs19


RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list \
 && sed -i 's|http://deb.debian.org/debian-security|http://archive.debian.org/debian-security|g' /etc/apt/sources.list || true \
 && echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until

# Install ffmpeg
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

CMD bash start