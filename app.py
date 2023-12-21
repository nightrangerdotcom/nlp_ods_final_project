import base64
from PIL import Image
from io import BytesIO
import streamlit as st
from search import search


st.set_page_config(
    page_title="T2I Search",
    page_icon="✨",
    layout="wide",
)

with st.sidebar:
    # https://discuss.streamlit.io/t/how-to-show-local-gif-image/3408/4

    # """### gif from url"""
    # st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

    # """### gif from local file"""
    finalgif = open("./emojibest_com_AnimatedSticker.gif", "rb")
    contents = finalgif.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    finalgif.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="70">',
        unsafe_allow_html=True,
    )

    st.markdown("<h3> ODS NLP\'23: Final Project </h3>", unsafe_allow_html=True)
    st.markdown("Text2Image Search using CLIP model")
    st.markdown(
        """
        ---
        :orange[**About Author:**]
        
        ✨ Victoria Frolova

        ✨ Contacts:
        """
    )
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("GitHub", "https://github.com/nightrangerdotcom")
    with col2:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/frolova-viktoria/")

    st.markdown(
        """
        ---
        :orange[**About Course:**]

        ✨ Lecturer: Valentin Malykh
        """
    )
    st.link_button("Course Link", "https://ods.ai/tracks/nlp-course-autumn-23")


st.markdown("<h2 style='text-align: center; color: black; font-family: DejaVu Sans Mono'>Search</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    title = st.text_input('Input your text query 👇', 'два lambs')
    number = st.slider("Choose the number of most similar images 👇", 1, 10, value=3)

if title and number:
    with col2:
        images = search(title, number)
        for idx, image in enumerate(images):
            # image = Image.open('beautiful-smooth-haired-red-cat-lies-on-the-sofa-royalty-free-image-1678488026.jpeg')
            st.image(image, caption=f'Image #{idx + 1} for query "{title}"')

            buf = BytesIO()
            imfile = Image.open(image)
            imfile.save(buf, format="JPEG")
            byte_im = buf.getvalue()

            btn = st.download_button(
                label="Download Image ✨",
                data=byte_im,
                file_name=f"query_{title.replace(' ', '_')}_img_{idx + 1}.png",
                mime="image/jpeg",
                )
        