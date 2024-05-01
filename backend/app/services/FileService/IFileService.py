from abc import ABC, abstractmethod

from fastapi import UploadFile


class IFileService(ABC):

    @abstractmethod
    async def add_file(
        self,
        file: UploadFile,
        allowed_formats: tuple,
        file_name: str,
    ) -> None:
        pass

    @abstractmethod
    async def remove_file(self, file_name: str) -> None:
        pass

    @abstractmethod
    async def exists(self, file_name: str) -> bool:
        pass