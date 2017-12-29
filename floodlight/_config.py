import json

# Load config
def load_config(file):
    """Accepts filename and returns config object"""

    config = json.load(open(file))
    for color in config['colors']:
        # Force colors to be tuples, required by fadecandy
        config['colors'][color] = tuple(config['colors'][color])
    return (config)
