
import streamlit as st 
import google.generativeai as genai

st.title("🧙🏻‍♀️ My SisNatt App") 
st.subheader("Conversation") 

# Initialize session state for storing chat history 
if "chat_history" not in st.session_state: 
    st.session_state.chat_history = [] # Initialize with an empty list 
# Display all chat messages 
# for message in st.session_state.chat_history: 
#     with st.chat_message("user"): 
#         st.markdown(message) 

# Capture user input and append to chat history 
if prompt := st.chat_input("Type your message here ..."): 
    st.session_state.chat_history.append(prompt) 
    st.chat_message("user").markdown(prompt)


# Capture Gemini API Key 
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")

# Initialize the Gemini Model 
if gemini_api_key: 
    try: 
        # Configure Gemini with the provided API Key 
        genai.configure(api_key=gemini_api_key) 
        model = genai.GenerativeModel("gemini-pro") 
        st.success("Gemini API Key successfully configured.") 
    except Exception as e: st.error(f"An error occurred while setting up the Gemini model: {e}")

    # Initialize session state for storing chat history 
    if "chat_history" not in st.session_state: 
        st.session_state.chat_history = [] # Initialize with an empty list

    # Display previous chat history using st.chat_message (if available) 
    for role, message in st.session_state.chat_history: 
        st.chat_message(role).markdown(message)

    # Define a prompt to guide the conversation
    prompt = "Welcome! I’m your Anti-Aging Assistant, here to help you maintain youthful health and appearance. I can provide tips on skincare, diet, fitness routines, and lifestyle habits to promote healthy aging. You can also ask me about specific anti-aging products, treatments, or wellness practices."

    # Capture user input and generate bot response
    if user_input := st.chat_input("Type your message here..."):
        # Combine the predefined prompt with user input
        full_input = prompt + user_input


    # Use Gemini AI to generate a bot response 
        if model: 
            st.write(user_input)
            try: 
                response = model.generate_content(user_input) 
                bot_response = response.text
                # Store and display the bot response 
                st.session_state.chat_history.append(("user", user_input)) 
                st.session_state.chat_history.append(("assistant", bot_response)) 
                st.chat_message("assistant").markdown(bot_response) 
            except Exception as e: 
                st.error(f"An error occurred while generating the response: {e}")

