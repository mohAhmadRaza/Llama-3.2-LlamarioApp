import streamlit as st
import base64
from groq import Groq
from PIL import Image

st.markdown(
    """
    <style>
    .stApp {
        background-color: #87CEFA;  /* Change this to your desired color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize the Groq client with your API key
client = Groq(api_key="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")
st.title("Llamario 🦙")
st.markdown("### AI App using Llama 3.2 11b and Llama 3-8b Models for Image Processing and Content Generation 🤖✨")

# Function to convert uploaded image to Data URL
def convert_image_to_data_url(image_file):
    image_bytes = image_file.read()
    mime_type = image_file.type
    base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
    return f"data:{mime_type};base64,{base64_encoded}"


st.header("📈 Process An Image Here 📈")
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="image_uploader")

if uploaded_image is not None:
    data_url = convert_image_to_data_url(uploaded_image)
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Make a request to the Groq model with the Data URL
    completion = client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {"type": "image_url", "image_url": {"url": data_url}}
                ]
            },
            {"role": "assistant", "content": ""}
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    response = completion.choices[0].message

    # Generate a detailed description using Llama 3-8b model
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'We are giving you a string. This string contains the short description of a processed image. Your task is to convert this into a well-formed and detailed description. The string is: "{response}".',
            }
        ],
        model="llama3-8b-8192",
    )

    st.success(chat_completion.choices[0].message.content)


def GenerateResponse(topic):
    st.subheader(f'✨Content On {topic}')

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""
                            You are an AI content creator tasked with generating a well-formatted article based on the selected topic. The article should include clear headings, subheadings, and well-structured paragraphs.

                            ## Topic: {topic}

                            Please provide an in-depth exploration of the topic, including:
                                
                            1. **Introduction**: A brief overview of the topic, its significance, and what the reader can expect to learn from this article.

                            2. **Main Points**: Divide the main content into sections with appropriate headings. Each section should cover a key aspect of the topic.

                            3. **Examples**: Include specific examples to illustrate the points made. These examples should be relevant and help in understanding the topic better.

                            4. **Conclusion**: Summarize the main points discussed and provide final thoughts or actionable insights for the reader.

                            Ensure that the writing is clear, engaging, and informative. The structure should be easy to follow, with a logical flow from one section to the next. Use bullet points or numbered lists where appropriate to enhance readability.
                            """,
            }
        ],
        model="llama3-8b-8192",
    )

    # Display the detailed description
    st.markdown(chat_completion.choices[0].message.content)


st.markdown("---")  # You can also use st.markdown("***")

st.header("📷 Get Content For Social Media 📷")
st.write("These are the sample topics. You can choose from here as well as from your own mindset!!")

topics_message = """
1. Health and Fitness 💪  
2. Personal Finance 💰  
3. Travel Destinations ✈️  
4. Technology Trends 📱  
5. Sustainable Living 🌱  
6. Food Recipes 🍽️  
7. Fashion and Style 👗  
8. Mental Health Awareness 🧠  
9. Home Improvement 🏡  
10. Parenting Tips 👶  
11. Career Development 📈  
12. Entrepreneurship 🚀  
13. Entertainment and Movies 🎬  
14. Photography Tips 📷  
15. Gaming Insights 🎮  
16. Science and Innovation 🔬  
17. Relationships and Dating ❤️  
18. Social Media Strategies 📊  
19. DIY Projects 🔨  
20. Cultural Awareness 🌍  
"""
st.markdown(topics_message)

# Get user input for the selected topic
selected_topic = st.text_input("Enter Any Topic")

if selected_topic: 
   GenerateResponse(selected_topic)
