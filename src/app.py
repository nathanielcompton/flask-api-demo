from flask import Flask, request, abort
from logging.config import dictConfig

from .sizing_tools import find_best_fit
from .settings import FLASK_LOGGING_CONFIG
from .request_utils import validate_request

dictConfig(FLASK_LOGGING_CONFIG)
app = Flask(__name__)


@app.route("/sanity", methods=["GET"])
def sanity_check():
    app.logger.info(f"Sanity check logger test!")
    return f"This is a sanity check!", 200


@app.route("/vehicle_size", methods=["POST"])
def find_best_vehicle():
    """
    Ideally, there should be several tools or services in front of this endpoint
    (e.g. authentication, authorization, rate limiting etc.)
    For the sake of this demo, we can assume the user has passed all these checks.
    """
    if request.method != "POST":
        return abort(404, "Invalid request method")
    else:
        request_data = request.get_json()
        app.logger.info(f"Received request data: {request_data}")
        try:
            validated_data = validate_request(request_data)
            best_fit = find_best_fit(validated_data)
            return best_fit, 200
        except (KeyError, ValueError) as e:
            abort(400, e)
