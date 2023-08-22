from flask import Flask, request, Response
import httpx
from functools import wraps
import base64
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


app = Flask(__name__)

def get_metrics():
  # NOTE - Need to use http2 to proxy correctly
  client = httpx.Client(http2=True)

  project_ref = os.environ.get('PROJECT_REF', 'default')
  url = f"https://{project_ref}.supabase.co/customer/v1/privileged/metrics"

  # Basic Auth configuration
  username = "service_role"
  password = os.environ.get('SERVICE_ROLE_JWT', 'default_password')

  return client.get(url, auth=(username, password))


@app.route('/', methods=['GET'])
@app.route('/metrics', methods=['GET'])
def proxy_metrics():
    resp = get_metrics()
    return (resp.content, resp.status_code, resp.headers.items())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
