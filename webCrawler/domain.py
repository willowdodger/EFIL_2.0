from urllib.parse import urlparse


# we will get domain name
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split(".")  # kad gautum www domainName com, vietoj www.domainName.com
        return results[-2] + "." + results[-1]  # returns domainName
    except:
        return ""


def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ""
