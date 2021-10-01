from itertools import tee
from os import makedirs, walk, scandir
from os.path import dirname, join

from yaml import dump

from generate_template_from_source import generate_template_from_source

print("Rendering mustache wallpapers")
source_dir = join(dirname(__file__), "..", "sources")
target_dir = join(dirname(__file__), "..", "templates")

print("from {} to {}".format(source_dir, target_dir))

makedirs(target_dir, exist_ok=True)


def source_basename(s):
    return s.name.replace(".svg", "")


with scandir(source_dir) as sources:
    with open(join(target_dir, 'config.yaml'), 'w') as f:
        f.write(dump({source_basename(s): {"extension": ".svg", "output": source_basename(s)} for s in sources}))

with scandir(source_dir) as sources:
    for source_svg in sources:
        print("Rendering {}".format(source_basename(source_svg)))
        with open(join(source_dir, source_svg), 'r') as t:
            generated = generate_template_from_source(t.read())
            with open(join(target_dir, source_basename(source_svg) + ".mustache"), 'w') as g:
                g.write(generated)
