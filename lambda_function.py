from langchain_experimental.data_anonymizer import PresidioReversibleAnonymizer
import json



def anonymize_text(text,anonymizer):
    anonymizer.reset_deanonymizer_mapping()
    result = anonymizer.anonymize(text)
    return result, anonymizer.deanonymizer_mapping

def lambda_handler(event, context):
    anonymizer = PresidioReversibleAnonymizer(
    analyzed_fields=["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD","LOCATION"],
    faker_seed=40,
    add_default_faker_operators=False)
    sample_txt = " Hello my name is Julian Arango, my id is 312351234123 and I live in Atlanta"
    message = event.get('text',sample_txt)
    anonimization= {
        "original": message,
        "anonimized" : anonymize_text(message,anonymizer)
    }
    return {
        'statusCode': 200,
        'body': anonimization
    }
