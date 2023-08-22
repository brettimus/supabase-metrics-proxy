from flask import Flask, request, Response
import httpx
from functools import wraps
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


app = Flask(__name__)

PROJECT_REF = os.environ.get('PROJECT_REF', 'default')
METRICS_URL = f"https://{PROJECT_REF}.supabase.co/customer/v1/privileged/metrics"

USERNAME = 'service_role'
PASSWORD = os.environ.get('SERVICE_ROLE_JWT', 'default_password')

def get_metrics():
  # NOTE - Need to use http2 to proxy correctly
  client = httpx.Client(http2=True)
  # print(f"Using {USERNAME} and {PASSWORD} to authenticate to {url}")
  return client.get(METRICS_URL, auth=(USERNAME, PASSWORD))


@app.route('/', methods=['GET'])
@app.route('/metrics', methods=['GET'])
def proxy_metrics():
    resp = get_metrics()
    return (resp.content, resp.status_code)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
