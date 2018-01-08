import json

log_levels = {"DEBUG": 10, "INFO": 20}


# Load config
def load_config(file):
    """Accepts filename and returns config object"""

    config = json.load(open(file))

    # Force colors to be tuples, required by fadecandy
    for color in config['colors']:
        config['colors'][color] = tuple(config['colors'][color])

    # Fix the python log level insanity
    config['logfile']['level'] = log_levels[config['logfile']['level']]
    return (config)
