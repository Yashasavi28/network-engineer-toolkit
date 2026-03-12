def latency_calc(distance):

    speed = 200000

    latency = distance / speed

    return {
        "distance_km": distance,
        "latency_ms": latency * 1000
    }