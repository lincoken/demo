from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()
    
    from os import path
    setup(name='demo',
          version='0.0.1',
          description='Basis expansion for 1D quantum potential.',
          long_description= "" if not path.isfile("README.md") else read_md('README.md'),
          author='Jeremy J Jorgensen',
          author_email='jerjorg@gmail.com',
          url='https://github.com/jerjorg/782',
          license='MIT',
          setup_requires=['pytest-runner',],
          tests_require=['pytest', 'python-coveralls'],
          install_requires=[
              "argparse",
              "termcolor",
              "numpy",
              "matplotlib",
          ],
          packages=['demo'],
          include_package_data=True,
          classifiers=[
              'Development Status :: 2 - Pre-Alpha',
              'Intended Audience :: Science/Research',
              'Natural Language :: English',
              'Operating System :: MacOS',
              'Programming Language :: Python',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.5',
          ],
    )
