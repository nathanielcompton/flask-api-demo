import logging
from typing import List, Dict
from .settings import REQ_LIST

logger = logging.getLogger()


def validate_request(request_data: List[Dict]) -> List[Dict]:
    """
    Check incoming request for malformed keys, incorrect/missing values, etc.

    This homegrown validator obviously won't scale well compared to existing
    libraries, and is intended only for demonstration purposes.

    Args:
        request_data: Incoming Flask request data, a List of dicts to be validated.
        These are yet-to-be instantiated shipment item objects.

    Returns:
        The validated request data

    Raises:
        KeyError: If malformed keys in Flask request object data
        ValueError: If the object's data doesn't meet requirements
    """
    logger.debug(f"Validating data for request object: {request_data}")
    for entry in request_data:
        if not all(key in REQ_LIST for key in entry.keys()):
            logger.warning(f"KeyError in request data")
            raise KeyError(f"Malformed item keys in: {entry}")
        if not all(isinstance(v, (float, int)) for k, v in entry.items()):
            logger.warning(f"ValueError in request data")
            raise ValueError(f"Incorrect value type(s) in: {entry}")
        if any(v <= 0 for k, v in entry.items()):
            logger.warning(f"ValueError in request data")
            raise ValueError(f"All values must be positive in: {entry}")
    return request_data
