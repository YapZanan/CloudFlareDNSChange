# Dynamic DNS Updater for Cloudflare

This script is a Python-based dynamic DNS updater for Cloudflare. It automatically updates the DNS record for a specified domain with the current public IP address. If you prefer to use a Dockerized version of the script, you can follow the instructions below.

## Prerequisites

- Python 3.x
- `requests` library: You can install it using `pip install requests`.
- `cloudflare` library: You can install it using `pip install cloudflare`.

## Installation

### Manual Installation:
1. Clone the repository or download the script to your local machine.
2. Install the required dependencies (`requests` and `cloudflare` libraries) using the provided installation commands.
3. Set up the required environment variables as mentioned in the previous instructions.
4. Run the script using `python main.py`.

### Dockerized Installation:
1. Pull the Docker image from Docker Hub using the following command:
```docker pull yapzanan/cloudflarednschange:first```
2. Set up the required environment variables as mentioned in the previous instructions.
3. Run the Docker container using the following command:
```docker run -d --name cloudflare-dns-updater -e TOKEN=<your_api_token> -e DOMAIN=<your_domain> -e RECORD_NAME=<your_dns_record_name> yapzanan/cloudflarednschange:first```


**Note:** Ensure that the Cloudflare API token you provide has the necessary permissions to access and modify DNS records for the specified domain.

## Usage
Once the script or Docker container is running, it will periodically check the public IP address and update the specified DNS record on Cloudflare if necessary. The current public IP address will be displayed in the console or Docker logs, and any DNS record updates will be logged.

## Troubleshooting
- If you encounter any errors or issues, make sure you have provided the correct values for the required environment variables.
- Check your Cloudflare API token and ensure it has the necessary permissions to access and modify DNS records.
- Verify that your system has an internet connection and can access the Cloudflare API.

Feel free to modify and customize the script or Dockerfile to fit your specific requirements.
