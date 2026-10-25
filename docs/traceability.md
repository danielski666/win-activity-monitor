# Win Activity Monitor — Traceability Matrix

**Document version:** 0.1  
**Project version:** 0.1.0  
**Status:** Draft

## 1. Purpose

This document maps project requirements to architectural components, planned test cases, implementation, and verification status.

## 2. Requirement Traceability

| Requirement | Architecture Component | Planned Test | Implementation | Status |
|---|---|---|---|---|
| FR-PROC-001 | Windows Event Source / Collector | TC-PROC-001 | Not implemented | Planned |
| FR-PROC-002 | Process Event Parser / Domain Model | TC-PROC-002 | Domain model implemented | In Progress |
| FR-PROC-003 | Persistence Repository | TC-DB-001 | Not implemented | Planned |
| FR-PROC-004 | SQLite Repository | TC-DB-002 | Not implemented | Planned |
| FR-PROC-005 | Parser / Collector | TC-PROC-003 | Not implemented | Planned |
| FR-PROC-006 | Persistence Repository | TC-DB-003 | Not implemented | Planned |
| NFR-PORT-001 | Core architecture | TC-PORT-001 | Not implemented | Planned |
| NFR-WIN-001 | Windows integration | TC-WIN-001 | Not implemented | Planned |
| NFR-TEST-001 | Unit test suite | CI-UNIT-001 | Not implemented | Planned |
| NFR-TEST-002 | Integration test suite | CI-INT-001 | Not implemented | Planned |
| NFR-CI-001 | Jenkins pipeline | CI-PIPE-001 | Not implemented | Planned |
| NFR-DATA-001 | Persistence architecture | TC-DATA-001 | Not implemented | Planned |
| NFR-DATA-002 | Git configuration | TC-REPO-001 | Partial | In Progress |
| NFR-MAINT-001 | Application architecture | Architecture review | Partial | In Progress |
| NFR-OBS-001 | Collector diagnostics | TC-LOG-001 | Not implemented | Planned |

## 3. Traceability Flow

The intended traceability chain is:

```text
Requirement
    ↓
Architecture / Design
    ↓
Implementation
    ↓
Test Case
    ↓
Automated Test
    ↓
CI Result
```

Example:

```text
FR-PROC-002
    ↓
ProcessEventParser
    ↓
src/pcmonitor/parsing/process_event_parser.py
    ↓
TC-PROC-002
    ↓
tests/unit/test_process_event_parser.py
    ↓
Jenkins
    ↓
PASS / FAIL
```

## 4. Status Definitions

| Status | Meaning |
|---|---|
| Planned | Requirement or test is defined but implementation has not started |
| In Progress | Implementation or verification work has started |
| Implemented | Implementation exists but verification may be incomplete |
| Verified | Required verification has passed |
| Blocked | Verification or implementation cannot currently continue |
