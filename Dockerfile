FROM python:3
ADD factorial-digits.py /
ENTRYPOINT ["python3", "./factorial-digits.py"]