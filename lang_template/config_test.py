# Copyright apache-2-0
#
# This source code is licensed under the Apache-2.0 License
# found in the LICENSE file in the root directory of this source tree.

import glob
import io
import subprocess

import lang_template


def test_version() -> None:
    assert lang_template.__version__


def test_copyright() -> None:
    """Check that source code files contain a copyright line"""
    for fname in glob.glob("lang_template/**/*.py", recursive=True):
        print("Checking " + fname + " for copyright header")

        with open(fname) as f:
            for line in f.readlines():
                if not line.strip():
                    continue
                assert line.startswith("# Copyright")
                break


def test_about() -> None:
    out = io.StringIO()
    lang_template.about(out)
    print(out)


def test_about_main() -> None:
    rval = subprocess.call(["python", "-m", "lang_template.about"])
    assert rval == 0
