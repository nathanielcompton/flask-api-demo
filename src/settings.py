FLASK_LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {"format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",}
    },
    "handlers": {
        "wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://flask.logging.wsgi_errors_stream",
            "formatter": "default",
        }
    },
    "root": {"level": "DEBUG", "handlers": ["wsgi"]},
}

FLOAT_FORMAT = ":.2f"

REQ_LIST = ["length", "width", "height", "weight", "quantity"]

VEH_CPT = "Compact"
VEH_SDN = "Sedan"
VEH_VAN = "Van"
VEH_TRK = "Truck"
NO_FIT_FOUND = "No vehicle found to fit the given item list!"
