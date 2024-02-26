from abc import ABC, abstractmethod
from .IRegistry import IRegistry
from ..RegistryPermission import RegistryPermission


class IRegistryFactory(ABC):
    """
    Abstract base class defining a factory for creating instances of IRegistry.
    """

    @abstractmethod
    def get(self, name: str, permissions: RegistryPermission) -> IRegistry:
        """Abstract method for getting an instance of IRegistry."""
        pass