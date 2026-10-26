
import streamlit as st
import numpy as np
from PIL import Image, ImageChops

st.set_page_config(
    page_title="ISRO Satellite Data Explorer",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ ISRO Satellite Data Explorer")
st.write(
    "Explore changes between two images of the same area "
    "captured at different times."
)

st.info(
    "This is an educational prototype, not an official ISRO application. "
    "Upload two images to compare them."
)

before_file = st.file_uploader(
    "Upload the earlier image",
    type=["png", "jpg", "jpeg"],
    key="before"
)

after_file = st.file_uploader(
    "Upload the later image",
    type=["png", "jpg", "jpeg"],
    key="after"
)

if before_file is not None and after_file is not None:
    before = Image.open(before_file).convert("RGB")
    after = Image.open(after_file).convert("RGB")

    # Resize the later image to match the earlier image.
    after = after.resize(before.size)

    # Calculate the pixel-by-pixel difference.
    difference = ImageChops.difference(before, after)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Earlier Image")
        st.image(before, use_container_width=True)

    with col2:
        st.subheader("Later Image")
        st.image(after, use_container_width=True)

    st.subheader("Detected Image Differences")
    st.image(difference, use_container_width=True)

    # Calculate an average pixel difference score.
    pixels = np.asarray(difference, dtype=np.float32)
    score = float(pixels.mean() / 255 * 100)

    st.metric(
        label="Average Pixel Difference",
        value=f"{score:.2f}%"
    )

    st.caption(
        "This score measures visual pixel differences. "
        "It does not directly measure actual land-cover change. "
        "For meaningful satellite analysis, images must be "
        "geographically aligned and appropriately processed."
    )

else:
    st.warning(
        "Please upload both an earlier image and a later image "
        "to compare them."
    )
