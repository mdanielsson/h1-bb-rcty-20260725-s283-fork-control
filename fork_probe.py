#!/usr/bin/env python3

import json
import os
import subprocess


print(
    json.dumps(
        {
            "marker": "S283_EXTERNAL_FORK_HEAD",
            "actor": os.environ.get("GITHUB_ACTOR"),
            "event": os.environ.get("GITHUB_EVENT_NAME"),
            "repository": os.environ.get("GITHUB_REPOSITORY"),
            "sha": os.environ.get("GITHUB_SHA"),
        },
        sort_keys=True,
    )
)

query_tag = f"H1_BB_RCTY_S283_{os.environ['GITHUB_RUN_ID']}"
query = f"""
SELECT
  CURRENT_USER() AS USER_NAME,
  CURRENT_ROLE() AS PRIMARY_ROLE,
  CURRENT_ACCOUNT() AS ACCOUNT_LOCATOR,
  CURRENT_ACCOUNT_NAME() AS ACCOUNT_NAME,
  '{query_tag}' AS QUERY_TAG_MARKER,
  IFF(
    CURRENT_USER() = 'H1_BB_RCTY_20260725_S283_OIDC_FORK_CONTROL'
    AND CURRENT_ROLE() = 'PUBLIC'
    AND CURRENT_ACCOUNT() = 'GD35286',
    'S283_EXTERNAL_FORK_EXPECTED_IDENTITY',
    'S283_EXTERNAL_FORK_UNEXPECTED_IDENTITY'
  ) AS CONTROL_RESULT
"""
completed = subprocess.run(
    ["snow", "sql", "-x", "--format", "json", "-q", query],
    check=True,
    text=True,
    stdout=subprocess.PIPE,
)
print(completed.stdout)
