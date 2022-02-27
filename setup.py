from setuptools import setup

setup(
    name='pyteddy',
    version='0.0.2',
    description='Python project manager',
    long_description='README.md',
    long_description_content_type='text/markdown',
    url='https://github.com/spralja/pyteddy',
    author='Robert Spralja',
    author_email='robert.spralja@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    packages=['pyteddy'],
    include_package_data=False,
    entry_points={
        'console_script': [
            'pyteddy=pyteddy.__main__:main'
        ]
    },
)