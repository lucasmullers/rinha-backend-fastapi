FROM python:3.11

# Create a directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN groupadd app && useradd -g app app

# Create the home directory
ENV APP_HOME=/home/app/api
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# Install dependencies
COPY . $APP_HOME
RUN pip install -e .

RUN chown -R app:app $APP_HOME
USER app

# CMD ["uvicorn", "blog.app:app", "--host=0.0.0.0", "--port=8000", "--reload", "--log-level", "debug"]
# CMD ["/bin/bash", "-c", "python3 main.py"]
CMD ["/bin/bash", "-c", "gunicorn main:app -w 2 -k uvicorn.workers.UvicornWorker -b '0.0.0.0:80'"]
