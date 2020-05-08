__copyright__ = """
    Copyright 2020 EPFL

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__license__ = "Apache 2.0"

from pathlib import Path
import pytest
import subprocess

example_scripts = (Path(__file__).parent.parent / "examples").glob("[br]*.py")


@pytest.mark.parametrize("script", example_scripts)
def test_example_script(script):
    subprocess.run([script, "--test"], check=True)
