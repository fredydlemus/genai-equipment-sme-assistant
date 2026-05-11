import boto3

client_sme = boto3.client("bedrock-runtime")

def lambda_handler(event, context):
    user_input = event['prompt']
    print(user_input)