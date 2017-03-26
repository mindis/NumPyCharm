# NumPyCharm
## [Yoav Ram | Python Training](http://python.yoavram.com)

This repo contains some simple Python code to show the integation between [PyCharm](https://www.jetbrains.com/pycharm/) and Scientific Python tools:

- [NumPy](http://numpy.org) & [matplotlib](http://matplotlib.org), see `np_example.py`:
    - set breakpoint on line 5
    - run in debug mode (green beetle)
    - step over definition of `X`
    - right click `X` in the _Variables_ window at the bottom
    - Choose `View as array` to open a _Data View_ window
    - Note how the figure window causes the run to halt; to avoid that, add the argument `block=False` to `plt.show` (but then the figure window cannot be viewed).
- [Cython](http://cython.org) - support for Cython in PyCharm is limited to editing code (rather than compiling and running it) and is only available in PyCharm Professional.
  - `primes.pyx` defines a new Cython function that returns `n` first primes
   - `setup.py` contains neccessary definitions to build the Cython extension: use _Tools->Run setup.py task..._,
   choose `build_ext` and add the parameter `--inplace` (otherwise the Cython extension will only be available when installing the package).
   - Once the extension (`pyx` file) is compiled `dll`/`so` file), you can test it with `test_primes.py`:
   Right click the project name and choose _Run NoseTests in ..._.
   - `timeit_primes.py` demontrates how to time both Python function (`primes`) and Cython functions (`cprimes`, imported from the `primes` module).
- [Jupyter notebook](http://jupyter.org)
   - PyCharm supports viewing of Jupyter notebooks.
   - Start a notebook server by typing in a terminal (can be a PyCharm terminal): `jupyter notebook`
   - Note that when the notebook server starts it will display a message, look for the `...token=` in the message and copy the token (the text after `token`).
   - Open `notebook.ipynb`
   - If required, paste that token you copied from the terminal.
   - You can run cells with the play button, etc.

# Dependencies

- numpy
- matplotlib
- cython
- nose
- ipykernel
- jupyter notebook

# License

[CC-BY-SA 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)