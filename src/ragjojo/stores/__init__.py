import importlib
import pkgutil

__all__ = []

for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    globals()[module_name] = module
    __all__.append(module_name)

# Just for linter stop crying

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import steamv1
