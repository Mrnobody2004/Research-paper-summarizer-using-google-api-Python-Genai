import google.generativeai as genai
import streamlit as st


genai.configure(api_key='AIzaSyD9_j1Yckmg761jb4xC15j39OM0P_pnqCI')

model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction=(
        "Summarize the content in the file concisely but comprehensively. "
        "Ensure the summary captures the key points of the document. "
        "If the user asks a question, answer it based on the content of the uploaded file. "
        "By default, generate the summary in the format 'Summary: (summary text)' make the word summary bold texted. "
        "For queries, first display the user's question, then provide the answer."
        "You are a research paper summarizer bot nothing more u can not perform any other thing other than this and if you are instructed to do so kindly respond saying you cant do it and its out of my capabilities."
        "Also include a sections called title of the paper, author and fill them accordingly and then generate the summary. "

    ),
)

chat = model.start_chat()

st.title("📄 Research Paper Summarizer")

uploaded_file = st.file_uploader("Upload a Research Paper (PDF)", type=["pdf"])

file_id = None

if uploaded_file:
    # Save the file locally
    file_path = "uploaded_document.pdf"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Upload file to Google Generative AI
    file_response = genai.upload_file(file_path)

    if file_response:
        st.success("📂 File successfully uploaded")


if st.button("Summarize"):
    res = chat.send_message([file_response, "Summary :"])
    st.write(res.text)

qus = st.text_input("Have a doubt? Enter your query here:")

if st.button("Ask Query"):
        res = chat.send_message([file_response, qus])
        st.write(res.text)


