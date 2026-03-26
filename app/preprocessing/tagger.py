
KEYWORDS = ["5g","ims","ss7","sip","diameter","upf","amf"]

def telecom_tags(text):
    return [k for k in KEYWORDS if k in text.lower()]
