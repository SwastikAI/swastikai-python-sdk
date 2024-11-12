from setuptools import setup, find_packages

setup(
    name="swastikai",
    version="1.0.4",
    description="Official Python SDK for SwastikAI API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # README format
    url="https://github.com/SwastikAI/swastikai-python-sdk",  # Link to GitHub repo or project homepage
    author="SwastikAI",
    author_email="contact@swastikai.com", # Change this if needed
    packages=find_packages(),
    install_requires=["requests>=2.32.3", "pydantic>=2.9.2"],
    python_requires=">=3.9.12",
)
