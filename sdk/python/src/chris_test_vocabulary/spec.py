"""Vocabulary spec mirror (generated).

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


FideEntityTypeName = Literal["Statement", "Person", "Organization", "SoftwareAgent", "NetworkResource", "PlatformAccount", "CryptographicAccount", "CreativeWork", "Concept", "Place", "Event", "Action", "PhysicalObject", "TextLiteral", "IntegerLiteral", "DecimalLiteral", "BoolLiteral", "DateLiteral", "YearMonthLiteral", "YearLiteral", "TimeLiteral", "DateTimeLiteral", "DurationLiteral", "URILiteral", "JSONLiteral"]
FideEntityTypeCode = Literal["00", "10", "11", "12", "20", "21", "22", "30", "31", "40", "41", "42", "43", "a0", "a1", "a2", "a3", "b1", "b2", "b3", "b4", "b0", "b5", "c0", "c1"]
FideStandardFit = Literal["Broad", "Close", "Exact"]


FIDE_VOCABULARY: Final[dict[str, object]] = {
    "namespaceUrl": "https://fide.work/vocabulary/v0/",
    "specVersion": "0",
    "specDate": "2026-03-28",
    "entityTypes": {
        "Statement": {
            "code": "00",
            "layer": "Graph Structure",
            "standards": ('rdf:Statement',),
            "standardFit": "Exact",
            "description": "A record of a Subject-Property-Object assertion.",
            "litmus": "Not a verified fact; verification is application-level. Not what it represents.",
        },
        "Person": {
            "code": "10",
            "layer": "Agents",
            "standards": ('schema:Person',),
            "standardFit": "Exact",
            "description": "A person (alive, dead, undead, or fictional).",
            "litmus": "Not an account or organization.",
        },
        "Organization": {
            "code": "11",
            "layer": "Agents",
            "standards": ('org:Organization',),
            "standardFit": "Exact",
            "description": "A durable collective of people, software agents, or both that can act as a unit.",
            "litmus": "Not a single person or software agent. Legal incorporation is not required, but a legal company is always an Organization. A branded initiative, product line, or program is usually a Concept unless it has its own durable collective agency. Not a query-defined group.",
        },
        "SoftwareAgent": {
            "code": "12",
            "layer": "Agents",
            "standards": ('schema:SoftwareApplication', 'prov:SoftwareAgent'),
            "standardFit": "Close",
            "description": "A running process that acts as an independent actor: bot, AI agent, smart contract. Can hold keys and sign.",
            "litmus": "Not a person or organization. Not static passive code (use CreativeWork for repos, images, logic).",
        },
        "NetworkResource": {
            "code": "20",
            "layer": "Network Anchors",
            "standards": ('schema:WebPage', 'schema:WebSite', 'schema:EntryPoint'),
            "standardFit": "Broad",
            "description": "A resource identified primarily by addressability or resolution, such as a URL, URI, or CID.",
            "litmus": "Not a subset or account. Not an inhabitable spatial context (use Place).",
        },
        "PlatformAccount": {
            "code": "21",
            "layer": "Network Anchors",
            "standards": ('schema:OnlineAccount',),
            "standardFit": "Close",
            "description": "An authority-based account principal (e.g., an email address or a specific GitHub, Google, or Mastodon user ID). The identity exists by the permission of a host system's database.",
            "litmus": "Authenticated by a host authority's database. This represents the account principal itself, not the agent or agents that operate it.",
        },
        "CryptographicAccount": {
            "code": "22",
            "layer": "Network Anchors",
            "standards": ('sec:PublicKey', 'sec:publicKeyMultibase'),
            "standardFit": "Close",
            "description": "A math-based account principal (e.g., an EVM address, Bitcoin wallet, or did:key). The identity exists mathematically and is authenticated via mathematical signature keys.",
            "litmus": "Authenticated via mathematical signature keys, independent of a host authority.",
        },
        "CreativeWork": {
            "code": "30",
            "layer": "Knowledge",
            "standards": ('schema:CreativeWork',),
            "standardFit": "Exact",
            "description": "The most generic kind of creative work, including books, movies, photographs, software programs, etc. Non-expressive digital artifacts (binaries, model weights, dataset snapshots) are CreativeWork with refinement via Statements (artifactKind, mediaType, generatedBy, derivedFrom).",
            "litmus": "Not a raw value or formal concept. Not a running agent instance (use SoftwareAgent). Not a resource where location is primary identifier (use NetworkResource).",
        },
        "Concept": {
            "code": "31",
            "layer": "Knowledge",
            "standards": ('skos:Concept', 'schema:DefinedTerm'),
            "standardFit": "Close",
            "description": "A socially or formally recognized unit of meaning, such as a term, topic, category, label, initiative, or other abstract idea.",
            "litmus": "Not a plain raw value. Use this for labels, brands, programs, or initiatives that do not have their own durable collective agency.",
        },
        "Place": {
            "code": "40",
            "layer": "Spacetime",
            "standards": ('schema:Place', 'schema:VirtualLocation'),
            "standardFit": "Broad",
            "description": "A spatial context that can contain presence, co-location, and interaction. Includes physical locations and persistent virtual environments (e.g., a concert venue, a Discord server or channel, a Zoom room, a VRChat instance). Physicality/virtuality is asserted via Statements, not the base type.",
            "litmus": "Not a happening or a physical artifact. Can an Actor have presence there? Is its identity a spatial address rather than a document location or account?",
        },
        "Event": {
            "code": "41",
            "layer": "Spacetime",
            "standards": ('schema:Event',),
            "standardFit": "Exact",
            "description": "An occurrence or happening bounded in time. Can be observed/aggregated; may be caused by Actions, systems, or nature. Occurs at a Place (physical or virtual).",
            "litmus": "Not a specific exertion of agency (Action).",
        },
        "Action": {
            "code": "42",
            "layer": "Spacetime",
            "standards": ('schema:Action', 'prov:Activity'),
            "standardFit": "Close",
            "description": "A discrete assertion or commitment attributable to an Agent. Often produces or records a change (e.g., a transaction, API call, signature). Can be linked to Events via Statements (causes, records, resultsIn).",
            "litmus": "Not a broad temporal happening (Event); must be driven by an Agent.",
        },
        "PhysicalObject": {
            "code": "43",
            "layer": "Spacetime",
            "standards": ('dcmitype:PhysicalObject',),
            "standardFit": "Exact",
            "description": "A tangible, inanimate physical object (e.g., hardware, vehicle, physical document, natural object). Physical only. Use Statements (madeBy, manufactured=true) if man-made vs natural matters.",
            "litmus": "Not a location (where). Not a digital artifact (use CreativeWork).",
        },
        "TextLiteral": {
            "code": "a0",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:string'),
            "standardFit": "Exact",
            "description": "A plain text sequence of characters.",
            "litmus": "Not a Concept.",
        },
        "IntegerLiteral": {
            "code": "a1",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:integer'),
            "standardFit": "Exact",
            "description": "A whole number.",
            "litmus": "Not a decimal or string.",
        },
        "DecimalLiteral": {
            "code": "a2",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:decimal'),
            "standardFit": "Exact",
            "description": "A decimal or floating-point number.",
            "litmus": "Not an integer.",
        },
        "BoolLiteral": {
            "code": "a3",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:boolean'),
            "standardFit": "Exact",
            "description": "A true or false value.",
            "litmus": "Not a number or string.",
        },
        "DateLiteral": {
            "code": "b1",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:date'),
            "standardFit": "Exact",
            "description": "A calendar date in canonical `YYYY-MM-DD` form.",
            "litmus": "Not a datetime or time.",
        },
        "YearMonthLiteral": {
            "code": "b2",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:gYearMonth'),
            "standardFit": "Exact",
            "description": "A calendar year and month in canonical `YYYY-MM` form.",
            "litmus": "Not a full date or year alone.",
        },
        "YearLiteral": {
            "code": "b3",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:gYear'),
            "standardFit": "Exact",
            "description": "A calendar year in canonical `YYYY` form.",
            "litmus": "Not a year-month or full date.",
        },
        "TimeLiteral": {
            "code": "b4",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:time'),
            "standardFit": "Exact",
            "description": "A time of day (formatted according to ISO 8601, represented in UTC).",
            "litmus": "Not a date or datetime.",
        },
        "DateTimeLiteral": {
            "code": "b0",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:dateTime'),
            "standardFit": "Exact",
            "description": "A specific point in time in canonical UTC `YYYY-MM-DDTHH:MM:SSZ` form.",
            "litmus": "Not a date or time alone.",
        },
        "DurationLiteral": {
            "code": "b5",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:duration'),
            "standardFit": "Exact",
            "description": "A calculated amount of elapsed time (ISO 8601 duration format).",
            "litmus": "Not a datetime.",
        },
        "URILiteral": {
            "code": "c0",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'xsd:anyURI'),
            "standardFit": "Exact",
            "description": "A formalized Uniform Resource Identifier string.",
            "litmus": "Not plain text.",
        },
        "JSONLiteral": {
            "code": "c1",
            "layer": "Literals",
            "standards": ('rdf:Literal', 'rdf:JSON'),
            "standardFit": "Exact",
            "description": "A structured JSON object represented in canonical string form.",
            "litmus": "Not a string.",
        },
    },
}

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
