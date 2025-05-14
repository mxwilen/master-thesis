# === EXAMPLE CATEGORY MATCHERS ===
def is_db_change(function_name):
    db_patterns = re.compile(r"(db|commit|session|update|delete|query)", re.IGNORECASE)
    return bool(db_patterns.search(function_name))

def is_file_write(function_name):
    file_patterns = re.compile(r"(write|save|store|append|file|export)", re.IGNORECASE)
    return bool(file_patterns.search(function_name))

def is_logging_change(function_name):
    log_patterns = re.compile(r"(log|logger|print|debug|warn|error)", re.IGNORECASE)
    return bool(log_patterns.search(function_name))
