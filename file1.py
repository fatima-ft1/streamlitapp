import streamlit as st
from PIL import Image, ImageFilter

def apply_filter(image, filter_name):
    if filter_name == "Blur":
        return image.filter(ImageFilter.BLUR)
    elif filter_name == "Grayscale":
        return image.convert("L")
    elif filter_name == "Invert":
        return ImageOps.invert(image)
    else:
        return image

def main():
    st.title("Image Processing App")
    st.write("Upload an image and select a filter to apply.")

    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    filter_name = st.selectbox("Select a filter", ["Blur", "Grayscale", "Invert"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        processed_image = apply_filter(image, filter_name)

        st.image(processed_image, caption="Processed Image", use_column_width=True)

if __name__ == "__main__":
    main()
