# Fleet Portal — a deliberately tiny, REAL Flask app.
# This is the application source Packer bakes into the AMI: on the build VM we
# git-clone this repo, install its deps into a virtualenv, and run it with
# gunicorn as the `fleet-portal` systemd service listening on port 5000
# (per the book's design: load balancer -> backend on 5000/HTTP).

from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    # Frontend/backend LB health checks hit "/". Keep it trivial.
    return "Fleet Portal is running \U0001F697  (baked into the AMI by Packer)"


@app.get("/health")
def health():
    # A JSON health endpoint the smoke test / load balancer can probe.
    return jsonify(
        status="healthy",
        service="fleet-portal",
        utc=datetime.now(timezone.utc).isoformat(),
    )


if __name__ == "__main__":
    # Dev-only entrypoint. In the AMI, gunicorn serves `app:app` instead.
    app.run(host="0.0.0.0", port=5000)
