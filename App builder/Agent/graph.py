from langchain_groq import ChatGroq
#importing the prompts class
from Agent.prompts import *
#import states file
from Agent.states import *

#libraries for langgraph
from langgraph.constants import END
from langgraph.graph import StateGraph

# Initialize the Groq client with correct model and key
#this model have some token limit
llm = ChatGroq(
    api_key="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",  # use your actual key
    model_name="openai/gpt-oss-120b"  # confirmed available
)

# user_prompt = " create simple calculator web application"

#planner prompt

#planner agent func get state as dic and return dic as o/p
def planner_agent(state: dict)->dict:
    users_prompt = state["user_prompt"]
    res =  llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
    return {"plan": res}

# state = {
#     "user_prompt": user_prompt,
#     "plan" :"",
# }
#
# print(res)

#graph creation

graph = StateGraph(dict)
graph.add_node("planner" , planner_agent)
graph.set_entry_point("planner")

agent = graph.compile()
user_prompt = "Create a simple calculator web application"

result = agent.invoke({"user_prompt":user_prompt})
print(result)

















############################################################for testing LLM connection at begining#########################
#it's a class derived from pydantic basemodel
# class Schema(BaseModel):
#     price : float
#     eps:  float
#
#
# #structured format data--> using langchains structured output
# res = llm.with_structured_output(Schema).invoke("Extract price and EPS from this report: "
#                                                 "NVIDIA reported quarterly EPS of 2.3 and"
#                                                 "their current price is $100.")
#
# # Print the result
# print(res)


#############################################################################################################