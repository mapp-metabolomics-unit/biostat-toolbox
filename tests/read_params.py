from biostat_toolbox.params import load_yaml


def test_load_yaml():
    params = load_yaml("tests/test_params.yaml")
    assert params["actions"]["run_with_gap_filled"] == False
