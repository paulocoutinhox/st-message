import setuptools

with open('README.md') as readme_file:
    readme = readme_file.read()


setuptools.setup(
    name="streamlit-message",
    version="0.0.1",
    author="Gamliel Cohen <gamcoh>",
    author_email="cohengamliel8@gmail.com",
    description="A streamlit component, to make chat ui messages",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/gamcoh/st-message",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="chat message ui streamlit streamlit-component",
    python_requires=">=3.8",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
