import logging

def setup_logger(debug=False):
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
