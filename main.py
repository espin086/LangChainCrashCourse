from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI()


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a world class dog namer."),
        ("user", "{input}"),
    ]
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

response = chain.invoke({"input": "I have a new dog, what should I name it?"})
print(response)
