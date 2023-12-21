# NLP ODS Course 2023: Final Project
## Text to Image Search using CLIP model

______
### General
Author: Victoria Frolova

Course: [link](https://ods.ai/tracks/nlp-course-autumn-23)

Lecturer: Valentin Malykh

______
### Data

Let's talk about [dataset with images](https://unsplash.com/data) used in this project. It's calles The Unsplash Dataset. There are Lite&Full versions of this dataset. Here I use the first one because it's smaller. 

If you want to know more about this dataset, you can study [this link](https://github.com/unsplash/datasets). In short, Lite version contains ~25,000 animals/nature-themed images **(take it into account during the search process!)** that is around ~1.9GB according to my laptop stats.

______
### How to Deploy & Host

To deploy & host a model, I use Streamlit + Yandex Cloud. You also need Docker if you want to run & host it locally.
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

# if it's up, then you need to paste 'localhost:8501' in your browser & enjoy the results.
```

3) ... but I decided to host my solution using Yandex Cloud's virtual machine, so you can skip steps 1-2 & just follow [this link](http://84.201.128.137:8501) (if it doesn't work, then it means right now I don't host my solution – I need to pay for this:) ).

Important notes: 

1) If you want to run container locally, first ask yourself what the architecture of your machine is. Maybe, you'll need to change the platform specified in Dockerfile & docker run command to avoid problems.   

2) As I build a search system, there must be a folder with images. Actually, the images are downloaded every time you run a new container & then their embeddings are being created. => Please, keep in mind, that it takes some time to build a container & prepare the web interface in your browser. 

______