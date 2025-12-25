Environment variables in Python are key–value pairs stored in the operating system, not inside the Python code. They are used to hold configuration and sensitive data like passwords, API keys, database URLs, and debug flags so that these values don’t get hardcoded or exposed in the source code. Python reads environment variables at runtime using the os module, typically with os.getenv("KEY_NAME"), allowing the same code to run in different environments (development, testing, production) by just changing the environment values, not the code itself.

Reading environment variables

import os

api_key = os.getenv("API_KEY")   # returns None if missing
db_name = os.environ["DB_NAME"]  # throws error if missing

print(api_key)
print(db_name)