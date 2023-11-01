import setuptools

#this is usefull for if we publish as a pypl package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-Deep-Learning-Project-AWS-Mlflow-DVC"
AUTHOR_USER_NAME = "shalidesh"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "sdeshan970@gmail.com"


setuptools.setup(
    #we set cnnClassifier as a local package of our project.we can use all folders inside the that,without mension src folder
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)