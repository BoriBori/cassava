Cassava is a library and web UI for analyzing IOCs with multiple APIs.

# Quickstart

Either clone this repo and install the Python package or install directly with pip. Using a virtualenv is not required, but since Cassava has many dependencies it is highly recommend.

Git clone:
```Bash
virtualenv venv
source venv/bin/activate
```

Git clone and install:
```
git clone https://github.com/BechtelCIRT/cassava.git
python cassava/setup.py install
```

Or Pip installation:
```Bash
pip install cassava
```

The run_cassava.py script can initialize a database and a template config file:
```Bash
run_cassava.py --initdb --initconfig
```

This will immediately start the Cassava web UI which can be accessed at http://localhost:5000. Add VirusTotal or OpenDNS API keys to cassava_config.py and restart (ctrl-c then re-run script) to enable those APIs.

The auto-generated cassava_config.py template will look like this:

```PYTHON
DB_PATH = 'sqlite:///cassava.db'
OPENDNS_APIKEY = ''
VT_API_KEY = ''
PROXIES = {'http_proxy' : None, 'https_proxy' : None}
```

Add your VirusTotal API key and OpenDNS if you've got one. This is technically optional, but you won't get much out of Cassava without it.

# Examples

Active whois lookups:
```Python
In [1]: import cassava
In [2]: cassava.whois('github.com')
Out[2]:
{'contacts': {'admin': {'city': u'San Francisco',
   'country': u'US',
   'email': u'hostmaster@github.com',
   'name': u'GitHub Hostmaster',
    ...
 'whois_server': [u'whois.markmonitor.com']}
```

# Roadmap

* Add DomainTools API
* Support full VirusTotal API
* Add more built-in active tools (nmap, traceroute, ???)
* Add export functions (to JSON, CSV, and possibly STIX or related formats)
* Change web UI to override Scrypture defaults
* Add historical analysis capabilities, better management tools
* Come up with a cool logo
