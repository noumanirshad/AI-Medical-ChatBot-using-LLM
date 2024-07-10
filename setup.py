import setuptools

__version__ = "0.0.1"

hy_e = '-e .'

def get_requirements(path: str):
    '''Returns a list of requirements'''
    requirement = []
    with open(path, 'r') as f: 
        requirement = f.readlines()
        requirement = [req.replace('\n', '') for req in requirement]
        if hy_e in requirement:
            requirement.remove(hy_e)
    return requirement


REPO_NAME = "AI-Medical-ChatBot-using-LLM"
AUTHOR_USER_NAME = "NOUMAN IRSHAD"
SRC_REPO = "AI-Medical-ChatBot-using-LLM"
AUTHOR_EMAIL = "noumanirshad564@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME, 
    author_email= AUTHOR_EMAIL,
    description="A AI python package for AI application",
    long_description='long_description',
    long_description_content= "text/markdown",
    url = f"https://github.com/noumanirshad/AI-Medical-ChatBot-using-LLM",
    project_urls = {
        "Bug Tracker": f"https://github.com/noumanirshad/AI-Medical-ChatBot-using-LLM/issues",
    },
    python_requires='>=3.9.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: AI Engineer',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    license="MMIT License",
    include_package_data=True,
    install_requires= get_requirements('requirements.txt'),
    zip_safe=False,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)