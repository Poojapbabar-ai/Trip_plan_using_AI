from pathlib import Path
from typing import List

from setuptools import find_packages, setup


def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    """Return project dependencies from the requirements file."""
    requirements_list: List[str] = []
    file_path_obj = Path(__file__).resolve().parent / file_path

    try:
        with file_path_obj.open("r", encoding="utf-8") as file:
            for line in file:
                requirement = line.strip()
                if requirement and not requirement.startswith("#") and requirement != "-e .":
                    requirements_list.append(requirement)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Error: The file '{file_path_obj}' was not found.") from exc

    return requirements_list


setup(
    name="AI_Trip_Planner",
    version="0.0.1",
    author="Pooja Babar",
    author_email="babarpooja2002@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)