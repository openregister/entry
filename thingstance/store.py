class Store(object):

    """Interface for storage of Things."""

    def put(self, thing):
        raise NotImplementedError

    def get(self, hash):
        raise NotImplementedError

    def get_latest(self, name=None):
        raise NotImplementedError
