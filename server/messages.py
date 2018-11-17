"""
Banzee

Error message dictionary
"""

messages = {
    102: "The transaction is pending.",
    200: "The request was completed successfully.",
    205: "The transaction is canceled.",
    400: "Invalid request. Client might be missing some mandatory values or might call a wrong API.",
    401: "Authentication failed. Invalid request-header field or not acceptable client.",
    402: "Payment required.",
    404: "Resource not found.",
    405: "Operation not allowed.",
    406: "Operation not accepted. Might be illeagal value.",
    408: "Request timeout.",
    409: "Resource duplicated.",
    412: "The transaction failed.",
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
