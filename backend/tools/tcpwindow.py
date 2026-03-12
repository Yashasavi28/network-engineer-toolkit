def tcp_window(bandwidth, latency):

    window = bandwidth * latency

    return {
        "bandwidth": bandwidth,
        "latency": latency,
        "window_size": window
    }