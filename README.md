# NLP ODS Course 2023: Final Project
## Text to Image Search using CLIP model

______
### General
Author: Victoria Frolova

Course: [link](https://ods.ai/tracks/nlp-course-autumn-23)

Lecturer: Valentin Malykh

______
### Goal

**What?**

1) To build text2image search system;
2) To deploy & host it.

**Why?**

1) Search systems are widely used in many retail companies. Adding image modality to a classical search system could improve product metrics;

2) My personal interests such as: 

2.1) To know how ML/DL solutions can be integrated using different instruments (VM, Docker, Streamlit);

2.2) To know more about image retrieval systems & multimodal models such as CLIP because it's really a well-known model.

______
### Data

Let's talk about [dataset with images](https://unsplash.com/data) used in this project. It's called The Unsplash Dataset. There are Lite&Full versions of this dataset. Here I use the first one because it's smaller. 

If you want to know more about this dataset, you can study [this link](https://github.com/unsplash/datasets). In short, Lite version contains ~25,000 animals/nature-themed images **(take it into account during the search process!)** that is around ~1.9GB according to my laptop stats.

[In process] Now I'm working on integration of another dataset which is called Fashion Product Images (Small). It contains ~44.000 clothes-themed images that is around ~570MB according to my laptop stats (=> lower-quality & smaller images than in the previously described dataset). Practically, this dataset seems to be more useful in terms of developing the search system because of two reasons. 1) Such systems are widely used in different retail companies (Ozon, Amazon, Lamoda, Wildberries etc); 2) Actually, in real life we often deal with small/low-quality pictures, so it's important to have a search system being able to work with such restrictions.

______
### Model

I decided to use CLIP model created by Open AI for Text-to-Image search. It's a famous multimodal model (because here we are dealing with text & image modalities) based on contrastive learning. Its architecture is depicted below ([src](https://github.com/openai/CLIP)):

![CLIP scheme](https://github.com/openai/CLIP/raw/main/CLIP.png)

In my project I use [this version of CLIP](https://huggingface.co/sentence-transformers/clip-ViT-B-32-multilingual-v1). Its advantages are 1) it's multi-lingual (supports 50+ languages including English, Russian, German, Chinese, Spanish); 2) it's distilled => smaller size but high quality comparable to the original model.

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

3) As fas as my code is integrated with streamlit framework, all the code pipeline is presented in Dockerfile (which files to run & in what order).

______