**********
ISF Reader
**********

Read Tek scope ISF files as a numpy array.

Installation
============
.. code-block:: bash

    pip install git+https://github.com/jeremitu/isfreader.git

Usage:
======
.. code-block:: python

    import isfreader

    data = isfreader.read_file('T0000CH1.ISF')
    data[:, 0]  # Time column (Does not always start at 0)
    data[:, 1]  # Data (Voltage) column
    print(data.shape)
    print(data.dtype)

    data, header = isfreader.read_file(filename,with_header=True)
    print(header) # dictionary of header values

    data = isfreader.get_isf_file(ip)
    ...
