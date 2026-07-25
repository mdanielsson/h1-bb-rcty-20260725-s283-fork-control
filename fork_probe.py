#!/usr/bin/env python3

import json
import os


print(
    json.dumps(
        {
            "marker": "S283_BASE_CONTROL",
            "actor": os.environ.get("GITHUB_ACTOR"),
            "event": os.environ.get("GITHUB_EVENT_NAME"),
            "repository": os.environ.get("GITHUB_REPOSITORY"),
            "sha": os.environ.get("GITHUB_SHA"),
        },
        sort_keys=True,
    )
)

