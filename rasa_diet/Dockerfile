FROM python:3.7
RUN useradd -m dockeruser
ADD . /home/dockeruser
WORKDIR /home/dockeruser
RUN pip install --trusted-host pypi.python.org -r requirements.txt && chown dockeruser.dockeruser /home/dockeruser -R
USER dockeruser
EXPOSE 5005
CMD ["rasa", "run", "--enable-api", "-m", "/home/dockeruser/models/nlu-20210326-193310.tar.gz"]
