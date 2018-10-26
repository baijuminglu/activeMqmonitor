import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


def get_queue_info(ip, port, user, pas):
    url = "http://{0}:{1}/admin/queues.jsp".format(ip, port)
    req = requests.get(url, auth=HTTPBasicAuth(user, pas))
    soup = BeautifulSoup(req.text, 'lxml')
    table = soup.find('table', {'id': 'queues'}).find('tbody').stripped_strings
    queue_info = list(filter(lambda x: x not in ["Browse", "Active Consumers",
                                                 "Send To", "Purge", 'Delete',
                                                 'Active Producers'], table))
    return [queue_info[i:i+5] for i in range(0, len(queue_info), 5)]




