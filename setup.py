from pathlib import Path

from setuptools import find_namespace_packages, setup


ROOT = Path(__file__).resolve().parent


def read_requirements():
    requirements = ROOT / "requirements.txt"
    if not requirements.exists():
        return []
    return [
        line.strip()
        for line in requirements.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]


setup(
    name="jarvis-ai-assistant",
    version="0.1.0",
    description="Voice-controlled AI assistant in Python",
    packages=find_namespace_packages(include=["*"]),
    include_package_data=True,
    install_requires=read_requirements(),
)