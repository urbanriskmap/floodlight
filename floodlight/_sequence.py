"""Construct sequences of light patterns"""
from _pattern import Pattern


class Sequence():
    """Build light event sequences using Pattern class"""
    def __init__(self, config):
        """Accpets config returns Sequence class"""
        self.config = config
        self.pattern = Pattern(config)

    def online(self):
        """Returns online sequence"""
        # heartbeat
        sequence = [{'pattern': self.pattern.online(), 'timing': 0.1}]
        sequence.append({'pattern': self.pattern.online(), 'timing': 0})
        return (sequence)

    def error(self):
        return ([{'pattern': self.pattern.error(), 'timing': 0}])

    def flood(self, count):
        # heartbeat
        sequence = [{'pattern': self.pattern.online(), 'timing': 0.1}]
        sequence.append({'pattern': self.pattern.flood(count), 'timing': 0})
        return (sequence)

    def rainfall(self, count):
        """Raindrop animation method"""
        # Get raindrop from pattern
        sequence = []
        sequence.append({'pattern': self.pattern.new_report, 'timing': 2})
        sequence.append({'pattern': self.pattern.flood(count), 'timing': 0})
        return sequence

    def build(self, last_count, new_count):
        """Accepts previous and new report counts, returns light sequence"""

        # Logic to set sequence based on latest report count
        if new_count == 0:
            return (self.online())
        elif new_count > last_count:
            return (self.rainfall(new_count))
        elif new_count > 0:
            return (self.flood(new_count))
        else:
            return (self.error())
