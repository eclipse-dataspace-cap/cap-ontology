#!/usr/bin/env python

from io import StringIO
from markdown import Markdown
from pathlib import Path
from linkml.generators import docgen
from linkml.generators.docgen import DocGenerator
from linkml.generators.owlgen import OwlSchemaGenerator
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

log_level = logging.DEBUG
logging.basicConfig(
    level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def test_owlready2(ontology_filepath: str):
    from owlready2 import get_ontology
    onto = get_ontology(ontology_filepath).load()
    for classe in onto.classes():
        print(classe, classe.iri)


def test_rdflib(ontology_filepath: str) -> str:
    import rdflib
    g = rdflib.Graph()
    g.parse(ontology_filepath)
    for s, p, o in g:
        print(s, p, o)
    return g.serialize(format="xml")


if __name__ == '__main__':
    rootdir = Path(__file__).parent
    schema_file = rootdir / 'linkml/conformity_assessment.yml'

    output_directory = rootdir / 'docs/ontology'
    template_directory = rootdir / 'docgen-template'

    # Generate documentation for each schema file
    logger.info(f"process file {schema_file}")
    # Create a DocGenerator instance for each schema file
    doc_generator = DocGenerator(
        str(schema_file),
        template_directory=template_directory,
        subfolder_type_separation=True,
        useuris=True,
        mergeimports=False,
        log_level=logging.DEBUG
    )
    doc_generator.serialize(directory=str(output_directory))
    owl_generator = OwlSchemaGenerator(
        str(schema_file),
        metadata_profile='linkml',
        type_objects=False,
        metaclasses=False,
        add_root_classes=False,
        add_ols_annotations=True,
        assert_equivalent_classes=False,
        mixins_as_expressions=False,
        use_native_uris=True,
        default_permissible_value_type=str(OWL.Class),
        log_level=logging.DEBUG
    )
    ontology_owl = owl_generator.serialize()
    with open(str((output_directory / 'ontology.owl.ttl').absolute()), "w") as fd:
        fd.write(ontology_owl)

    ontology_rdfxml = test_rdflib(
        str((output_directory / 'ontology.owl.ttl').absolute()))
    with open(str((output_directory / 'ontology.owl.xml').absolute()), "w") as fd:
        fd.write(ontology_rdfxml)
    test_owlready2(
        "file://" + str((output_directory / 'ontology.owl.xml').absolute()))
