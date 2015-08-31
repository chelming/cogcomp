from setuptools import setup, find_packages

setup(
    name="cogcomp",
    packages=['cogcomp'],
    version="1.1.4",
    description="A call stack profiler for Python. Inspired by Apple's Instruments.app",
    author='University of Illinois Cognitive Computation Group',
    author_email='erichorn@illinois.edu',
    url='https://github.com/cwhits/cogcomp',
    keywords=['curator', 'illinois'],
    include_package_data=True,
    entry_points={'console_scripts': ['cogcomp = cogcomp.__main__:main']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Testing',
    ]
)
