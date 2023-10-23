import yfinance as yf
import pandas as pd
from io import StringIO

def fetch_data(symbols, start, end, interval):
    sym_string = " ".join(symbols)
    data = yf.download(sym_string, start=start, end=end,interval=interval)
    return data

def mk_positions(data, portfolio):
    positions = pd.DataFrame(index=data.index)
    for (sym, shares) in portfolio.items():
        positions[sym] = data["Adj Close"][sym] * shares
    positions["Total"] = positions.sum(axis=1)
    return positions

def mk_gains(positions, portfolio):
    percentage_change = pd.DataFrame(index=positions.index)
    percentage_change["Total"] = 100 * (1 - positions["Total"].shift(1) / positions["Total"])
    for (sym) in portfolio.keys():
        percentage_change[sym] = 100 * (1 - positions[sym].shift(1) / positions[sym])
    return percentage_change

def to_csv(data, dec_format = "{:,.2f}%"):
    out_buffer = StringIO()
    data.to_csv(out_buffer,float_format = dec_format.format)
    return out_buffer.getvalue()