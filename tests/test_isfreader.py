import sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '..')

import isfreader
import numpy as np


def test_isfreader():
    data = isfreader.read_file('./T0000CH1.ISF')
    np_data = np.load('./T0000CH1.npy')
    assert data.shape == np_data.shape
    assert data.dtype == np_data.dtype
    assert np.all(data == np_data)

def test_data1():
    data = isfreader.read_file('./data1.ISF')
    assert (10000, 2) == data.shape
    assert np.float == data.dtype


if __name__ == '__main__':
    test_isfreader()
    test_data1()
    print('All tests finished successfully!')
