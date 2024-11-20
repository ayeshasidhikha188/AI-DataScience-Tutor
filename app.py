import streamlit as st
import google.generativeai as ai

# Read API key from file
with open(r"C:\Users\mdimr\Downloads\AI_Tutor\Aireviewer_Key.txt", "r") as key_file:
    api_key = key_file.read().strip()

# Configure the AI model
ai.configure(api_key=api_key)

# Define the system prompt
sys_prompt = """
You are a highly advanced Conversational AI Data Science Tutor, designed to provide clear, structured, and engaging explanations tailored to the user’s query. Ensure your responses are concise, visually appealing, and easy to understand. Always format your outputs in Markdown, incorporating relevant emojis to enhance readability and engagement. Follow the guidelines below:

1. Output Structuring Guidelines
Greeting (Optional): Begin with a warm greeting only for conversational or general questions (e.g., "Hello there! 👋").

Content Organization:

Use section headers (e.g., ### What is Time Series?) and bullet points to structure explanations.
Incorporate subheadings for clarity when breaking down complex topics.
Maintain clear spacing between sections for better readability.
Examples:

Provide real-world examples or analogies to make concepts relatable.
Include code snippets enclosed in triple backticks (```) for technical queries with clear comments for clarity.
Add emojis sparingly to emphasize or visually distinguish sections (e.g., 📊 for data analysis, 🧮 for calculations).
Conclusion (Optional):

End with a positive and engaging note only if the query involves learning or open-ended discussion (e.g., "I hope this helps! Feel free to ask more questions. 😊").
2. Formatting Rules
Format the response using Markdown syntax:
Use #, ##, and ### for headers based on the section hierarchy.
Use - or * for bullet points and 1. for numbered lists.
Add bold for key terms sparingly to draw attention.
Include inline code using backticks (inline code) for variable names or methods.
Use triple backticks (```) for code blocks, ensuring proper indentation.
Avoid overlapping text, inconsistent spacing, or excessive emojis. Use only relevant emojis that align with the topic.
3. Tone Guidelines
Conversational Tone:

Use for beginner or exploratory questions, such as "What is machine learning?"
Add engaging language and relatable analogies.
Professional Tone:

Use for academic or technical queries, focusing on clarity and depth.
Avoid Redundant Friendliness:

Be direct and precise for factual or task-specific questions, without unnecessary embellishments.
"""

# Initialize the AI model
model = ai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", 
                           system_instruction=sys_prompt)

# Set up the Streamlit app layout
st.set_page_config(page_title="Conversational AI Data Science Tutor", layout="wide")

# App title with custom styling
st.markdown(
    """
    <style>
    body {
        background-color: #E0F7FA;  /* Light gray background for the full page */
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .container {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: flex-start;
        background-color: #FFB6C1;
        height: 100vh;
        padding: 20px;
        box-sizing: border-box;
    }
    .app-box {
        background-color: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 1200px;
    }
    .input-box {
        margin-bottom: 20px;
    }
    .response-box {
        margin-top: 20px;
        padding: 15px;
        background-color: #e1f5fe;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        font-size: 18px;
        color: #333;
    }
    .response-box h4 {
        margin-bottom: 10px;
        color: #FF6347;
    }
    .response-box p {
        margin: 10px 0;
        font-style: italic;
    }
    .input-box textarea {
        width: 100%;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ccc;
        font-size: 18px;
    }
    .get-answer-btn {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        font-size: 16px;
        cursor: pointer;
    }
    .get-answer-btn:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main layout with a container to place the title and image on the right side
with st.container():
    col1, col2 = st.columns([3, 2])

    # Left column: User input and AI response
    with col1:
        # Title
        st.markdown('<div class="title">AI Data Science Tutor 🤖</div>', unsafe_allow_html=True)

        st.subheader("👋😊 Welcome! How can I assist you in Data Science ???")
        st.write("I am here to help you learn and answer your data science questions. Ask away! 💡")

        # Input text area for user query
        user_prompt = st.text_area(
            "Ask Your Question: :speech_balloon:",
            placeholder="Type your question here... 🌱",
            height=100
        )

        # Button to get the response
        if st.button("Get Answer", key="get_answer", help="Click to get a detailed answer!"):
            if user_prompt.strip():
                with st.spinner("Wait... 🤔"):
                    try:
                        # Generate response from model
                        response = model.generate_content(user_prompt)
                        
                        # Extract the response text
                        if response and response.candidates:
                            response_text = response.candidates[0].content.parts[0].text
                        else:
                            response_text = "I couldn't generate a proper response. Please try rephrasing your question. 🙇"

                        # Display the response as a normal conversation
                        st.write(f"**AI's Answer:** 🤖\n\n✅ {response_text}")

                    except Exception as e:
                        st.error(f"Something went wrong: {str(e)} 😞")
            else:
                st.warning("Please enter a question to get started! 🤗")

    # Right column: Static image
    with col2:
        st.image(
            "https://miro.medium.com/v2/resize:fit:740/0*3VYXf9OgP494lrqR.png",
            caption="Data Science Insights 📊",
            use_container_width=True,
        )
