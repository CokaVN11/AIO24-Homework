import streamlit as st
from hugchat import hugchat
from hugchat.login import Login


class Chatbot:
    __instance = None

    # Singleton Pattern
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Chatbot, cls).__new__(cls)
        return cls.__instance

    def __init__(self, username, password):
        if not hasattr(self, "__initialized") or not self.__initialized:
            if username and password:
                self._login(username, password)
                self._chatbot = hugchat.ChatBot(
                    cookies=self._cookies.get_dict())
                self.__initialized = True
            else:
                st.error("Please enter username and password")
                st.stop()

    def _login(self, username, password):
        try:
            sign = Login(username, password)
            print("Logging in...")
            self._cookies = sign.login()
            print("Login Successful")
        except Exception as e:
            print(f"Error: {e}")
            st.error(f"Error: {e}")
            st.stop()

    def get_response(self, user_input):
        return self._chatbot.chat(user_input)


class ChatApp:
    def __init__(self):
        self._init_session_state()
        self._init_sidebar()

    def _init_session_state(self):
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "How may I help you?"}]
        if "chatbot" not in st.session_state:
            st.session_state.chatbot = None

    def _init_sidebar(self):
        with st.sidebar:
            st.title("Login HugChat")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                self._handle_login(username, password)

    def _handle_login(self, username, password):
        if not (username and password):
            st.error("Please enter username and password")
        else:
            try:
                chatbot = Chatbot(username, password)
                st.session_state.chatbot = chatbot
                st.success("Login Successful")
            except Exception as e:
                st.error(f"Error: {e}")
                st.stop()

    def display_messages(self):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    def handle_user_input(self):
        if not st.session_state.chatbot_initialized:
            st.warning("Please login to start chatting")
            st.stop()

        if prompt := st.chat_input(disabled=not st.session_state.chatbot):
            print(prompt)
            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)
            self._get_chatbot_response(prompt)

    def _get_chatbot_response(self, prompt):
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chatbot.get_response(prompt)
                st.write(response)
        st.session_state.messages.append(
            {"role": "assistant", "content": response})


def main():
    st.title("Chatbot")
    app = ChatApp()
    app.display_messages()
    app.handle_user_input()


if __name__ == "__main__":
    main()
