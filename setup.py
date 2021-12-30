from setuptools import setup

install_requires = [
    "orator==0.9.9",
]

testing_requires = [
    "flake8==4.0.1",
    "isort==5.10.1",
    "mypy==0.930",
]

setup(
    install_requires=install_requires,
    extras_require={
        'test': testing_requires,
    }
)
