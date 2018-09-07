"""
Banzee

Error message dictionary
"""

messages = {
    200: "The request was completed successfully.",
    400: "Invalid request. Client might be missing some mandatory values or might call a wrong API.",
    401: "API authentication failed. Invalid request-header field or not acceptable client.",
    402: "Payment required.",
    404: "Resource not found.",
    405: "Operation not allowed.",
    408: "Request timeout.",
    409: "Resource duplicated.",
    423: "Client locked. Maximum number of attempts exceeded. Please try again later.",
    500: "Internal server error.",
}

def get_message(code):
    """
    Read a message by code value.
    """
    if code not in messages:
        return "Unknown code"

    return messages[code]
