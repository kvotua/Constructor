from app.registry import IRegistry

from ..NodeService.INodeService import INodeService
from ..NodeService.schemas import NodeTreeSchema
from ..NodeService.schemas.NodeId import NodeId
from .ITemplateService import ITemplateService
from .schemas.TemplateId import TemplateId
from .schemas.TemplateSchema import TemplateSchema
from .schemas.TemplateView import TemplateView


class TemplateService(ITemplateService):
    __node_service: INodeService
    __registry: IRegistry

    def __init__(self, registry: IRegistry) -> None:
        self.__registry = registry

    async def inject_dependencies(self, node_service: INodeService) -> None:
        self.__node_service = node_service
        await self.__prepopulate()

    async def get_all(self) -> list[TemplateId]:
        # TODO: docstring
        return [TemplateSchema(**template).id for template in self.__registry.read({})]

    async def get(self, template_id: TemplateId) -> TemplateView:
        # TODO: docstring
        result = self.__registry.read({"id": template_id})
        if len(result) < 1:
            raise ValueError("Wrong template id")
        template = TemplateSchema(**result[0])
        tree = await self.__node_service.get_tree(template.root_node_id)
        return TemplateView(id=template.id, tree=tree)

    async def create(self, node_id: NodeId) -> TemplateId:
        # TODO: docstring
        tree = await self.__node_service.get_tree(node_id)
        copied_tree = await self.__deep_copy(tree)
        template = TemplateSchema(root_node_id=copied_tree.id)
        self.__registry.create(template.model_dump())
        return template.id

    async def instantiate(self, template_id: TemplateId) -> NodeTreeSchema:
        # TODO: docstring
        root_node_id = await self.__get_root_node_id(template_id)
        tree = await self.__node_service.get_tree(root_node_id)
        copied_tree = await self.__deep_copy(tree)
        return copied_tree

    async def __deep_copy(self, tree: NodeTreeSchema) -> NodeTreeSchema:
        # TODO: docstring
        copied_tree = tree.model_copy(deep=True)
        root_id = await self.__node_service.create(parent_id=None)
        copied_tree.id = root_id
        stack = [(root_id, child) for child in copied_tree.children]
        while len(stack) > 0:
            parent_id, current = stack.pop()
            current.id = await self.__node_service.create(parent_id)
            stack.extend([(current.id, child) for child in current.children])
        return copied_tree

    async def __get_root_node_id(self, templte_id: TemplateId) -> NodeId:
        # TODO: docstring
        result = self.__registry.read({"id": templte_id})
        if len(result) < 1:
            raise ValueError("Wrong template id")
        template = TemplateSchema(**result[0])
        return template.root_node_id

    async def __prepopulate(self) -> None:
        # TODO: docstring
        root_id = await self.__node_service.create(parent_id=None)
        await self.create(root_id)