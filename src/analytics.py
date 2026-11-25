def align_prices(instrument, benchmark):
    dates = sorted(
        set(row["date"] for row in instrument)
        & set(row["date"] for row in benchmark)
    )

    i = {row["date"]: float(row["close"]) for row in instrument}
    b = {row["date"]: float(row["close"]) for row in benchmark}

    if len(dates) < 2:
        raise ValueError("Not enough common dates")

    return dates, [i[d] for d in dates], [b[d] for d in dates]


def period_return(prices):
    return prices[-1] / prices[0] - 1


def base_100(prices):
    return [100 * p / prices[0] for p in prices]


def relative_performance(instrument, benchmark):
    return period_return(instrument) - period_return(benchmark)
