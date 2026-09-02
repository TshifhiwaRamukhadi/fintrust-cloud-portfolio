from opensearchpy import OpenSearch
import datetime

client = OpenSearch(

    hosts=[
        {
            "host":
            "search-fintrust-security-logs.af-south-1.es.amazonaws.com",

            "port": 443
        }
    ],

    http_auth=(
        "admin",
        "CHANGE_ME"
    ),

    use_ssl=True,
    verify_certs=True
)

doc = {

    "timestamp":
        datetime.datetime.utcnow()
        .isoformat(),

    "event_type":
        "SUSPICIOUS_LOGIN",

    "account_id":
        "ACC-0001",

    "source_ip":
        "41.13.45.22",

    "country":
        "NG",

    "risk_score":
        87
}

index_name = (
    "fintrust-security-"
    +
    datetime.date.today()
    .strftime("%Y-%m")
)

response = client.index(
    index=index_name,
    body=doc
)

print(
    f"Indexed document: "
    f"{response['_id']}"
)

query = {
    "query": {
        "range": {
            "risk_score": {
                "gte": 80
            }
        }
    }
}

results = client.search(
    index=index_name,
    body=query
)

for hit in results["hits"]["hits"]:

    print(hit["_source"])