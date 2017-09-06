#FROM clburlison/pylint:py3-wheezy
FROM python:3.6-jessie

RUN apt-get update && \
    apt-get install -y \
    git \
    openssl \
    python3-enchant && \
    pip install --no-cache-dir flake8 flake8-docstrings pylint pyenchant tweepy django django-tastypie
	
WORKDIR /usr/share/battletweets/
ADD . .

#RUN pip install pyenchant
#RUN pip install tweepy
#RUN pip install django
#RUN pip install django-tastypie

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]