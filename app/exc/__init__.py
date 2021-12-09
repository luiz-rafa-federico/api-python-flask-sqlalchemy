class InvalidCPFError(Exception):
    def __init__(self, message="The CPF must be numbers only.", code=400):
        self.message = message
        self.code = code


class InvalidEmailError(Exception):
    def __init__(self, message="Email format must be name@domain.com or name@domain.com.xx", code=400):
        self.message = message
        self.code = code


class InvalidDataTypeError(Exception):
    def __init__(self, key, type_send, type_valid, code=400):
        self.message = f"{key} must be of the {type_valid} type, and was sent as {type_send}."
        self.code = code