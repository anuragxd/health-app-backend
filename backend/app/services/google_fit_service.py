import requests
from datetime import datetime, timedelta


def fetch_google_fit_steps(access_token: str):

    url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    end_time = int(datetime.utcnow().timestamp() * 1000)
    start_time = int((datetime.utcnow() - timedelta(days=1)).timestamp() * 1000)

    body = {
        "aggregateBy": [
            {
                "dataTypeName": "com.google.step_count.delta"
            }
        ],
        "bucketByTime": {
            "durationMillis": 86400000
        },
        "startTimeMillis": start_time,
        "endTimeMillis": end_time
    }

    response = requests.post(url, headers=headers, json=body)

    return response.json()