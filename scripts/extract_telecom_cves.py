import json
import os

INPUT_FILE = "data/raw/nvdcve.json"
OUTPUT_FILE = "data/processed/telecom_cves.json"

os.makedirs("data/processed", exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

telecom_cves = []

for item in data["vulnerabilities"]:

    cve = item["cve"]
    cve_id = cve["id"]

    # CVSS extraction
    cvss_score = None
    metrics = cve.get("metrics", {})

    if "cvssMetricV31" in metrics:
        cvss_score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]

    elif "cvssMetricV30" in metrics:
        cvss_score = metrics["cvssMetricV30"][0]["cvssData"]["baseScore"]

    elif "cvssMetricV2" in metrics:
        cvss_score = metrics["cvssMetricV2"][0]["cvssData"]["baseScore"]

    # get English description
    description = ""

    for d in cve.get("descriptions", []):
        if d["lang"] == "en":
            description = d["value"].lower()

    # telecom keywords
    keywords = [
        "5g","5g core","5g network","4g","3g","2g","lte", "telecom", "cellular",
        "mobile network", "base station","mobile core", "radio access","ran", "gnb", "enb","nodeb", "packet core", "network slicing",
        "sip", "diameter","ss7","gtp", "sctp", "rtp","ims", "sim","subscriber"
    ]
    description = description.lower()
    if any(k.lower() in description for k in keywords):

        telecom_cves.append({
            "id": cve_id,
            "description": description,
            "cvss": cvss_score
        })

print("Telecom CVEs found:", len(telecom_cves))

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(telecom_cves, f, indent=2)

print("Saved telecom CVEs to:", OUTPUT_FILE)