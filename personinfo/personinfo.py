# Auto generated from personinfo.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-10-10T11:29:37
# Schema: personinfo
#
# id: https://w3id.org/linkml/examples/personinfo
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PERSONINFO = CurieNamespace('personinfo', 'https://w3id.org/linkml/examples/personinfo/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = PERSONINFO


# Types

# Class references
class PersonId(extended_str):
    pass


@dataclass(repr=False)
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = PERSONINFO.Person

    id: Union[str, PersonId] = None
    full_name: str = None
    aliases: Optional[Union[str, List[str]]] = empty_list()
    phone: Optional[str] = None
    age: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.full_name):
            self.MissingRequiredField("full_name")
        if not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self.phone is not None and not isinstance(self.phone, str):
            self.phone = str(self.phone)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PERSONINFO["Container"]
    class_class_curie: ClassVar[str] = "personinfo:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = PERSONINFO.Container

    persons: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="persons", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=PERSONINFO.id, name="id", curie=PERSONINFO.curie('id'),
                   model_uri=PERSONINFO.id, domain=None, range=URIRef)

slots.full_name = Slot(uri=SCHEMA.name, name="full_name", curie=SCHEMA.curie('name'),
                   model_uri=PERSONINFO.full_name, domain=None, range=str)

slots.aliases = Slot(uri=PERSONINFO.aliases, name="aliases", curie=PERSONINFO.curie('aliases'),
                   model_uri=PERSONINFO.aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.phone = Slot(uri=SCHEMA.telephone, name="phone", curie=SCHEMA.curie('telephone'),
                   model_uri=PERSONINFO.phone, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\d\(\)\-]+$'))

slots.age = Slot(uri=PERSONINFO.age, name="age", curie=PERSONINFO.curie('age'),
                   model_uri=PERSONINFO.age, domain=None, range=Optional[int])

slots.container__persons = Slot(uri=PERSONINFO.persons, name="container__persons", curie=PERSONINFO.curie('persons'),
                   model_uri=PERSONINFO.container__persons, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])