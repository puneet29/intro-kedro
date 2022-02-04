"""Example code for the nodes in the example pipeline. This code is meant
just for illustrating basic Kedro features.

Delete this when you start working on your own Kedro project.
"""

from kedro.pipeline import Pipeline, node

from .nodes import split_data, make_scatter_plot


# Edited this for personal learning ---------------------------------------
def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                make_scatter_plot,
                inputs="example_iris_data",
                outputs="iris_scatter_plot@matplotlib",
                name="save_scatter_matplotlib"
            ),
            node(
                # Because we are not in a way transforming the data, we are
                # just changing the encoding of the data while saving
                lambda x : x,
                inputs="iris_scatter_plot@bytes",
                outputs="iris_scatter_plot_64bit",
                name="save_scatter_base64"
            ),
            node(
                split_data,
                ["example_iris_data", "params:example_test_data_ratio"],
                dict(
                    train_x="example_train_x",
                    train_y="example_train_y",
                    test_x="example_test_x",
                    test_y="example_test_y",
                ),
                name="split",
            )
        ]
    )

# -------------------------------------------------------------------------