from unittest import TestCase
from os import path

color_dict = {
    "1d1f21": "base00-hex",
    "282a2e": "base01-hex",
    "373b41": "base02-hex",
    "969896": "base03-hex",
    "b4b7b4": "base04-hex",
    "c5c8cf": "base05-hex",
    "e0e0e0": "base06-hex",
    "ffffff": "base07-hex",
    "cc6666": "base08-hex",
    "de935f": "base09-hex",
    "f0c674": "base0A-hex",
    "b5bd68": "base0B-hex",
    "8abeb7": "base0C-hex",
    "81a2be": "base0D-hex",
    "b294bb": "base0E-hex",
    "a3685a": "base0F-hex",
}


def generate_template_from_source(
        template
):
    build_template = template
    for key, value in color_dict.items():
        build_template = build_template.replace(key, "{{" + value + "}}")
    return build_template


class TestBuild(TestCase):

    def test_functional(self):
        self.maxDiff = None
        with open(path.join(path.dirname(__file__), "test-data", "test.svg"), 'r') as f:
            generated = generate_template_from_source(f.read())
            with open(path.join(path.dirname(__file__), "test-data", "test.expected.mustache"), 'r') as e:
                self.assertEquals(generated, e.read())
