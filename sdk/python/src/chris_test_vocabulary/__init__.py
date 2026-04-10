"""Fide Vocabulary SDK (Python) — typed access to the Fide entity vocabulary (v0)."""

from chris_test_vocabulary.spec import (
    FIDE_ENTITY_TYPES,
    FIDE_VOCABULARY,
    FideEntityTypeCode,
    FideEntityTypeName,
    FideEntityTypeSpec,
    FideStandardFit,
    get_fide_entity_type_spec_by_code,
    get_fide_entity_type_spec_by_name,
    list_fide_entity_types,
)

__all__ = [
    "FIDE_ENTITY_TYPES",
    "FIDE_VOCABULARY",
    "FideEntityTypeCode",
    "FideEntityTypeName",
    "FideEntityTypeSpec",
    "FideStandardFit",
    "__version__",
    "get_fide_entity_type_spec_by_code",
    "get_fide_entity_type_spec_by_name",
    "list_fide_entity_types",
]

__version__ = "0.0.0a0"
