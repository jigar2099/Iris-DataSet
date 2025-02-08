from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
      """
      This function will return the list of requirements.
      :param file_path:
      :return:
      """
      requirements = []
      with open(file_path, 'r') as f:
            requirements = f.readlines()
            requirements = [req.replace("\n", "") for req in requirements]
            if HYPHEN_E_DOT in requirements:
                  requirements.remove(HYPHEN_E_DOT)
      return requirements
setup(name='iris',
      version='1.0',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt'))