from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''This function will return the list of requirements'''
    with open(file_path, 'r') as f:
        requirements = [line.strip() for line in f if line.strip()]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Tp',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)