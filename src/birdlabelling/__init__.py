"""
birdlabelling: Trying out wing marker labelling
"""

from __future__ import annotations

from importlib.metadata import version
from .labelling import myfunction

__all__ = ("__version__", "myfunction")
__version__ = version(__name__)
