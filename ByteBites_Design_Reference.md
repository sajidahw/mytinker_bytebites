# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions

**Scope guardrails**
- Only suggest code involving the four core classes: `Customer`, `FoodItem`, `Menu`, `Transaction`
- Do not introduce new classes, modules, or abstractions not in the spec

**Complexity limits**
- Keep implementations in plain Python — no external libraries, frameworks, or design patterns beyond what the spec requires
- No database layer, file I/O, or authentication logic (already noted in Project Scope)

**Suggestion style**
- When offering multiple approaches, show the simplest one first
- Prefer readable code over clever/optimized code — this is a learning exercise
- Don't add error handling or validation beyond what's explicitly asked for

**Design consistency**
- Follow the class diagram in `draft_from_copilot.md` as the source of truth for attributes and methods
- If asked to add a feature that conflicts with the diagram, flag it before implementing

**Ambiguity handling**
- When a request is unclear, ask one clarifying question rather than assuming and proceeding
- Flag design decisions that could conflict with the existing diagram (e.g., the dual-composer issue with `FoodItem`)
