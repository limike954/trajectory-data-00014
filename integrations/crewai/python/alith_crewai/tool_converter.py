"""Tool converters between Alith and CrewAI."""

from typing import Any

from alith import Tool
from pydantic import BaseModel, ConfigDict, create_model

try:
    from crewai.tools import BaseTool as CrewAIBaseTool
except ImportError:
    CrewAIBaseTool = None


def _stringify_result(result: Any) -> str:
    if isinstance(result, str):
        return result
    return str(result)


def _copy_args_schema(args_schema: type[BaseModel] | None, name: str) -> type[BaseModel] | None:
    if args_schema is None:
        return None

    fields: dict[str, tuple[Any, Any]] = {}
    for field_name, field in args_schema.model_fields.items():
        annotation = field.annotation if field.annotation is not None else Any
        default = ... if field.is_required() else field.default
        fields[field_name] = (annotation, default)

    return create_model(f"{name}ArgsSchema", **fields)


if CrewAIBaseTool is not None:

    class _AlithCrewAITool(CrewAIBaseTool):
        alith_tool: Tool

        def _run(self, **kwargs: Any) -> str:
            return _stringify_result(self.alith_tool.handler(**kwargs))

else:

    class _AlithCrewAITool(BaseModel):
        name: str
        description: str
        args_schema: type[BaseModel] | None = None
        alith_tool: Tool

        model_config = ConfigDict(arbitrary_types_allowed=True)

        def _run(self, **kwargs: Any) -> str:
            return _stringify_result(self.alith_tool.handler(**kwargs))

        def run(self, **kwargs: Any) -> str:
            return self._run(**kwargs)


def convert_alith_tool_to_crewai(alith_tool):
    """Convert an Alith Tool to a CrewAI-compatible tool."""
    return _AlithCrewAITool(
        name=alith_tool.name,
        description=alith_tool.description,
        args_schema=_copy_args_schema(alith_tool.parameters, alith_tool.name),
        alith_tool=alith_tool,
    )


def convert_crewai_tool_to_alith(crewai_tool):
    """Convert a CrewAI tool to an Alith Tool."""
    args_schema = getattr(crewai_tool, "args_schema", None)

    def handler(**kwargs: Any) -> str:
        return _stringify_result(crewai_tool._run(**kwargs))

    return Tool(
        name=crewai_tool.name,
        description=crewai_tool.description,
        parameters=args_schema,
        handler=handler,
    )


__all__ = ["convert_alith_tool_to_crewai", "convert_crewai_tool_to_alith"]
