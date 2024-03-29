import re
import collections

def is_ip(indicator):
    ip_format = re.compile(ip_regex)
    return ip_format.match(indicator)

def is_md5(indicator):
    ip_format = re.compile(md5_regex)
    return ip_format.match(indicator)

def is_sha1(indicator):
    ip_format = re.compile(sha1_regex)
    return ip_format.match(indicator)

def is_sha256(indicator):
    ip_format = re.compile(sha256_regex)
    return ip_format.match(indicator)

def is_sha256(indicator):
    ip_format = re.compile(sha256_regex)
    return ip_format.match(indicator)

def is_email(indicator):
    ip_format = re.compile(email_regex)
    return ip_format.match(indicator)

def is_domain(indicator):
    ip_format = re.compile(domain_regex)
    return ip_format.match(indicator)

def is_hash(indicator):
    if is_md5(indicator) or is_sha1(indicator) or is_sha256(indicator):
        return True
    else:
        return False

def hash_type(indicator):
    if is_sha256(indicator):
        return 'sha256'
    elif is_sha1(indicator):
        return 'sha1'
    elif is_md5(indicator):
        return 'md5'
    else:
        return False

def indicator_type(indicator):
    hash = hash_type(indicator)
    if hash:
        return hash
    elif is_ip(indicator):
        return 'ip'
    elif is_email(indicator):
        return 'email'
    elif is_domain(indicator):
        return 'domain'

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunker(seq, size):
    return(seq[pos:pos + size] for pos in xrange(0, len(seq), size))

"""
TLDs taken from http://data.iana.org/TLD/tlds-alpha-by-domain.txt
on 30 June 2015
Re-generate the list any time by running:
def get_updated_tlds():
    r = requests.get('http://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    tlds = r.text.split('\n')[1:-1] # split on lines and strip header
    return tlds
print '|'.join(sorted(get_updated_tlds(), key=lambda x: -len(x))).lower()
Note: The list must be sorted like this, or we might match shorter TLDs before
longer ones (e.g., .co will match before .com)
"""
TLDs = '''xn--vermgensberatung-pwb|xn--vermgensberater-ctb|xn--clchc0ea0b2g2a9gcd|xn--mgberp4a5d4ar|xn--xkc2dl3a5ee0h|xn--xkc2al3hye2a|sandvikcoromant|xn--i1b6b1a6a2e|xn--kcrx77d1x4a|xn--lgbbat1ad8j|xn--mgba3a4f16a|xn--mgbc0a9azcg|xn--nqv7fs00ema|cancerresearch|xn--6qq986b3xl|xn--b4w605ferd|xn--fiq228c5hs|xn--mgbaam7a8h|xn--mgbayh7gpa|xn--mgbbh1a71e|xn--mgbx4cd0ab|international|spreadbetting|xn--fpcrj9c3d|xn--fzc2c9e2c|xn--yfro4i67o|xn--ygbi2ammx|construction|scholarships|versicherung|xn--3e0b707e|xn--80adxhks|xn--80asehdb|xn--mgb9awbf|xn--mgbab2bd|xn--mgbpl2fh|xn--ngbc5azd|xn--ogbpf8fl|xn--qcka1pmc|accountants|barclaycard|blackfriday|bridgestone|contractors|engineering|enterprises|investments|motorcycles|photography|productions|williamhill|xn--1qqw23a|xn--3bst00m|xn--3ds443g|xn--45brj9c|xn--55qw42g|xn--6frz82g|xn--80ao21a|xn--czr694b|xn--d1acj3b|xn--estv75g|xn--fjq720a|xn--flw351e|xn--gecrj9c|xn--h2brj9c|xn--hxt814e|xn--imr513n|xn--j6w193g|xn--kprw13d|xn--kpry57d|xn--nyqy26a|xn--pgbs0dh|xn--q9jyb4c|xn--rhqv96g|xn--s9brj9c|xn--ses554g|xn--vuq861b|xn--xhq521b|xn--zfr164b|accountant|apartments|associates|bnpparibas|consulting|creditcard|cuisinella|eurovision|foundation|healthcare|immobilien|industries|management|properties|republican|restaurant|technology|telefonica|university|vistaprint|vlaanderen|xn--30rr7y|xn--45q11c|xn--4gbrim|xn--55qx5d|xn--80aswg|xn--90a3ac|xn--9et52u|xn--cg4bki|xn--czrs0t|xn--czru2d|xn--fiq64b|xn--fiqs8s|xn--fiqz9s|xn--io0a7i|xn--kput3i|xn--mxtq1m|xn--o3cw4h|xn--unup4y|xn--wgbh1c|xn--wgbl6a|xn--y9a3aq|accenture|allfinanz|amsterdam|aquarelle|barcelona|bloomberg|christmas|community|directory|education|equipment|financial|furniture|goldpoint|homedepot|institute|marketing|melbourne|microsoft|montblanc|solutions|vacations|xn--90ais|xn--c1avg|xn--d1alf|xn--j1amh|xn--l1acc|xn--nqv7f|xn--p1acf|xn--vhquv|yodobashi|airforce|attorney|barclays|bargains|boutique|bradesco|brussels|budapest|builders|business|capetown|catering|cleaning|clothing|commbank|computer|delivery|democrat|diamonds|discount|download|engineer|everbank|exchange|feedback|firmdale|flsmidth|football|graphics|holdings|infiniti|lighting|marriott|memorial|mortgage|movistar|partners|pharmacy|pictures|plumbing|property|redstone|saarland|services|software|supplies|training|ventures|xn--node|xn--p1ai|yokohama|abogado|academy|android|auction|bauhaus|brother|capital|caravan|careers|cartier|channel|college|cologne|company|cooking|corsica|country|coupons|courses|cricket|cruises|dentist|digital|domains|exposed|express|fashion|finance|fishing|fitness|flights|florist|flowers|forsale|frogans|gallery|genting|guitars|hamburg|hangout|hitachi|holiday|hosting|hoteles|hotmail|jewelry|kitchen|komatsu|lacaixa|lasalle|latrobe|leclerc|liaison|limited|markets|netbank|network|neustar|okinawa|organic|panerai|philips|realtor|recipes|rentals|reviews|samsung|sandvik|schmidt|schwarz|science|shiksha|shriram|singles|spiegel|starhub|statoil|support|surgery|systems|temasek|theater|tickets|toshiba|trading|website|wedding|whoswho|windows|youtube|zuerich|abbott|active|agency|airtel|alsace|bayern|berlin|bharti|broker|camera|career|casino|center|chrome|church|claims|clinic|coffee|condos|credit|dating|datsun|degree|dental|design|direct|doosan|durban|emerck|energy|estate|events|expert|futbol|garden|global|google|gratis|hermes|hiphop|hockey|insure|joburg|juegos|kaufen|lawyer|london|luxury|madrid|maison|market|monash|mormon|moscow|museum|nagoya|nissan|office|online|oracle|otsuka|photos|physio|piaget|pictet|quebec|racing|realty|reisen|repair|report|review|ryukyu|sakura|school|schule|soccer|social|studio|supply|suzuki|swatch|sydney|taipei|tattoo|tennis|tienda|travel|viajes|villas|vision|voting|voyage|walter|webcam|yachts|yandex|actor|adult|archi|audio|autos|azure|bible|bingo|black|boats|build|canon|cards|cheap|chloe|cisco|citic|click|cloud|coach|codes|crown|cymru|dabur|dance|deals|drive|earth|email|epson|faith|forex|forum|gifts|gives|glass|globo|gmail|green|gripe|guide|homes|honda|horse|house|irish|jetzt|koeln|kyoto|lease|legal|loans|lotte|lotto|lupin|mango|media|miami|money|movie|nadex|nexus|ninja|omega|osaka|paris|parts|party|photo|pizza|place|poker|praxi|press|rehab|reise|ricoh|rocks|rodeo|sener|shoes|skype|solar|space|study|style|sucks|swiss|tatar|tires|tirol|today|tokyo|tools|toray|tours|trade|trust|vegas|video|vista|vodka|wales|watch|works|world|xerox|aero|army|arpa|asia|auto|band|bank|bbva|beer|best|bike|bing|blue|bond|buzz|cafe|camp|care|cars|casa|cash|cern|chat|city|club|cool|coop|cyou|date|dclk|desi|diet|docs|doha|dvag|erni|fail|fans|farm|film|fish|fund|game|gbiz|gent|ggee|gift|gold|golf|goog|guge|guru|haus|help|here|host|icbc|immo|info|java|jobs|jprs|kddi|kiwi|kred|land|lgbt|lidl|life|limo|link|live|loan|love|ltda|luxe|maif|meet|meme|menu|mini|mobi|moda|mtpc|name|navy|news|nico|page|pics|pink|play|plus|pohl|porn|post|prod|prof|qpon|reit|rent|rest|rich|rsvp|ruhr|sale|sarl|saxo|scor|scot|seat|sexy|show|site|sncf|sohu|sony|surf|taxi|team|tech|tips|town|toys|vote|voto|wang|weir|wien|wiki|work|xbox|yoga|zone|abb|ads|aeg|afl|aig|app|axa|bar|bbc|bcn|bid|bio|biz|bmw|bnl|boo|bzh|cab|cal|cat|cba|cbn|ceo|cfa|cfd|com|crs|dad|day|dev|dnp|dog|eat|edu|esq|eus|fan|fit|fly|foo|frl|fyi|gal|gdn|gle|gmo|gmx|goo|gop|gov|hiv|how|ibm|icu|ifm|ing|ink|int|iwc|jcb|jlc|jll|kim|krd|lat|law|lds|lol|mba|men|mil|mma|moe|mov|mtn|nec|net|new|ngo|nhk|nra|nrw|ntt|nyc|one|ong|onl|ooo|org|ovh|pro|pub|red|ren|rio|rip|run|sap|sca|scb|sew|sex|ski|sky|soy|tax|tel|thd|top|tui|uno|uol|vet|wed|win|wme|wtc|wtf|xin|xxx|xyz|zip|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cu|cv|cw|cx|cy|cz|de|dj|dk|dm|do|dz|ec|ee|eg|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|za|zm|zw'''

ip_regex = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
md5_regex = '([a-f]|[0-9]){32}'
sha1_regex = '([a-f]|[0-9]){40}'
sha256_regex = '([a-f]|[0-9]){64}'
domain_regex = '((?=[a-z0-9-]{1,63}(\.|\[\.\]))(xn--)?[a-z0-9]+(-[a-z0-9]+)*(\.|\[\.\]))+('+TLDs+')'
email_regex = '[a-z0-9(\.|\[\.\])_%+-]+(@|\[@\])'+domain_regex
