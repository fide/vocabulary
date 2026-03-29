# `@fide-work/vocabulary`

JavaScript/TypeScript SDK for the Fide Vocabulary.

This package provides typed access to the current Fide Vocabulary spec and helper functions for working with Fide entity type definitions.

- SDK docs: [fide.work/docs/vocabulary/sdk/javascript](https://fide.work/docs/vocabulary/sdk/javascript)
- npm: [@fide-work/vocabulary](https://www.npmjs.com/package/@fide-work/vocabulary)
- Repository: [github.com/fide/vocabulary](https://github.com/fide/vocabulary)

## Status

This package is in alpha.

- It currently tracks the mutable `v0` vocabulary line.
- Breaking changes are allowed during alpha.
- Consumers should pin exact versions.

## Install

```bash
pnpm add @fide-work/vocabulary
```

## Usage

```ts
import {
  FIDE_VOCABULARY,
  getFideEntityTypeSpecByName,
  getFideEntityTypeSpecByCode,
  listFideEntityTypes,
} from "@fide-work/vocabulary";

const person = getFideEntityTypeSpecByName("Person");
const statement = getFideEntityTypeSpecByCode("00");
const allEntityTypes = listFideEntityTypes();

console.log(FIDE_VOCABULARY.specVersion);
console.log(person.code);
console.log(statement?.description);
console.log(allEntityTypes.length);
```

## Exports

- `FIDE_VOCABULARY`
- `FIDE_ENTITY_TYPES`
- `getFideEntityTypeSpecByName(name)`
- `getFideEntityTypeSpecByCode(code)`
- `listFideEntityTypes()`

## Types

- `FideEntityTypeName`
- `FideEntityTypeCode`
- `FideEntityTypeSpec`
- `FideStandardFit`

## Source Of Truth

The exported vocabulary data is generated from the canonical spec source in the Fide Vocabulary repository.

- Spec docs: [fide.work/docs/vocabulary](https://fide.work/docs/vocabulary)
- Repository: [github.com/fide/vocabulary](https://github.com/fide/vocabulary)

## Development

Useful local commands:

- `pnpm run build`
- `pnpm test`
