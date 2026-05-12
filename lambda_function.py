import boto3
import os

client_sme = boto3.client("bedrock-runtime")

def lambda_handler(event, context):

    model_id = os.environ["MODEL_ID"]

    user_input = event['prompt']
    print(user_input)

    message_list = [{
            "role": "user",
            "content": [{
                "text": user_input
            }]
        }]

    request_body = {
        "schemaVersion": "messages-v1",
        "messages": message_list
    }

    response = client_sme.invoke_model(
        body=request_body,
        contentType="application/json",
        accept="application/json",
        modelId=model_id,
        trace="ENABLED",
        performanceConfigLatency='standard'
    )