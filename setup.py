from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Meghna Bajoria',
    isntall_requires=["openai","langchain","streamlit","python-dotenv","PyPDF20"],
    packages=find_packages()
)