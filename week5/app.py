
import requests
import streamlit as st

API_BASE = "https://api.elevenlabs.io/v1"


API_KEY = "sk_07a500b05d8e24b3b67463e91904c81432517ce30c1c56f4"
AGENT_ID = "agent_0401ky1v4fvfes4r5nrj0j47kas5"
URL = f"https://api.elevenlabs.io/v1/convai/agents/{AGENT_ID}/simulate-conversation"



st.title("The Garden of Eden", text_alignment='center')
st.markdown("Hi, I am sophia with The Garden of Eden, Its your local and cozy flowershop!")
st.markdown("How may I help you today?")


# Keep the growing conversation history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Show past messages
for turn in st.session_state.history:
    role = "user" if turn["role"] == "user" else "assistant"
    st.chat_message(role).write(turn["message"])

# Get new user input
prompt = st.chat_input("Message Ava...")

if prompt:
    elapsed = len(st.session_state.history)  # simple incrementing counter
    st.session_state.history.append({"role": "user", "message": prompt, "time_in_call_secs": elapsed})
    st.chat_message("user").write(prompt)

    payload = {
        "simulation_specification": {
            "simulated_user_config": {"language": "en"},
            "partial_conversation_history": st.session_state.history,
        },
        "new_turns_limit": 1,
    }
    headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}

    response = requests.post(URL, headers=headers, json=payload)
    data = response.json()

    if "simulated_conversation" not in data:
        st.error(f"API error (status {response.status_code}): {data}")
    else:
        # Update history with whatever the API returned, then pull out the reply
        st.session_state.history = data["simulated_conversation"]
        agent_turns = [t for t in st.session_state.history if t["role"] == "agent"]
        reply = agent_turns[-1]["message"] if agent_turns else "Sorry, I couldn't respond."

        st.chat_message("assistant").write(reply)