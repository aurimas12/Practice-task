FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt


# ADD test.sh .
# # RUN bash -c "/test.sh"
# CMD [ "/test.sh","test" ]