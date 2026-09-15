import boto3

comp = boto3.client(
    "comprehend",
    region_name="af-south-1"
)


def redact_pii(text):

    response = comp.detect_pii_entities(
        Text=text,
        LanguageCode="en"
    )

    entities = response["Entities"]

    entities.sort(
        key=lambda e:
        e["BeginOffset"],
        reverse=True
    )

    detected_types = list({

        entity["Type"]

        for entity in entities

    })

    text_chars = list(text)

    for entity in entities:

        replacement = (
            f"[{entity['Type']}]"
        )

        text_chars[
            entity["BeginOffset"]:
            entity["EndOffset"]
        ] = list(replacement)

    return (
        "".join(text_chars),
        detected_types
    )