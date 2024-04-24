import os
import subprocess
from typing import Optional

from exemplify.steps.base import Step, register


@register("pip")
class Pip(Step):
    def __init__(
        self, meta: dict, packages: str | list[str], pip_path: Optional[str] = None
    ) -> None:
        if isinstance(packages, str):
            packages = [packages]
        self.packages = packages

        pip_path = pip_path or "~/.pyenv/shims/pip"
        self.pip = os.path.expanduser(pip_path)

    def sync(self) -> None:
        subprocess.check_call([self.pip, "install", "--upgrade"] + self.packages)

    def __str__(self):
        return f"PIP INSTALL {', '.join(self.packages)}"
