FROM python:3.5

# Copy project source files into the container
COPY app /deploy

# Tell docker which directory inside of the container to run commands in
WORKDIR /deploy

## Install dependencies
RUN pip install pipenv
# Note: you can use --system flag on pipenv to install the deps to the _host_
#   instead of into a virtualenv. This feature was create with docker in mind.
#   See https://docs.pipenv.org/advanced.html#deploying-system-dependencies.
RUN pipenv install --system

# Set environment variables inside the container
ENV FLASK_APP app/app.py

# The app will run in the container on port 5000, need to expose that port
EXPOSE 5000

# Start the gunicorn web server with our app
CMD ["gunicorn", "--config", "gunicorn_config.py", "--log-file", "-". "-w", "4", "src.app:app"]
# ENTRYPOINT ["flask", "run"]
