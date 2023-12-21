"""
reference: 
https://huggingface.co/sentence-transformers/clip-ViT-B-32-multilingual-v1
https://github.com/UKPLab/sentence-transformers/blob/master/examples/applications/image-search/Image_Search-multilingual.ipynb 
"""

import os
import glob
import pickle
from PIL import Image
import streamlit as st
from IPython.display import display
from IPython.display import Image as IPImage

from sentence_transformers import SentenceTransformer, util


@st.cache_data
def general(use_precomputed_embeddings: bool = True):
    """
    function to get embeddings
    """
    model = SentenceTransformer('clip-ViT-B-32-multilingual-v1')

    if use_precomputed_embeddings:
        emb_filename = 'unsplash-25k-photos-embeddings.pkl'
        if not os.path.exists(emb_filename):   # Download dataset if does not exist
            util.http_get('http://sbert.net/datasets/' + emb_filename, emb_filename)

        with open(emb_filename, 'rb') as fIn:
            img_names, img_emb = pickle.load(fIn)
        print("Images:", len(img_names))

    else:
        # For embedding images, we need the non-multilingual CLIP model
        img_model = SentenceTransformer('clip-ViT-B-32')

        img_names = list(glob.glob('unsplash/photos/*.jpg'))
        print("Images:", len(img_names))

        imgs = []
        for file in img_names:
            # to avoid this err:
            # https://stackoverflow.com/questions/29234413/too-many-open-files-error-when-opening-and-loading-images-in-pillow
            temp = Image.open(file)
            keep = temp.copy()
            imgs.append(keep)
            temp.close()
                    
        img_emb = img_model.encode(
            imgs, 
            batch_size=128, 
            convert_to_tensor=True, 
            show_progress_bar=True,
        )

    return model, img_names, img_emb 


def search(query, k: int = 1, use_precomputed_embeddings: bool = True, img_folder: str = 'photos/'):
    """
    search function
    """
    model, img_names, img_emb = general(use_precomputed_embeddings)

    # First, we encode the query (which can either be an image or a text string)
    query_emb = model.encode([query], convert_to_tensor=True, show_progress_bar=False)

    # Then, we use the util.semantic_search function, which computes the cosine-similarity
    # between the query embedding and all image embeddings.
    # It then returns the top_k highest ranked images, which we output
    hits = util.semantic_search(query_emb, img_emb, top_k=k)[0]

    # print("Query:")
    # display(query)
    res = []
    for hit in hits:
        # print(img_names[hit['corpus_id']])
        # display(IPImage(os.path.join(img_folder, img_names[hit['corpus_id']]), width=200))
        res.append(os.path.join(img_folder, img_names[hit['corpus_id']]))
    return res
