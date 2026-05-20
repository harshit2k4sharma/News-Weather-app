from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda

# Components
model = ChatMistralAI(model="mistral-small-2506")
parser = StrOutputParser()

# Two different prompts
short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 1-2 lines"
)

detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detail"
)

# Input
topic = "Machine Learning"

# #EARLIER APPROACH(BEFORE CHAINS)
# formatted_short = short_prompt.format_messages(topic = topic)
# response_short = model.invoke(formatted_short)
# str_out = parser.parse(response_short.content)

# formatted_detailed = detailed_prompt.format_messages(topic = topic)
# response_detailed = model.invoke(formatted_detailed)
# str_out_detailed = parser.parse(response_detailed.content)

# #EARLIER APPROACH (AFTER CHAINS IMPLEMENTATION)
# chain1 = short_prompt | model | parser
# chain2 = detailed_prompt | model | parser



chain = RunnableParallel({
    "short" :short_prompt | model | parser ,
    "detailed" :detailed_prompt |model |parser
})


result = chain.invoke({"topic":"Machine Learning"})

#for seperate short and detailed outputs, we can also use RunnableLambda to extract the respective inputs for each prompt from the main input dictionary as shown below:

# chain = RunnableParallel({
#     "short" :RunnableLambda(lambda x :x['short']) |short_prompt | model | parser ,
#     "detailed" :RunnableLambda(lambda x: x['detailed']) |detailed_prompt |model |parser
# })


# result = chain.invoke({
#     "short" : {"topic":"Machine Learning"},
#     "detailed" : {"topic":"Deep Learning"}
# })


print(result['short'])
print(result['detailed'])