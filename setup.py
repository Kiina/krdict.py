from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name = "krdict.py",
        packages=find_packages(),
        python_requires=">= 3.5",
        include_package_data=True,
        install_requires=[
            "cssselect",
            "requests",
        ],
        license="MIT",
    )
