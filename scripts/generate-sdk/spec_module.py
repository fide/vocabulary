#!/usr/bin/env python3
"""Generate ``sdk/python/src/fide_vocabulary/spec.py`` from ``spec/v0/vocabulary.json``."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, TypedDict


class _RawEntity(TypedDict, total=False):
    code: str
    layer: str
    standards: list[str]
    standardFit: str
    description: str
    litmus: str


class _Entity(_RawEntity):
    name: str


def _ensure_str(value: object, path: str) -> str:
    if not isinstance(value, str) or len(value) == 0:
        raise ValueError(f"Invalid string at {path}")
    return value


def normalize_spec(raw: dict[str, Any]) -> dict[str, Any]:
    namespace_url = _ensure_str(raw.get("namespaceUrl"), "namespaceUrl")
    spec_version = _ensure_str(raw.get("specVersion"), "specVersion")
    spec_date = _ensure_str(raw.get("specDate"), "specDate")

    entity_types = raw.get("entityTypes")
    if not isinstance(entity_types, dict):
        raise ValueError("Invalid entityTypes object")

    entities: list[_Entity] = []
    for name, value in entity_types.items():
        if not isinstance(value, dict):
            raise ValueError(f"Invalid entity type entry for {name!r}")
        standards_raw = value.get("standards")
        standards = (
            [_ensure_str(s, f"{name}.standards[{i}]") for i, s in enumerate(standards_raw)]
            if isinstance(standards_raw, list)
            else []
        )
        entities.append(
            {
                "name": _ensure_str(name, "entityTypes key"),
                "code": _ensure_str(value.get("code"), f"{name}.code"),
                "layer": _ensure_str(value.get("layer"), f"{name}.layer"),
                "standards": standards,
                "standardFit": _ensure_str(value.get("standardFit"), f"{name}.standardFit"),
                "description": _ensure_str(value.get("description"), f"{name}.description"),
                "litmus": _ensure_str(value.get("litmus"), f"{name}.litmus"),
            }
        )

    return {
        "namespaceUrl": namespace_url,
        "specVersion": spec_version,
        "specDate": spec_date,
        "entities": entities,
    }


def _literal_union(names: list[str], type_name: str) -> str:
    inner = ", ".join(json.dumps(n) for n in names)
    return f"{type_name} = Literal[{inner}]"


def build_spec_module(spec: dict[str, Any]) -> str:
    entities: list[_Entity] = spec["entities"]
    names = [e["name"] for e in entities]
    codes = [e["code"] for e in entities]
    fits = sorted({e["standardFit"] for e in entities})

    entity_blocks: list[str] = []
    for e in entities:
        name = e["name"]
        tup = repr(tuple(e["standards"]))
        entity_blocks.append(
            f'''        {json.dumps(name)}: {{
            "code": {json.dumps(e["code"])},
            "layer": {json.dumps(e["layer"])},
            "standards": {tup},
            "standardFit": {json.dumps(e["standardFit"])},
            "description": {json.dumps(e["description"])},
            "litmus": {json.dumps(e["litmus"])},
        }},'''
        )
    entities_body = "\n".join(entity_blocks)

    name_literal = _literal_union(names, "FideEntityTypeName")
    code_literal = _literal_union(codes, "FideEntityTypeCode")
    fit_literal = _literal_union(fits, "FideStandardFit")

    return f'''"""Vocabulary spec mirror (generated).

Generated from ``packages/fide-vocabulary/spec/v0/vocabulary.json``.
Do not edit directly; regenerate from the vocabulary source of truth.
"""

from __future__ import annotations

from typing import Final, Literal, TypedDict, cast


class FideEntityTypeSpec(TypedDict):
    code: str
    layer: str
    standards: tuple[str, ...]
    standardFit: str
    description: str
    litmus: str


{name_literal}
{code_literal}
{fit_literal}


FIDE_VOCABULARY: Final[dict[str, object]] = {{
    "namespaceUrl": {json.dumps(spec["namespaceUrl"])},
    "specVersion": {json.dumps(spec["specVersion"])},
    "specDate": {json.dumps(spec["specDate"])},
    "entityTypes": {{
{entities_body}
    }},
}}

FIDE_ENTITY_TYPES: Final[dict[FideEntityTypeName, FideEntityTypeSpec]] = cast(
    dict[FideEntityTypeName, FideEntityTypeSpec],
    FIDE_VOCABULARY["entityTypes"],
)


def get_fide_entity_type_spec_by_name(name: FideEntityTypeName) -> FideEntityTypeSpec:
    """Return the entity type definition for ``name``."""
    return FIDE_ENTITY_TYPES[name]


def get_fide_entity_type_spec_by_code(code: FideEntityTypeCode) -> FideEntityTypeSpec | None:
    """Return the entity type definition for ``code``, or ``None`` if unknown."""
    for spec in FIDE_ENTITY_TYPES.values():
        if spec["code"] == code:
            return spec
    return None


def list_fide_entity_types() -> list[FideEntityTypeSpec]:
    """Return all entity type definitions in source order."""
    return list(FIDE_ENTITY_TYPES.values())
'''


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    package_root = script_dir.parent.parent
    vocabulary_path = package_root / "spec" / "v0" / "vocabulary.json"
    out_path = package_root / "sdk" / "python" / "src" / "chris_test_vocabulary" / "spec.py"

    raw = json.loads(vocabulary_path.read_text(encoding="utf8"))
    normalized = normalize_spec(raw)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build_spec_module(normalized), encoding="utf8")
    print(f"Wrote {out_path} ({len(normalized['entities'])} entity types).")


if __name__ == "__main__":
    main()
