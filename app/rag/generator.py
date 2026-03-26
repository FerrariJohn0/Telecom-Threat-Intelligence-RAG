def generate_summary(query, docs):

    vuln_texts = [d["clean"] for d in docs]

    combined = ". ".join(vuln_texts)

    summary = (
        f"For the query '{query}', the following telecom vulnerabilities were retrieved: "
        f"{combined}. "
        f"These vulnerabilities may impact telecom network infrastructure and should be mitigated."
    )

    return summary