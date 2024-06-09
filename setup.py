from setuptools import setup


setup(
    name="rename-pdf",
    version="1.0.0",
    author="kaiiy",
    url="https://github.com/kaiiy/rename-pdf",
    license="MIT",
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "rename-pdf=main:main",
        ]
    },
    install_requires=["pypdf2>=3.0.1"],
    python_requires=">=3.11",
)
