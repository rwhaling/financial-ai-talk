import boto3
import json

bedrock = boto3.client('bedrock-runtime', 'us-west-2', endpoint_url='https://bedrock-runtime.us-west-2.amazonaws.com')

modelId = 'anthropic.claude-v2'
accept = 'application/json'
contentType = 'application/json'

def complete(prompt, tokens=1000, temperature=0.5):
    claude_prompt = f"\n\nHuman:{prompt}\n\nAssistant:"
    body = json.dumps({
                        "prompt": claude_prompt,
                        "temperature": 0.5,
                        "top_p": 1,
                        "top_k": 250,
                        "max_tokens_to_sample": 1000,
                        "stop_sequences": ["\n\nHuman:"]
                     })
    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    return json.loads(response['body'].read())
    