

class BaseImageFile(object):
    '''
    Images utils here ....
    '''
    def exists(self):
        raise NotImplemented()

    @property
    def width(self):
        return self.size[0]
    x = width

    @property
    def height(self):
        return self.size[1]
    y = height

    def is_portrait(self):
        return self.y > self.x

    @property
    def ratio(self):
        return float(self.x) / self.y

    @property
    def url(self):
        raise NotImplemented()
    #src = url