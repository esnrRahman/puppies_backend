class ErrorCodes(object):
    """
    Extending HTTP error code convention -
    1xx: Informational - Request received, continuing process
    2xx: Success - The action was successfully received, understood, and accepted
    3xx: Redirection - Further action must be taken in order to complete the request
    4xx: Client Error - The request contains bad syntax or cannot be fulfilled
    5xx: Server Error - The server failed to fulfil an apparently valid request
    """

    # status codes
    # informational
    CONTINUE                                    = 100
    SWITCHING_PROTOCOLS                         = 101
    PROCESSING                                  = 102

    # successful
    OK                                          = 200
    CREATED                                     = 201
    ACCEPTED                                    = 202
    NON_AUTHORITATIVE_INFORMATION               = 203
    NO_CONTENT                                  = 204
    RESET_CONTENT                               = 205
    PARTIAL_CONTENT                             = 206
    MULTI_STATUS                                = 207
    IM_USED                                     = 226

    # redirection
    MULTIPLE_CHOICES                            = 300
    MOVED_PERMANENTLY                           = 301
    FOUND                                       = 302
    SEE_OTHER                                   = 303
    NOT_MODIFIED                                = 304
    USE_PROXY                                   = 305
    TEMPORARY_REDIRECT                          = 307

    # client error
    BAD_REQUEST                                 = 400
    UNAUTHORIZED                                = 401
    PAYMENT_REQUIRED                            = 402
    FORBIDDEN                                   = 403
    NOT_FOUND                                   = 404
    METHOD_NOT_ALLOWED                          = 405
    NOT_ACCEPTABLE                              = 406
    PROXY_AUTHENTICATION_REQUIRED               = 407
    REQUEST_TIMEOUT                             = 408
    CONFLICT                                    = 409
    GONE                                        = 410
    LENGTH_REQUIRED                             = 411
    PRECONDITION_FAILED                         = 412
    REQUEST_ENTITY_TOO_LARGE                    = 413
    REQUEST_URI_TOO_LONG                        = 414
    UNSUPPORTED_MEDIA_TYPE                      = 415
    REQUESTED_RANGE_NOT_SATISFIABLE             = 416
    EXPECTATION_FAILED                          = 417
    UNPROCESSABLE_ENTITY                        = 422
    LOCKED                                      = 423
    FAILED_DEPENDENCY                           = 424
    UPGRADE_REQUIRED                            = 426

    # server error
    INTERNAL_SERVER_ERROR                       = 500
    NOT_IMPLEMENTED                             = 501
    BAD_GATEWAY                                 = 502
    SERVICE_UNAVAILABLE                         = 503
    GATEWAY_TIMEOUT                             = 504
    HTTP_VERSION_NOT_SUPPORTED                  = 505
    INSUFFICIENT_STORAGE                        = 507
    NOT_EXTENDED                                = 510

    # Mapping status codes to official W3C names
    responses = {
        100: 'Continue',
        101: 'Switching Protocols',

        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        203: 'Non-Authoritative Information',
        204: 'No Content',
        205: 'Reset Content',
        206: 'Partial Content',

        300: 'Multiple Choices',
        301: 'Moved Permanently',
        302: 'Found',
        303: 'See Other',
        304: 'Not Modified',
        305: 'Use Proxy',
        306: '(Unused)',
        307: 'Temporary Redirect',

        400: 'Bad Request',
        401: 'Unauthorized',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable',
        407: 'Proxy Authentication Required',
        408: 'Request Timeout',
        409: 'Conflict',
        410: 'Gone',
        411: 'Length Required',
        412: 'Precondition Failed',
        413: 'Request Entity Too Large',
        414: 'Request-URI Too Long',
        415: 'Unsupported Media Type',
        416: 'Requested Range Not Satisfiable',
        417: 'Expectation Failed',

        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
        505: 'HTTP Version Not Supported',
    }

    # SUCCESS MESSAGE
    SUCCESS_MESSAGE = "{}. {}"

    # ERROR MESSAGE CONVENTION. Pattern that is going to be followed is a generic status code response. It will be
    # followed by an optional custom message
    ERROR_MESSAGE = "ERROR: {}. {}"

    # 2XX related message
    LOG_IN_SUCCESS_MESSAGE                      = "Successfully logged in !"
    LOG_OUT_SUCCESS_MESSAGE                     = "Successfully logged out !"
    FOUND_USER_SUCCESS_MESSAGE                  = "Successfully found user !"
    POST_LIKED_SUCCESS_MESSAGE                  = "Post has been liked !"
    POST_UNLIKED_SUCCESS_MESSAGE                = "Post has been unliked !"

    # 4XX related messages

    NO_USERNAME_OR_PASSWORD_ERROR_MESSAGE             = "Username or password not provided"
    USER_NOT_FOUND_ERROR_MESSAGE                      = "User not found"
    USER_ALREADY_EXISTS_ERROR_MESSAGE                 = "User already exists"
    POST_NO_CONTENT_OR_IMG_UPLOAD_ERROR_MESSAGE       = "Post has no content or image has not been uploaded"
    POST_NOT_FOUND_ERROR_MESSAGE                      = "Post not found"
