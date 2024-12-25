'''Will be useful for creating this whole ML project as a package and probably 
 deploy it in PyPi if needed'''

from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirememnts=file_obj.readlines()
        requirememnts=[req.replace ("\n","")for req in requirememnts]
        
        if HYPEN_E_DOT in requirememnts:
            requirememnts.remove(HYPEN_E_DOT)

    return requirememnts
setup(
 name='e2e_ml_project',
    version='0.0.1',
    author='Sathvik Divili',
    author_email='divilisathvik@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)