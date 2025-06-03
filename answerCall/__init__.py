import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Call received.')

    return func.HttpResponse(
        json.dumps({
            "actions": [
                {
                    "actionType": "PlayPrompt",
                    "prompts": [
                        {
                            "type": "text",
                            "text": "Hello. Please state your full name and appointment time after the beep."
                        }
                    ]
                },
                {
                    "actionType": "Recognize",
                    "recognitionType": "Speech",
                    "playPrompt": False,
                    "endSilenceTimeoutInMs": 3000,
                    "operationContext": "record-transcription"
                }
            ]
        }),
        mimetype="application/json"
    )
