## Supabase Metrics Proxy

## Wat is dit?

This is a simple proxy that allows you to scrape metrics from your Supabase project locally. You configure it via a `.env` file with your project ref and service key, and it will authenticate requests to the Supabase metrics API.

It's useful for local development, if you want to gather metrics from your Supabase project with a tool like [`am`](https://github.com/autometrics-dev/am).

## Let's Go

```sh
# Copy the example .env file
cp .env.example .env

# Now, add secret key to .env, as well as project ref
# ...
# (i'll wait)
# ...
# Alright. You're back? Good! Let's continue.

# Now, let's create a virtual env and start a proxy to the metrics endpoint
python3 -m venv venv
pip3 install -r requirements.txt

# Start the proxy so we can scrape metrics locally
flask --app app.py --debug run

# Boot up a local prometheus that scrapes this bad boi
am start http://127.0.0.1:5000
```