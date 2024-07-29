from datetime import datetime

KSEARCH_DAGS_DEFAULT_ARGS = {
    "default_view": "grid",
    "catchup": False,
    "max_active_runs": 1,
    "start_date": datetime(2024, 1, 1),
    "default_args": {
        "email": ["labs_wpinto@keystonestrategy.com"],
        "email_on_retry": False,
        "email_on_failure": True,
        "retries": 1,
    },
    "tags": ["ksearch"],
}
