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
    data, header = isfreader.read_file('./data1.ISF', with_header = True)
    assert (10000, 2) == data.shape
    assert np.float == data.dtype
    #print(header)
    assert 10000 == header['NR_PT']

def test_get_data():
    # This test requires connected instrument.
    ip = '192.168.101.22'
    data, header = isfreader.get_isf_data(ip, channel = 'math', filename = "test.isf", with_header = True)
    print(header)
    assert (100000, 2) == data.shape


if __name__ == '__main__':
    test_isfreader()
    test_data1()
    #test_get_data()
    print('All tests finished successfully!')
