LOGURU_FORMAT = (
    "{time} | {level} |'trace id': {thread}|'function':{function}|'module':{"
    "module}|'process':{process}|'name':{name}|file':{file}| {"
    "message}"
)

LOGURU_ROTATION = "10 MB"

LOGURU_LOG_FILE_PATH = "log/accounts.log"

USA = "USA"

ALPHABETS = r"[a-zA-Z\s]+$"
CONTACT = r"^(\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$"
POSTAL = r"[0-9]{4}$"
STREET = r"^(?=.*[a-zA-Z])[A-Za-z0-9\s\,]+$"
CUSTOMER_ID = "^PT[0-9]{3}$"
SEARCH_WITH_NAME_OR_PHONE_NUMBER = r"[a-zA-Z\s]+$|^(\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$"
