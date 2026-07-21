#sk_bdfb4162aebdcc8dee3dc557ea111eeb5571530d72206de0


from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key="sk_bdfb4162aebdcc8dee3dc557ea111eeb5571530d72206de0"
)

response = client.conversational_ai.agents.create(
    name="My conversational agent",
    conversation_config={
        "agent": {
            "prompt": {
                "prompt": "You are a helpful assistant that can answer questions and help with tasks.",
            }
        }
    }
)
