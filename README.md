# Fleet Portal (study app)

A deliberately tiny Flask app used by the `packer-ami-images` Terraform-study
episode. Packer bakes it into an AWS AMI and runs it with gunicorn behind a
systemd service on port 5000.

## Endpoints
- `GET /`        → plain-text liveness string
- `GET /health`  → JSON `{status, service, utc}`

## Run locally
```
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 app:app     # prod-style (Linux)
python app.py                            # dev server (any OS)
```
