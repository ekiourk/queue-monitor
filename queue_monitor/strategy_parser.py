import yaml


class StrategyParser(object):
    def __init__(self, filename):
        data = yaml.load(open(filename, 'r'))

        # put the dictionary keys as the properties of the object
        self.__dict__.update(data)
