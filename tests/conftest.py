import decimal

import pytest


@pytest.fixture(params=[5, 10, 100, 1000])
def precision(request):
    prec = request.param
    with decimal.localcontext() as localcontext:
        localcontext.prec = prec + 1
        yield prec
