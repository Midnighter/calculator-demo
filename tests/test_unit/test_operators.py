# Copyright (c) 2019, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Test the calculator operations."""


import hypothesis.strategies as st
import pytest
from hypothesis import assume, example, given

from demo import operators


@pytest.mark.parametrize("a, b, expected", [(2, 2, 4)])
def test_add(a, b, expected):
    """Test known examples of addition."""
    assert operators.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(4, 2, 2)])
def test_subtract(a, b, expected):
    """Test known examples of subtraction."""
    assert operators.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(2, 2, 4)])
def test_multiply(a, b, expected):
    """Test known examples of multiplication."""
    assert operators.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 1),
        (4, 2, 2),
        pytest.param(
            1, 0, None, marks=pytest.mark.raises(exception=ZeroDivisionError)
        ),
    ],
)
def test_divide(a, b, expected):
    """Test known examples of division."""
    assert operators.divide(a, b) == expected


@given(a=st.integers(), b=st.integers())
def test_divide_int(a, b):
    """Test division on a wide integer domain."""
    assume(b != 0)
    operators.divide(a, b)


@given(a=st.floats(), b=st.floats())
def test_divide_float(a, b):
    """Test division on a wide float domain."""
    assume(b != 0.0)
    operators.divide(a, b)


@given(a=st.floats(), b=st.integers())
@example(a=1.0, b=1)
def test_divide_by_int(a, b):
    """Test that division by an integer maintains a float value."""
    assume(b != 0)
    assert isinstance(operators.divide(a, b), float)
