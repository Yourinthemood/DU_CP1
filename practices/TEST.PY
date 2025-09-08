(lambda f: (lambda x: f(f, x))(
    lambda g, y: [
        (lambda z: z.decode('utf-8'))(
            bytes([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100])
        )
        for _ in [0]
    ][0]
))(lambda f, x: x)