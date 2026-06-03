import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

from prompts import ANALYSIS_PROMPT

llm = ChatOpenAI(
    model="gpt-5.1",
    temperature=0.3
)

prompt = PromptTemplate(
    template=ANALYSIS_PROMPT,
    input_variables=["idea", "customers", "revenue"]
)

startup_chain = prompt | llm | StrOutputParser()