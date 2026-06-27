# Adaptive Learning Platform Documentation

Welcome to the engineering documentation for the Adaptive Learning Platform.

This documentation is intended for developers, architects, testers, DevOps engineers, AI engineers, and future contributors.

Before contributing to the project, every team member should follow the reading order below.

---

# Documentation Reading Order

## 1. Architecture

Start here to understand the overall platform.

```
architecture/
```

Contains:

* Project Vision
* System Architecture
* Backend Architecture
* AI Architecture
* Database Architecture
* Deployment Architecture

---

## 2. ADR (Architecture Decision Records)

```
adr/
```

Contains permanent architectural decisions.

Examples:

* Platform Architecture
* Authentication Strategy
* Knowledge Graph Design
* AI Agent Architecture

Read these to understand **why** the system is designed the way it is.

---

## 3. RFC (Request for Comments)

```
rfc/
```

Contains design proposals that are discussed before implementation.

RFCs become ADRs once approved.

---

## 4. Milestones

```
milestones/
```

Contains implementation history.

Each milestone documents:

* Objectives
* Completed work
* Decisions
* Verification
* Future tasks

---

## 5. Database

```
database/
```

Contains:

* PostgreSQL schema
* Neo4j graph design
* ER diagrams
* Migration strategy

---

## 6. API

```
api/
```

Contains:

* API standards
* Versioning
* Endpoint documentation
* Authentication flow

---

## 7. Setup

```
setup/
```

Contains developer setup guides.

Examples:

* Ubuntu setup
* Docker setup
* Local development
* Environment variables

---

## 8. Standards

```
standards/
```

Contains engineering standards.

Examples:

* Coding conventions
* Git workflow
* Branch strategy
* Commit message standards
* API naming conventions

---

# Engineering Philosophy

The project follows an architecture-first development approach.

Every significant feature follows the lifecycle below:

Requirement

↓

RFC

↓

Architecture Decision

↓

Implementation

↓

Testing

↓

Documentation

↓

Git Commit

↓

GitHub Push

This ensures that implementation always aligns with architectural decisions and remains understandable for future contributors.

---

# Contributing

Before implementing a feature:

1. Read the relevant architecture documents.
2. Check existing ADRs.
3. Create an RFC if the feature introduces a major design change.
4. Implement the feature.
5. Update documentation.
6. Commit with a meaningful message.

---

This documentation evolves alongside the platform and serves as the single source of truth for engineering decisions.
