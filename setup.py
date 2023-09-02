import setuptools

with open ("README.md",'r',encoding='utf-8') as f :
    long_desc=f.read()

__version__='0.0.0'
AUTHORS_NAME1 ='Devanshi-Joshi '
AUTHORS_NAME2= 'Mukundan'
SRC_REPO='text-summarizer'

setuptools.setup(

    name=SRC_REPO,
    version=__version__,
    author=AUTHORS_NAME1,
    description='a package for txt-summarization built using transformers as its core',

    url=f"https://github.com/'{AUTHORS_NAME1}/{SRC_REPO}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)