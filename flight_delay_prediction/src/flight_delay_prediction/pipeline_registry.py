"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, node
from .pipelines.nodes import partition_by_day, partition_calc


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {
        "__default__": Pipeline([
            # Uncomment below block of code to run partition dataset
            # node(partition_by_day,
            #      "ontime_2019",
            #      "ontime_2019_by_day",
            #      name="partition"),
            node(partition_by_day,
                 "ontime_2019",
                 "ontime_2019_incremental",
                 name="incremental"),
            node(partition_calc,
                 "ontime_2019_incremental",
                 "ontime_2019_calc",
                 name="calc",
                 # Confirms if the incremental dataset has completed successfully
                 confirms="ontime_2019_incremental")
        ])
    }
