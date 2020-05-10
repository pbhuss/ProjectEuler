

def fibonacci_generator():
    a = 1
    b = 0

    while True:
        yield a
        b += a
        yield b
        a += b


class MemoizedGenerator(object):

    def __init__(self, generator, start_at=0):
        self.reset(start_at)
        self._generator = generator
        self._mem = []
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._yield_pos += 1
        return self[self._yield_pos]

    def __getitem__(self, item):
        if isinstance(item, int):
            generate_to = item
        elif isinstance(item, slice):
            if item.step is None or item.step > 0:
                generate_to = item.stop - 1
            else:
                generate_to = item.start
        else:
            raise TypeError
        while len(self._mem) <= generate_to:
            self._generate_next()
        return self._mem[item]

    def _generate_next(self):
        val = next(self._generator)
        self._mem.append(val)

    def reset(self, start_at):
        self._yield_pos = start_at - 1
