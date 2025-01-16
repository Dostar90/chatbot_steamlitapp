from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_models import ChatOpenAI
import streamlit as st

st.set_page_config(page_title="Conversational Chatbot", page_icon="💬")

st.title("💬 A Langchain Chatbot")
st.caption("🚀 A chatbot powered by OpenAI LLM")

# Hardcoded API key (Not recommended for production)
api_key = "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"

chat = None  # Define chat object

if api_key:  # Check if API key is provided
    chat = ChatOpenAI(api_key=api_key, temperature=0.5)  # Create ChatOpenAI instance

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        SystemMessage(content="Hello, I am a chatbot to help you with your queries. How can I help you!")
    ]

st.write(st.session_state['messages'][0].content)

def get_openai_response(query):
    st.session_state['messages'].append(HumanMessage(content=query))
    answer = chat(st.session_state['messages'])
    st.session_state['messages'].append(AIMessage(content=answer.content))

    return answer.content if answer else "Sorry, I couldn't generate a response."

description = "Enter your query here..."
input_text = st.text_input("Input: ", value="", key="input", placeholder=description)

if st.button("Submit"):
    if chat is None:
        st.warning("Please input your OpenAI API key.")
    elif not input_text.strip():
        st.warning("Please enter a query.")
    else:
        try:
            with st.spinner('Generating...'):
                response = get_openai_response(input_text)
                st.write(response)
        except Exception as e:
            st.error("An error occurred: {}".format(str(e)))
