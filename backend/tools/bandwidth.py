def bandwidth_calc(size, speed):

    time = size / speed

    return {
        "size": size,
        "speed": speed,
        "seconds": time
    }