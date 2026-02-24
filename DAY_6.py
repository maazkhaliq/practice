from google import genai
import streamlit as st

client=genai.Client(api_key="AIzaSyA3cnJSaUu4ObjzJpkQdOoQx9RvzPr_gb0")

st.title("TALK TO AGENT")
st.write("This app demonstrates a conversational agent")

user_input=st.text_input("Ask a question:")
if st.button("Submit"):
    with st.spinner("Agent is thinking. . . "):
        response=client.models.generate_content(
            model='gemini-2.5-flash',contents=user_input
        )
    st.write(response.text)
