FROM python:3.7
RUN pip3 install --upgrade pip

ENV APP/app

RUN mkdir ${APP}
ENV PYTHONPATH="$PYTHONPATH:/app/Text-Summarization-Using-T5"

COPY . ${APP}/Text-Summarization-Using-T5/

WORKDIR ${APP}/Text-Summarization-Using-T5/

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python","backend/services/text_summarization/api/app.py"]