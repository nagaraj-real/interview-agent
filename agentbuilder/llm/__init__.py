
from agentbuilder.llm.nvidia_llm import nvidia_embed
from agentbuilder.logger import uvicorn_logger as logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.embeddings import Embeddings
from agentbuilder.llm.openai_llm import openai_chat
from langchain.agents import create_tool_calling_agent

chat_llm = None

def get_chat_llm(*args,**Kwargs):
     return openai_chat(*args,**Kwargs)

def create_agent(*args,**Kwargs):
    return create_tool_calling_agent(*args,**Kwargs)

def get_embed_llm(*args,**Kwargs) -> Embeddings:
     return nvidia_embed(*args,**Kwargs) 

def get_casual_chat_prompt(preamble:str|None)->ChatPromptTemplate:
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                preamble,
            ), # type: ignore
            ("user", "{input}"),
        ]
    )
    return prompt

def extract_after_slash(text):
  if "/" in text:
    parts = text.split("/")
    return (parts[0],parts[1])
  else:
    return (text,None)

def load_chat_llm():
    global chat_llm
    try:
        chat_llm = get_chat_llm()
    except Exception as exc:
        logger.error(f"Error: {str(exc)}")