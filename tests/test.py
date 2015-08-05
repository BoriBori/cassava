from pprint import pprint
import pytest

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def test_categorization(inv):
    keys = ['status', 'content_categories', 'security_categories']

    # Test get with a single domain
    domain = 'www.amazon.com'
    resp_json = inv.categorization(domain)

    assert_keys_in(resp_json, domain)
    assert_keys_in(resp_json[domain], *keys)


tapioca.whois('bechtel.com')
 ['status',
 'updated_date',
 'contacts',
 'nameservers',
 'expiration_date',
 'emails',
 'raw',
 'whois_server',
 'registrar',
 'creation_date',
 'id']

tapioca.whois('147.1.126.156')
['asn_registry',
 'asn_date',
 'asn_country_code',
 'raw',
 'asn_cidr',
 'query',
 'nets',
 'asn']

