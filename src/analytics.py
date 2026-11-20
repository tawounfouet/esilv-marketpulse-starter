"""MarketPulse analytics: pure functions for comparison (TD07)."""


def index_by_date(prices):
    raise NotImplementedError


def align_series(instrument_prices, benchmark_prices):
    raise NotImplementedError


def calculate_period_return(prices):
    raise NotImplementedError


def calculate_base_100(prices):
    raise NotImplementedError


def calculate_relative_performance(instrument_return, benchmark_return):
    raise NotImplementedError