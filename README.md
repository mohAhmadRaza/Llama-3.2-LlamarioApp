# Llamario 🦙
![Capture](https://github.com/user-attachments/assets/0f1b0277-b930-4596-8274-a5491336ce7a)

Llamario is an AI-powered web application that utilizes the Llama 3.2 11b and Llama 3-8b models for image processing and content generation. This application allows users to upload images and receive detailed descriptions, as well as generate content for social media based on user-defined topics.

## Features

- **Image Upload**: Users can upload images in JPG, JPEG, or PNG formats.
- **Image Processing**: The application analyzes uploaded images and provides insights about their contents.
- **Content Generation**: Users can generate well-structured articles based on selected topics or their own ideas.
- **User-Friendly Interface**: A clean and engaging interface built with Streamlit for ease of use.

## Technologies Used

- **Streamlit**: For building the web interface.
- **Pillow**: For image processing.
- **Groq**: To interact with the Llama models for image analysis and content generation.

## Getting Started

To run this application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mohAhmadRaza/Llama-3.2-LlamarioApp.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```

4. **Open in Browser**:
   Navigate to `https://llamario.streamlit.app/` in your web browser to view the application.

## Usage

1. Upload an image to receive a description.
2. Select a topic or enter your own topic to generate content for social media.
3. Enjoy the insights and content generated by Llama models!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Thanks to the creators of the Llama models for their innovative work in AI and machine learning.
- Special thanks to the Streamlit community for providing an excellent framework for building web applications.
