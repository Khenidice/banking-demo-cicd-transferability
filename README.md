# Banking Demo - Transferability Proof - Different Sector, Same Pipeline - Domain-Agnostic

**Obademi Kehinde | 190407047 | Systems Engineering | 2026**
**Part of: Secure CI/CD Pipeline for Healthcare & Beyond**

**Main Project:** https://github.com/Khenidice/secure-cicd-healthcare
**Hospital Demo:** https://github.com/Khenidice/hospital-demo-hamzaezzine-cicd
**This Repo:** Banking demo based on https://github.com/saadmk11/banking-system — Different Sector, Same Pipeline — Proves Framework is General, Not Just for Hospitals

![CI/CD](https://github.com/Khenidice/banking-demo-cicd-transferability/actions/workflows/ci-cd-pipeline.yml/badge.svg)

## Purpose

**Prove framework is NOT only for hospitals, but works for ANY critical sector — banking, e-gov, insurance, education, etc. — domain-agnostic.**

Addresses examiner concern: "Is your CI/CD relevant only to hospital systems?" — Answer with TWO real repos, SAME pipeline, both pass.

## Source Repository

- **Original:** https://github.com/saadmk11/banking-system
- **Stack:** Django 3.2→4.2 (modernized like main project), User (email auth), BankAccountType, UserBankAccount, UserAddress, Transaction
- **Domain:** Banking — VERY HIGH sensitivity (handles MONEY, PCI-DSS stricter than NDPA 2023), VERY LOW downtime tolerance (customers cannot access money)
- **Completely different business logic:** No Doctors/Patients/Appointments — instead Accounts/Transactions/Interest Calculation

## What We Did

1. Cloned saadmk11/banking-system
2. Upgraded Django 3.2→4.2 (same modernization process as main project)
3. Added requirements.txt: Django 4.2.20 + celery + pytest + bandit
4. Added pytest.ini
5. Wrote 7 real tests (accounts/tests.py, transactions/tests.py):
   - BankAccountType creation, interest calculation
   - User + BankAccount creation, balance property, interest months
   - Transaction creation, home page loads
6. Copied SAME UNIVERSAL pipeline files from main project and hospital demo:
   - `.github/workflows/ci-cd-pipeline.yml` — 100% identical to main project and hospital demo
   - `security_gate.py` — 100% identical
   - `Dockerfile` — 95% identical (only WSGI name differs — configuration, not redesign)
7. Ran tests: 7 OK in 0.646s — REAL log
8. Ran Bandit: 1 LOW, 0 HIGH → SECURITY GATE PASSED — REAL

## Real Results (From Actual Runs)

```
System check identified 5 issues (0 silenced).
test_home_page ... ok
test_create_account_type ... ok
test_interest_calculation ... ok
test_create_user_and_account ... ok
test_interest_months ... ok
test_user_balance_property ... ok
test_deposit_transaction ... ok

Ran 7 tests in 0.646s OK

Bandit: Total findings: 1 | Blocked: 0 — SECURITY GATE PASSED — 0 HIGH, 0 MEDIUM, 1 LOW in 729 LOC
```

**Same pipeline files as main project and hospital demo — proves 99% reusable across sectors**

## How to Run (Old Laptop Friendly - No Docker Needed)

```bash
git clone https://github.com/Khenidice/banking-demo-cicd-transferability.git
cd banking-demo-cicd-transferability
pip install -r requirements.txt
python manage.py test --verbosity 2
# Expected: Ran 7 tests in 0.646s OK

bandit -r accounts transactions banking_system core --exclude tests.py,migrations -f json -o bandit-report-banking.json
python security_gate.py bandit-report-banking.json
# Expected: SECURITY GATE PASSED - 0 HIGH
```

## GitHub Actions (Cloud - No Laptop Power Needed)

1. Push to main → Actions tab → Watch workflow run: install → test (7 tests) → sast (0 HIGH) → build-and-scan → deploy
2. Green checkmark ✅ = Pipeline PASSED — Proof for defense — different sector, same pipeline
3. Screenshot logs for offline proof

## File Comparison - Proof of 99% Reusable Across Sectors

| File | Main Project (Hospital sumitkumar1503) | Hospital Demo (hamzaezzine) | Banking Demo (saadmk11) | Identical? |
|------|----------------------------------------|----------------------------|------------------------|------------|
| ci-cd-pipeline.yml | 5 jobs | 5 jobs | 5 jobs | **YES 100% - all three identical** |
| security_gate.py | Blocks HIGH | Blocks HIGH | Blocks HIGH | **YES 100% - all three identical** |
| Dockerfile Stage 1 | python:3.13-alpine AS builder | python:3.13-alpine AS builder | python:3.13-alpine AS builder | **YES 100%** |
| Dockerfile Stage 2 | Alpine, non-root user | Alpine, non-root user | Alpine, non-root user | **YES 100%** |
| Dockerfile CMD | hospitalmanagement.wsgi | hospital.wsgi | banking_system.wsgi | **95% same - only WSGI name (config)** |

**Overall: 99% reusable across sectors — adaptation by configuration, not redesign — Section 4.6.6 in thesis**

**If same pipeline works for medical records AND money (two most sensitive domains), works for any critical sector — Table 4.12 shows 8 sectors: Healthcare (NDPA 2023), Banking (PCI-DSS), Public Admin, Insurance, Education, Telecom, Energy, Logistics**

## Why Banking is Stronger Proof Than Hospital

- Different business logic: Accounts/Transactions/Interest vs Doctors/Patients/Appointments — completely different
- VERY HIGH sensitivity: Handles MONEY, not just medical records — financial fraud risk if leaked
- Regulation: PCI-DSS stricter than NDPA 2023 — requires secrets scanning, SCA, etc. — pipeline handles it by configuration (tighten gate HIGH→MEDIUM)
- Downtime tolerance: VERY LOW — customers cannot access money — same auto-rollback (11 min vs 48 min manual) handles it
- Same pipeline files — 100% identical YAML, 100% identical security_gate.py — both pass 0 HIGH

**Conclusion: Framework is GENERAL reusable pattern, not one-off — hospital is test case, framework is general — proved with live hospital (9 tests) + banking (7 tests) demos, same pipeline, both pass**

See main thesis Table 4.12 and Transferability_Demo_Evidence.docx for full evidence.
