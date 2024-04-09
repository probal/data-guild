from setuptools import setup, find_packages

# Function to read the lines of the requirements.txt file
def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

setup(
    name='prefect_hands_on',
    version='0.1.0',
    url='https://github.com/your_username/your_project_name',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),
    install_requires=read_requirements(),
)