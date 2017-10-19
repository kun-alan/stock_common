"""
    Patching YahooQuotesReader to get trade date
"""

from collections import defaultdict
import csv

import pandas.compat as compat
from pandas import DataFrame
from pandas_datareader.yahoo.quotes import YahooQuotesReader

_yahoo_codes = {'symbol': 's', 'last': 'l1', 'change_pct': 'p2', 'PE': 'r',
                'time': 't1', 'short_ratio': 's7', 'date': 'd1'}


class MyYahooQuotesReader(YahooQuotesReader):

    """Get current yahoo quote"""

    @property
    def params(self):
        if isinstance(self.symbols, compat.string_types):
            sym_list = self.symbols
        else:
            sym_list = '+'.join(self.symbols)

        # For codes see: http://www.myhow2.net/wp/2013/07/python-how-to-look-up-stock-price-using-yahoo-stock-data-service/
        #
        # Construct the code request string.
        request = ''.join(compat.itervalues(_yahoo_codes))
        params = {'s': sym_list, 'f': request}
        return params

    def _read_lines(self, out):
        data = defaultdict(list)
        header = list(_yahoo_codes.keys())

        for line in csv.reader(out.readlines()):
            for i, field in enumerate(line):
                if field[-2:] == '%"':
                    v = float(field.strip('"%'))
                elif field[0] == '"':
                    v = field.strip('"')
                else:
                    try:
                        v = float(field)
                    except ValueError:
                        v = field
                data[header[i]].append(v)

        idx = data.pop('symbol')
        return DataFrame(data, index=idx)


def get_quote_yahoo(*args, **kwargs):
    return MyYahooQuotesReader(*args, **kwargs).read()
