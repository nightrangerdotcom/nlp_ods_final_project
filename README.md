# NLP ODS Course 2023: Final Project
## Text to Image Search using CLIP model


### How to Deploy & Host

To deploy & host a model, I use Streamlit + Yandex Cloud. 
Short flow description with relevant commands: 

1) Create docker image using Dockerfile specified in this repository: 

```
# check that your dir contains Dockerfile from the root dir

docker build . -t t2i_streamlit:v1
```

2) Then, you can run docker container locally: 
```
# check that you've already created docker image from step-1

docker run -it -d --rm -p 8501:8501 --platform linux/amd64 t2i_streamlit:v1

# if it's up, then you need to paste 'localhost:8501' in your browser.
```

3) ... but I decided to host my solution using Yandex Cloud's vurtual machine, so you can just follow [this link](http://84.201.128.137:8501).

Important note:
