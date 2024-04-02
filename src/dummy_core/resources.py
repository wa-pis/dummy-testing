import http.client
import json
from typing import Any, Dict

from src.dummy_core.constant import EMOJI_PROVIDER_HOST, EMOJI_PROVIDER_RANDOM_PATH


def get_new_avatar() -> Dict[str, Any]:
    host = EMOJI_PROVIDER_HOST
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", EMOJI_PROVIDER_RANDOM_PATH, headers={"Host": host})
    response = conn.getresponse()
    return json.loads(response.read().decode("utf-8"))
