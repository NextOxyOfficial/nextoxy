import requests

endpoint = 'https://api.cloudflare.com/client/v4/'
api_key = '51d459ab812563a59b822bbfeffeb2266f160'
owner = '6219c8ae5e9742a2353292c242078b55'
headers = {
    'X-Auth-Key': api_key,
    'X-Auth-Email': 'alimulislam50@gmail.com'
}
def add_dns(cfid, type, name, content, proxy, ttl=3600):
    response = requests.post(endpoint+'zones/'+cfid+'/dns_records', json={"type":type,"name":name,"content":content,"ttl":ttl,"priority":10,"proxied":proxy}, headers=headers)
    return response.json()
def delete_dns(dns):
    response = requests.delete(endpoint+'zones/'+dns.domain.cfid+'/dns_records/'+dns.cfid, headers=headers)
    return response.json()
def add_domain(domain):
    response = requests.post(endpoint+'zones', json={"name":domain,"account":{"id":owner},"jump_start":True,"type":"full"}, headers=headers)
    return response.json()
def delete_domain(domain):
    response = requests.delete(endpoint+'zones/'+domain.cfid, headers=headers)
    return response.json()


