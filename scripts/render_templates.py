from os import makedirs, walk, scandir
from os.path import dirname, join

from yaml import dump

from generate_template_from_source import generate_template_from_source

print("Rendering mustache wallpapers")

source_dir = join(dirname(__file__), "..", "sources")
target_dir = join(dirname(__file__), "..", "templates")

makedirs(target_dir, exist_ok=True)


with scandir(source_dir) as sources:

    name = sources.name.replace(".svg", "")

    print(
        dump({name: {"extension": ".svg", "output": name} for s in sources}),
        file=open(join(target_dir, 'config.yaml'), 'w')
    )

    for source_svg in sources:
        with open(join(source_dir, source_svg), 'r') as t:
            generated = generate_template_from_source(t.read())
            with open(join(target_dir, name + ".mustache"), 'w') as g:
                g.write(generated)

