FROM python:3.10

ENV STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true

EXPOSE 8080
WORKDIR /hcls_demo
COPY . ./

#install all requirements in requirements.txt
RUN pip install -r requirements.txt

# Run the web service on container startup
CMD ["streamlit", "run", "Home.py", "--server.port=8080"]
