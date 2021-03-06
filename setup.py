from setuptools import setup
from setuptools import find_packages
import os

# Utility function to read README.md file for long description
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="syfertext",
    author="Alan Aboudib",
    author_email="agabudeeb@gmail.com",
    description="A privacy preserving NLP framework",
    url="https://github.com/OpenMined/SyferText",
    keywords="nlp smpc secure multi-party computation federated learning deep learning artificial intelligence secure model sharin natural language processing spacy spaCy",
    classifier=["Programming Language :: Python :: 3.6", "Operating System :: OS Independent"],
    license="Apache-2.0",
    version="0.0.1",
    packages=find_packages(),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=[
        "tqdm==4.36.1",
        "mmh3==2.5.1",
        "syft @ git+https://github.com/OpenMined/PySyft@bc5337507047b325e79cb9b2060abac4bdc08f3f",
        "requests==2.22.0",
    ],
    extras_require={
        "test": [
            "black>=19.10b0",
            "pytest>=5.3.5",
            "pytest-black>=0.3.8",
            "jupyter>=1.0.0",
            "papermill>=1.2.1",
        ]
    },
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent"],
)
