from distutils.core import setup

setup(
    name='Clockwork',
    version='1.0',
    packages=['clockwork'],
    install_requires=['lxml'],
    license='MIT',
    author='Mediaburst',
    author_email='hello@clockworksms.com',
    long_description=open('README.md').read(),
    description='Python wrapper for the clockwork SMS Api',
    url='https://github.com/mediaburst/clockwork-python'
)