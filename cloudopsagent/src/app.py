import json
# from agent import getmyagent
# import json
# from tools import tool_list
# from langgraph.graph import StateGraph,  START, END
# from langgraph.prebuilt import ToolNode
# from langchain_core.messages import SystemMessage,  HumanMessage
# from langgraph_dynamodb_checkpoint import DynamoDBSaver
# from langgraph_utils import call_model, create_tools_json
# import os
# from langgraph_reducer import PrunableStateFactory
# import boto3
# import logging
# from twilio.rest import Client
# import requests

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# model = os.environ["MODEL_NAME"]


# tool_node = ToolNode(tools=tool_list)

# def should_continue(state) -> str:
#     last_message = state['messages'][-1]
#     if not last_message.tool_calls:
#         return END
#     return 'tools'

# def process_message(channel_type, recipient, message):

#     prompt = (
#         f"The following user has sent a message:\n"
#         f"- UserID: {recipient}\n"
#         f"- Message: {message}\n"
#         f"- Sent via: {channel_type}\n\n"
#     )    

#     input_message = {
#         "messages": [HumanMessage(prompt)],
#     }


#     response = app.invoke(input_message)

#     logger.info("Unparsed Response History - last 7:", response["messages"][-7:])

#     agent_response = response["messages"][-1].content
#     logger.info(f"Unparsed Response: {agent_response}")

#     # Assuming the comms_agent_response is in the format:
#     # {"nextagent": "END", "message": "User-facing message delivered"}
#     parsed_response = json.loads(agent_response)

#     logger.info(f"Response: {parsed_response}")

#     return {
#         "fromagent": "awsagent",  # Identifying this agent
#         "nextagent": parsed_response.get("nextagent", ""),  # or another agent name if chaining
#         "message": parsed_response.get("message", ""),
#         "channel_type": channel_type,
#         "from": recipient
#     }

# def lambda_handler(event, context):
#     logger.info(f"Received event: {event}")

    
#     if "Records" in event:
#         for record in event["Records"]:
#             body = json.loads(record["body"])
#             channel_type = body.get("channel_type")
#             recipient = body.get("from")
#             message = body.get("messages")

#             if not all([channel_type, recipient, message]):
#                 logger.info(f"Skipping message due to missing fields")
#                 continue

#             process_message(channel_type, recipient, message)

#     # response_message = getmyagent(body) 
#     return 

def lambda_handler(event, context):
    return {
        "response": "Hello World!"
    }