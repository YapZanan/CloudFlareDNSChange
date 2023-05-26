import os
import time
import requests
import CloudFlare


# Get the current public IP address
def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        return response.json()['ip']
    else:
        raise Exception('Failed to retrieve public IP')


# Get the Cloudflare zone ID based on the domain name
def get_zone_id(api_token, domain):
    cf = CloudFlare.CloudFlare(token=api_token)
    zones = cf.zones.get(params={'per_page': 100})

    for zone in zones:
        if zone['name'] == domain:
            return zone['id']

    raise Exception('Zone not found')

# Update the Cloudflare DNS record
def update_dns_record(api_token, domain, dns_record_name, dns_record_type, ip_address):
    zone_id = get_zone_id(api_token, domain)
    cf = CloudFlare.CloudFlare(token=api_token)
    dns_records = cf.zones.dns_records.get(zone_id)

    matching_records = []
    for dns_record in dns_records:
        if dns_record['name'] == dns_record_name and dns_record['type'] == dns_record_type:
            matching_records.append(dns_record)

    if len(matching_records) == 1:
        dns_record = matching_records[0]
        dns_record['content'] = ip_address
        cf.zones.dns_records.put(zone_id, dns_record['id'], data=dns_record)
        print('DNS record updated successfully')
    else:
        print('Found DNS records:', matching_records)
        raise Exception('DNS record not found or multiple records found')


if __name__ == '__main__':
    try:
        api_token = os.getenv('TOKEN')
        domain = os.getenv('DOMAIN')
        dns_record_name = os.getenv('RECORD_NAME')
        dns_record_type = os.getenv('RECORD_TYPE', 'A')
        interval_minutes = int(os.getenv('INTERVAL', 1))

        if not (api_token and domain and dns_record_name):
            raise Exception('One or more environment variables are missing')

        while True:
            current_ip = get_public_ip()
            print(f'Current public IP: {current_ip}')
            update_dns_record(api_token, domain, dns_record_name, dns_record_type, current_ip)

            print(f'Waiting for {interval_minutes} minutes...')
            time.sleep(interval_minutes * 60)

    except Exception as e:
        print(f'Error: {str(e)}')
        exit(1)
