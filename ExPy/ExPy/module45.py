"""Word Finder"""

import os
import json

def _load_configuration():
    """Load the configured replacements"""
    with open('module45.json') as jsonhandle:
        return json.load(jsonhandle)

def _read_in_dir():
    """Return list of file names and contents in the module45/in directory"""
    in_path = os.path.join('module45', 'in')
    for file in os.listdir(in_path):
        with open(os.path.join(in_path, file)) as filehandle:
            contents = filehandle.read()
            yield (file, contents)

def _write_out_dir(file_content_pairs):
    """Write sequence of file name and content pairs the module45/out directory"""
    for name, content in file_content_pairs:
        with open(os.path.join('module45', 'out', name), 'w') as filehandle:
            filehandle.write(content)

def _transform_dir(replacements, file_content_pairs):
    """Given a dictionary of replacements (key to find, value to replace)
    and a sequence of file name and content pairs
    Produce a sequence of file name, content, replacement count triples
    """
    for name, content in file_content_pairs:
        replaced_content = content
        replaced = {}
        for find, replace in replacements.items():
            replaced[find] = content.count(find)
            replaced_content = replaced_content.replace(find, replace)
        yield (name, replaced_content, replaced)


def ex45():
    """Find replace all text in all files in module45/in directory
    Write the replaced text to module45.out directory
    """
    replacements = _load_configuration()
    file_content_pairs = _read_in_dir()
    transformed_triple = _transform_dir(replacements, file_content_pairs)

    transformed_pair = []
    for name, content, replaced in transformed_triple:
        print(name)
        for replace, count in replaced.items():
            print('{}: {}'.format(replace, count))
        print()
        transformed_pair.append((name, content))

    _write_out_dir(transformed_pair)

if __name__ == '__main__':
    ex45()
