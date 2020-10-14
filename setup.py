from distutils.core import setup
setup(
    name='knowru_client',
    packages=['knowru_client'],
    version='0.2',
    description='Client to run runnables in Knowru',
    author='Knowru, LLC',
    author_email='hello@knowru.com',
    license='MIT',
    url='https://github.com/knowru/knowru_client',
    download_url='https://github.com/knowru/knowru_client/archive/0.2.zip',
    keywords='knowru client',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=['requests', 'timezone_logging']
)
