import os
import fnmatch
from pathlib import Path
from typing import List
from contextlib import contextmanager


def find_notebooks(directories: List[str], exclude_list: List[str] = []) -> List[str]:
    """
    Find jupyter notebooks in a list of paths.
    
    Args:
        directories: List of paths to dirs and files.
        exclude_list: List of globs to exclude.
    
    """

    
    filenames = []

    for fn in directories:

        fn = Path(fn)

        if not fn.is_dir():
            if fn.suffix == ".ipynb" and not is_excluded(fn, exclude_list):
                filenames.append(str(path))
                continue



        notebooks = [str(f) for f in fn.glob("**/*.ipynb") if not f.suffix == ".ipynb_checkpoints"]
        notebooks = [f for f in notebooks if not is_excluded(f, exclude_list)]

        filenames += notebooks
        
    return filenames



def is_excluded(src_path: str, globs: List[str]) -> bool:
    """
    Determine if a src_path should be excluded.
    
    Supports globs (e.g. folder/* or *.md).
    Credits: code inspired by / adapted from
    https://github.com/apenwarr/mkdocs-exclude/blob/master/mkdocs_exclude/plugin.py

    Args:
        src_path (src): Path of file
        globs (list): list of globs
    
    Returns:
        (bool): whether src_path should be excluded
    """
    if not isinstance(src_path, str):
        src_path = str(src_path)
    
    assert isinstance(globs, list)

    for g in globs:
        if fnmatch.fnmatchcase(src_path, g):
            return True

        # Windows reports filenames as eg.  a\\b\\c instead of a/b/c.
        # To make the same globs/regexes match filenames on Windows and
        # other OSes, let's try matching against converted filenames.
        # On the other hand, Unix actually allows filenames to contain
        # literal \\ characters (although it is rare), so we won't
        # always convert them.  We only convert if os.sep reports
        # something unusual.  Conversely, some future mkdocs might
        # report Windows filenames using / separators regardless of
        # os.sep, so we *always* test with / above.
        if os.sep != "/":
            src_path_fix = src_path.replace(os.sep, "/")
            if fnmatch.fnmatchcase(src_path_fix, g):
                return True

    return False


@contextmanager
def working_directory(path):
    """
    Temporarily change working directory.
    A context manager which changes the working directory to the given
    path, and then changes it back to its previous value on exit.
    Usage:
    ```python
    # Do something in original directory
    with working_directory('/my/new/path'):
        # Do something in new directory
    # Back to old directory
    ```
    """
    prev_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)
