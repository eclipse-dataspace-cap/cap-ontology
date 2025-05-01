#!/usr/bin/env python

import argparse
import logging
import os
from io import StringIO
from pathlib import Path

import yaml
from markdown import Markdown

from linkml.generators import docgen
from linkml.generators.docgen import DocGenerator

log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# monkey patching Markdown
Markdown.output_formats["plain"] = unmark_element

# saving original function
_enshorten = docgen.enshorten


def enshorten(input: str) -> str:
    if input is None:
        return ""
    __md = Markdown(output_format="plain")
    __md.stripTopLevelTags = False
    return _enshorten(__md.convert(input))


# monkey patching docgen
docgen.enshorten = enshorten


def generate_doc(schema_file: Path, output_directory: Path):
    logger.info(f"Generate documentation with {schema_file}")
    doc_generator = DocGenerator(
        str(schema_file),
        template_directory=template_directory,
        subfolder_type_separation=True,
        useuris=True,
        mergeimports=False,
        log_level=log_level,
    )
    doc_generator.serialize(directory=str(output_directory))


def format_yaml(input_file: Path, output_file: Path, version: str):
    with open(input_file, "r") as f:
        data = yaml.safe_load(f)

    values = {"version": version, "major": version.split(".")[0]}

    # Check and update the 'id' field using format()
    if "id" in data and isinstance(data["id"], str):
        data["id"] = data["id"].format(**values)
    if "cap" in data["prefixes"] and isinstance(data["prefixes"]["cap"], str):
        data["prefixes"]["cap"] = data["prefixes"]["cap"].format(**values)

    # Save the updated YAML back to a file
    os.makedirs(output_file.parent, exist_ok=True)
    with open(output_file, "w") as f:
        yaml.dump(data, f, sort_keys=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ProgramName", description="What the program does", epilog="Text at the bottom of help"
    )
    parser.add_argument("--version", default="0.0.0")
    args = parser.parse_args()

    logger.info(f"Generating files for version {args.version}")

    rootdir = Path(__file__).parent

    schema_file = rootdir / "build" / "conformity_assessment.yml"

    format_yaml(input_file=rootdir / "linkml/conformity_assessment.yml", output_file=schema_file, version=args.version)

    output_directory = rootdir / "docs/ontology"
    template_directory = rootdir / "docgen-template"

    logger.info(f"process file {schema_file}")

    generate_doc(schema_file, output_directory)
