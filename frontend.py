import streamlit as st
from ai_researcher_langgraph import INITIAL_PROMPT, graph, config
import logging
from langchain_core.messages import AIMessage

# -------------------- Logging --------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------------------- Page Config --------------------
st.set_page_config(page_title="Research AI Agent", page_icon="📄", layout="wide")

# -------------------- Custom Styling --------------------
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 850px;
            margin: auto;
        }
        .stChatMessage {
            border-radius: 14px;
            padding: 12px 16px;
            margin-bottom: 12px;
            font-size: 15px;
            line-height: 1.6;
        }
        .stChatMessage.user {
            background: linear-gradient(135deg, #e6f0ff, #cce0ff);
            color: #003366;
            font-weight: 500;
        }
        .stChatMessage.assistant {
            background: #f9f9f9;
            border: 1px solid #ddd;
            color: #1a1a1a;
        }
        .stTextInput input, .stChatInput input {
            border-radius: 14px;
            padding: 10px 14px;
            font-size: 15px;
            border: 1px solid #ccc;
        }
        .title {
            font-size: 32px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 0.3rem;
        }
        .subtitle {
            font-size: 16px;
            text-align: center;
            color: #555;
            margin-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- Header --------------------
st.markdown("<div class='title'>📄 Research AI Agent</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>💡 Explore, analyze, and generate research papers with AI</div>", unsafe_allow_html=True)

# -------------------- Session State --------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    logger.info("Initialized chat history")

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = None

# -------------------- Render Previous Chat --------------------
for chat in st.session_state.chat_history:
    st.chat_message(chat["role"]).write(chat["content"])

# -------------------- Chat Interface --------------------
user_input = st.chat_input("🔍 What research topic would you like to explore?")

if user_input:
    # Save and show user input
    logger.info(f"User input: {user_input}")
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Prepare input for agent
    chat_input = {"messages": [{"role": "system", "content": INITIAL_PROMPT}] + st.session_state.chat_history}
    logger.info("Starting agent processing...")

    # Placeholder for streaming assistant message
    assistant_placeholder = st.empty()
    full_response = ""

    for s in graph.stream(chat_input, config, stream_mode="values"):
        message = s["messages"][-1]

        # Log tool calls
        if getattr(message, "tool_calls", None):
            for tool_call in message.tool_calls:
                logger.info(f"Tool call: {tool_call['name']}")

        # Stream assistant response
        if isinstance(message, AIMessage) and message.content:
            text_content = message.content if isinstance(message.content, str) else str(message.content)
            full_response += text_content + " "
            assistant_placeholder.chat_message("assistant").write(full_response)

    # Save final assistant response
    if full_response:
        st.session_state.chat_history.append({"role": "assistant", "content": full_response})
