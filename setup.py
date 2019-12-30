from setuptools import setup, find_packages

setup(
        name="key-value-store-cli",
        py_modules=find_packages(),
        install_requires=[
            "Click",
            "requests",
            ],
        entry_points="""
        [console_scripts]
        employee=app:cli
        """,
        )