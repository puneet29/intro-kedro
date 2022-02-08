"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, node
from .pipelines.nodes import partition_by_day


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {
        "__default__": Pipeline([
            node(partition_by_day, "ontime_2019", "ontime_2019_by_day")
        ])
    }
