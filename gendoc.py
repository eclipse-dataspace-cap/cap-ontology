#!/usr/bin/env python
import argparse
import logging
import os
from pathlib import Path

import yaml

from linkml.generators import docgen
from linkml.generators.docgen import DocGenerator

log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def enshorten(input: str) -> str:
    return (input or "").replace("\n", " ")  # to avoid breaking markdown table syntax


# monkey patching docgen to have full rendered documentation
docgen.enshorten = enshorten


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
    schema_file = rootdir / "build" / "cap.yaml"
    format_yaml(input_file=rootdir / "linkml/cap.yaml", output_file=schema_file, version=args.version)

    logger.info(f"process file {schema_file}")
    doc_generator = DocGenerator(
        str(schema_file),
        subfolder_type_separation=True,
        # use_slot_uris=True,
        # use_class_uri=True,
        # useuris=True,
        mergeimports=False,
        log_level=log_level,
    )
    doc_generator.serialize(directory=str(rootdir / "docs/ontology"))
