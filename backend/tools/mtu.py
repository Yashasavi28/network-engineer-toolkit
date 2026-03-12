def mtu_calculator(mtu):

    mss = mtu - 40

    return {
        "mtu": mtu,
        "mss": mss
    }