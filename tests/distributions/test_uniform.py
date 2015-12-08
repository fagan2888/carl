# -*- coding: utf-8 -*-
#
# Carl is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

from numpy.testing import assert_array_almost_equal
import scipy.stats as st
from sklearn.utils import check_random_state
import theano
import theano.tensor as T

from carl.distributions import Uniform


def check_uniform(low, high):
    rng = check_random_state(1)

    p_carl = Uniform(low=low, high=high)
    p_scipy = st.uniform(loc=low, scale=high - low)
    X =  3 * rng.rand(50, 1) - 1

    assert_array_almost_equal(p_carl.pdf(X).ravel(),
                              p_scipy.pdf(X.ravel()))
    assert_array_almost_equal(p_carl.cdf(X).ravel(),
                              p_scipy.cdf(X.ravel()))


def test_uniform():
    for low, high in [(0., 1.), (0., 2.), (1., 5.), (-1., -0.5)]:
        yield check_uniform, low, high
