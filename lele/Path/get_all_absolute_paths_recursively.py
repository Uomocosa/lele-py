import lele
from lele.Path import P
import os
from pathlib import Path
from loguru import logger

def get_all_absolute_paths_recursively(starting_path, max_depth=None):
    starting_path = P(starting_path)
    assert starting_path.exists()
    if not max_depth: return fast(starting_path)
    else: return custom(starting_path, max_depth)


def fast(starting_path):
    return list(starting_path.rglob("*"))


def custom(starting_path, max_depth):
    def recursive_function(path, out_list):
        out_list.append(path)
        if not os.path.isdir(path): return
        for name in os.listdir(path):
            new_path = path / name
            recursive_function(new_path, out_list)

    def recursive_function_2(path, out_list, max_depth):
        out_list.append(path)
        if not os.path.isdir(path): return
        if max_depth <= 0: return
        for name in os.listdir(path):
            new_path = path / name
            max_depth -= 1
            recursive_function_2(new_path, out_list, max_depth)

    out_list = list()
    if max_depth: recursive_function_2(starting_path, out_list, max_depth)
    else: recursive_function(starting_path, out_list)
    return out_list

import pytest
@pytest.mark.above10s
def test_fast():
    from lele.Metaprogramming import try_import
    myvars = try_import("lele.__my_variables__")
    if myvars:
        starting_path = myvars.synchting_Path / "Obsidian Vaults"
        logger.debug(f"starting_path: '{starting_path}'")
        out = get_all_absolute_paths_recursively(starting_path) 
        logger.debug(len(out))
        assert len(out) > 0

def test_custom():
    from lele.Metaprogramming import try_import
    myvars = try_import("lele.__my_variables__")
    if myvars:
        starting_path = myvars.synchting_Path / "Obsidian Vaults"
        logger.debug(f"starting_path: '{starting_path}'")
        out = get_all_absolute_paths_recursively(starting_path, max_depth = 3)
        logger.debug(len(out))
        assert len(out) > 0
