import streamlit as st
from agent import memory_agent


st.title("An Agent To Help You")
st.write("This agent is helpfull assistant")


if 'messages' not in st.session_state:
    st.session_state['messages']=[]


user_input=st.text_input("Ask anything you want😌")
if st.button("Submit") and user_input:
    
    st.session_state['messages'].append({"role" : "user" , "content" : user_input})
    with st.spinner("Agent is thinking for a desired answer..."):
        response=memory_agent.invoke(
            {'messages' : st.session_state['messages']},
            config={'configurable' : {'thread_id' : 'user123'}}
        )

    agent_msg=response['messages'][-1].content
    st.session_state['messages'].append({"role": "assistant" , "content" : agent_msg})


for msg in st.session_state['messages']:
    if msg["role"]=="user":
        st.markdown(f"**you:** {msg['content']}")
    else:
        st.markdown(f"**Agent:** {msg['content']}")