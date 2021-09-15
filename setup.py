import setuptools


with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().splitlines()


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="webopencv",
    version="0.0.4",
    author="Alvin Wan",
    author_email="hi@alvinwan.com",
    description="Stream live video feed from a webpage to a server-side python openCV script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD",
    url="https://github.com/alvinwan/webopencv",
    project_urls={
        "Bug Tracker": "https://github.com/alvinwan/webopencv/issues",
    },
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["webopencv"],
    include_package_data=True,
    python_requires=">=3.6",
)