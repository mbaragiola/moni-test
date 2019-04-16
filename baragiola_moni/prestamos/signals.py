import requests


def autorizar(sender, instance, raw, **kwargs):
    url = "http://scoringservice.moni.com.ar:7001/api/v1/scoring/"
    url += "?document_number=" + instance.dni
    url += "&gender=" + instance.genero
    url += "&email=" + instance.email

    response = requests.get(url)
    instance.autorizado = (response.status_code == requests.codes.ok)
