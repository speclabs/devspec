from pathlib import Path
from shutil import copytree

from setuptools import setup
from setuptools.command.build_py import build_py as BuildPy


class BuildFrameworkAssets(BuildPy):
    def run(self) -> None:
        super().run()
        source = Path(__file__).parent / "devspec"
        destination = Path(self.build_lib) / "devspec" / "_assets" / "devspec"
        copytree(source, destination, dirs_exist_ok=True)


setup(cmdclass={"build_py": BuildFrameworkAssets})