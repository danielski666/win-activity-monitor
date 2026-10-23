# Win Activity Monitor — Test Plan

**Document version:** 0.1  
**Project version:** 0.1.0  
**Status:** Draft

## 1. Purpose

This document defines the testing strategy for Win Activity Monitor.

The initial test scope covers version 0.1 — Process Monitoring MVP.

The objective is to verify that supported Sysmon process creation events can be collected, parsed, validated, and persisted correctly while maintaining separation between platform-independent and Windows-specific functionality.

## 2. Test Objectives

Testing shall provide confidence that:

- process events are parsed correctly
- malformed input does not terminate the collector
- required process information is persisted correctly
- duplicate events are handled according to the defined strategy
- database initialization works correctly
- platform-independent logic operates on Linux and Windows
- Windows-specific telemetry acquisition works on Windows
- the complete monitoring path can be verified end-to-end

## 3. Test Scope

### In Scope

Version 0.1 testing covers:

- domain models
- process-event parsing
- event validation
- SQLite database initialization
- SQLite event persistence
- duplicate-event handling
- collector orchestration
- Windows Event Log acquisition
- Sysmon process creation events
- automated CI checks

### Out of Scope

The following areas are outside the v0.1 test scope:

- network connection monitoring
- DNS monitoring
- full URL monitoring
- Android application
- REST API
- remote reporting
- production installer
- Windows service lifecycle
- multi-device monitoring

These areas will receive separate test coverage when introduced in future releases.

## 4. Test Levels

### 4.1 Unit Testing

Unit tests verify individual components in isolation.

Primary targets:

- domain models
- parsers
- validation logic
- collector decision logic

External dependencies should be replaced by test doubles where appropriate.

Unit tests shall not require:

- Sysmon
- Windows Event Log
- network access
- a production monitoring database

Example:

```text
Synthetic Sysmon Event
        ↓
ProcessEventParser
        ↓
ProcessEvent
        ↓
Assertions
```

### 4.2 Integration Testing

Integration tests verify communication between multiple components.

Primary targets:

- domain model → repository
- repository → SQLite
- schema initialization
- event persistence and retrieval
- duplicate handling

Integration tests may use a temporary SQLite database.

Example:

```text
ProcessEvent
     ↓
SQLiteRepository
     ↓
temporary SQLite database
     ↓
database query
     ↓
assertions
```

### 4.3 System Testing

System tests verify PCMonitor with real Windows platform dependencies.

Primary targets:

- Windows Event Log access
- Sysmon event acquisition
- Windows-specific adapters
- real event parsing

System tests require a Windows test environment.

### 4.4 End-to-End Testing

E2E tests verify the complete monitoring chain.

Expected flow:

```text
Start test process
       ↓
Sysmon detects process
       ↓
Windows Event Log
       ↓
PCMonitor Event Source
       ↓
Parser
       ↓
Repository
       ↓
SQLite
       ↓
Test verification
```

An example E2E scenario is:

1. Start `notepad.exe`.
2. Wait for the corresponding Sysmon process creation event.
3. Allow PCMonitor to process the event.
4. Query the monitoring database.
5. Verify that a matching process record exists.

## 5. Static Verification

Static verification shall be performed before dynamic tests where practical.

The initial toolset includes:

| Tool | Purpose |
|---|---|
| Ruff | linting and code-quality checks |
| mypy | static type checking |
| pytest | automated dynamic testing |
| pytest-cov | code coverage measurement |

Static-analysis failures should cause the CI build to fail.

## 6. Test Environments

### Linux CI Environment

Initial platform:

```text
Debian VM
```

Responsibilities:

```text
Ruff
mypy
unit tests
platform-independent integration tests
coverage
```

Linux shall not be responsible for testing Windows Event Log or Sysmon integration.

### Windows Test Environment

Initial platform:

```text
Windows 10
```

Responsibilities:

```text
Sysmon integration
Windows Event Log acquisition
Windows-specific integration tests
system tests
E2E tests
future installer tests
```

## 7. CI Test Strategy

The target Jenkins pipeline is:

```text
Source Checkout
      ↓
Dependency Installation
      ↓
Ruff
      ↓
mypy
      ↓
Unit Tests
      ↓
Coverage
      ↓
Integration Tests
      ↓
Windows System / E2E Tests
      ↓
Build Result
```

Platform-independent stages should execute on a Linux Jenkins agent.

Windows-specific stages shall execute on a Windows Jenkins agent.

## 8. Test Data Strategy

Tests should prefer deterministic input.

Parser tests shall use:

- synthetic Sysmon event data
- recorded sanitized event samples
- intentionally malformed event samples

Production monitoring logs shall not be required for normal unit testing.

Personally identifiable or sensitive monitoring data shall not be committed to the repository.

## 9. Test Isolation

Automated tests shall avoid dependence on previous test execution.

Where practical:

- temporary databases shall be created per test or test session
- tests shall clean up created data
- test order shall not affect results
- external Windows state shall be explicitly prepared before system tests

## 10. Entry Criteria

Testing for a feature may begin when:

- the related requirement is defined
- the expected behavior is understood
- the relevant implementation is available
- required test dependencies are available

Windows-specific testing additionally requires:

- supported Windows environment
- Sysmon installed and configured
- required event logging enabled

## 11. Exit Criteria

Version 0.1 may be considered test-complete when:

- all in-scope functional requirements have corresponding tests
- all critical automated tests pass
- no unresolved blocker or critical defects remain
- Windows E2E process-monitoring flow passes
- required CI checks pass
- traceability is updated
- known limitations are documented

## 12. Defect Severity

Initial defect severity classification:

| Severity | Meaning |
|---|---|
| Critical | Monitoring cannot operate or data integrity is severely compromised |
| High | Major required functionality is incorrect or unavailable |
| Medium | Functionality works with meaningful limitations |
| Low | Minor issue with limited functional impact |

## 13. Test Reporting

Automated test execution should provide:

- PASS / FAIL status
- failing test identification
- execution duration
- code coverage where applicable
- diagnostic output for failures

Jenkins will later provide centralized build and test-result reporting.

## 14. Traceability

Tests shall be traceable to requirements.

Example:

```text
FR-PROC-001
      ↓
TC-PROC-001
      ↓
tests/system/test_process_collection.py
      ↓
Jenkins result
```

Traceability details are maintained in:

```text
docs/traceability.md
```

## 15. Test Automation Principle

The project should follow the testing pyramid where practical:

```text
             E2E
            /   \
           /     \
          System
         /       \
        Integration
       /           \
      /             \
          Unit
```

The majority of tests should be fast, deterministic unit and integration tests.

A smaller number of system and E2E tests should validate real Windows behavior.
