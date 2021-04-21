FROM nginx:1.19.10

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/streamlit.conf /etc/nginx/conf.d/

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install python3 python3-pip python3-dev libpq-dev -y
RUN pip3 install pipenv

WORKDIR /app
COPY . /app
RUN cp .streamlit/config-prod.toml .streamlit/config.toml
RUN python3 -m pipenv install --system --deploy
RUN chmod 755 nginx/run.sh

ENV PORT=80
EXPOSE 80

CMD ["nginx/run.sh"]