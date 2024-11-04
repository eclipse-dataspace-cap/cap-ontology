#!/usr/bin/env python

from io import StringIO
from markdown import Markdown
from pathlib import Path
from linkml.generators import docgen
from linkml.generators.docgen import DocGenerator
from linkml.generators.owlgen import OwlSchemaGenerator
from linkml.generators.linkmlgen import LinkmlGenerator
import logging
import traceback

from rdflib import OWL


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


docgen.enshorten = enshorten

log_level = logging.INFO
logging.basicConfig(
    level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def test_owlready2(ontology_filepath: Path):
    from owlready2 import get_ontology
    onto = get_ontology("file://" + str(ontology_filepath.absolute())).load()
    logger.info(f"owlready2: found {len(list(onto.classes()))} classes")
    # for classe in onto.classes():
    #     print(classe, classe.iri)


def test_rdflib(ontology_filepath: Path):
    import rdflib
    g = rdflib.Graph()
    g.parse(str(ontology_filepath.absolute()))
    logger.info(f"rdflib: found {len(list(g))} elements")
    # for s, p, o in g:
    #     print(s, p, o)
    # return g.serialize(format="xml")


def generate_doc(schema_file: Path, output_directory: Path):
    logger.info(f"Generate documentation with {schema_file}")
    doc_generator = DocGenerator(
        str(schema_file),
        template_directory=template_directory,
        subfolder_type_separation=True,
        useuris=True,
        mergeimports=False,
        log_level=log_level
    )
    doc_generator.serialize(directory=str(output_directory))


def generate_owl(schema_file: Path, output_file: Path, format: str = 'owl'):
    owl_generator = OwlSchemaGenerator(
        str(schema_file),
        format=format,
        metadata_profile='linkml',
        type_objects=False,
        metaclasses=False,
        add_root_classes=False,
        add_ols_annotations=True,
        assert_equivalent_classes=False,
        mixins_as_expressions=False,
        use_native_uris=True,
        default_permissible_value_type=str(OWL.Class),
        log_level=log_level
    )
    ontology_owl = owl_generator.serialize()
    with open(str(output_file.absolute()), "w") as fd:
        fd.write(ontology_owl)


def generate_linkml(schema_file: Path, output_file: Path):
    linkml_generator = LinkmlGenerator(
        str(schema_file),
        format='yaml',
        materialize_attributes=False,
        materialize_patterns=False,
        mergeimports=False,
        log_level=log_level
    )
    ontology_linkml = linkml_generator.serialize()
    with open(str((output_directory / 'ontology.linkml.yml').absolute()), "w") as fd:
        fd.write(ontology_linkml)


if __name__ == '__main__':
    rootdir = Path(__file__).parent
    schema_file = rootdir / 'linkml/conformity_assessment.yml'

    output_directory = rootdir / 'docs/ontology'
    template_directory = rootdir / 'docgen-template'

    logger.info(f"process file {schema_file}")

    generate_doc(schema_file, output_directory)
    generate_owl(schema_file, output_directory / 'ontology.owl.ttl')
    generate_owl(schema_file, output_directory /
                 'ontology.owl.xml', format='xml')
    generate_linkml(schema_file, output_directory / 'ontology.linkml.yml')
    test_owlready2(output_directory / 'ontology.owl.xml')
    test_rdflib(output_directory / 'ontology.owl.ttl')
