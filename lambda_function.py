import boto3
import os
import json

client_sme = boto3.client("bedrock-runtime")

model_id = os.environ["MODEL_ID"]

def lambda_handler(event, context):
    body = json.loads(event['body'])
    prompt = body['prompt']

    message_prompt = [{
            "role": "user",
            "content": [{
                "text": prompt
            }]
        }]

    system_prompt = [{
        "text": "Act as a wind turbine manufacturing assitant. Summarize the logs in 5 lines."
    }]

    inference_params = {
        "maxTokens": 2500,
        "topP": 0.95,
        "topK": 20,
        "temperature": 0.7
    }

    request_body = {
        "schemaVersion": "messages-v1",
        "messages": message_prompt,
        "system": system_prompt,
        "inferenceConfig": inference_params
    }

    response = client_sme.invoke_model(
        body=json.dumps(request_body),
        contentType="application/json",
        accept="application/json",
        modelId=model_id,
        trace="ENABLED",
        performanceConfigLatency='standard'
    )

    response_dict = json.loads(response['body'].read())
    final_response = response_dict['output']['message']['content'][0]['text']

    return {
        'statusCode': 200,
        'body': json.dumps(final_response)
    }