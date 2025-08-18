# capstone-rag-assistant

ERP Knowledge Assistant

# ERP Knowledge Assistant (RAG + React + FastAPI + AWS)

## Problem Statement

Knowledge about our ERP (product catalogs, SOPs, invoices, sales CSVs) is scattered across PDFs and spreadsheets. New team members struggle to find accurate, up-to-date answers quickly. We need a secure assistant that:

- Accepts PDF/CSV uploads.
- Answers questions with citations from our documents.
- Optionally runs safe read-only SQL analytics on a sales table.

## Users & Scenarios

- **Sales Ops**: “What’s the discount policy for RD sales?”
- **Finance**: “Summarize last month’s outlet sales by SKU, top 5.”
- **New Hires**: “Where is the SOP for returns?”

## Out of Scope (Non-Goals)

- Writing back to ERP.
- Complex data quality/ETL.
- Advanced multi-doc editing.

## Success Criteria (Measurable)

- **Groundedness ≥ 70%** on a 30-Q golden set (RAGAS/LC evals).
- **Answer latency ≤ 6s p95** for top-k retrieval=5 on 1000 chunks.
- **Citations shown** for ≥ 95% of answers retrieving context.
- **Deployed public demo URL** with basic auth.
- **Admin panel** shows docs + ingestion status.

## Architecture (High-Level)

React (Vite/Tailwind) → FastAPI → LangChain RAG  
Storage: S3 (raw docs), Postgres + pgvector (chunks/embeddings)  
Optional tool: read-only SQL over Postgres for small analytics.

## Milestones (Week-by-Week)

- **Wk1**: Local MVP (upload → ingest → ask → cite).
- **Wk2**: Retrieval quality, SQL tool, evals, auth, rate-limit.
- **Wk3**: AWS deploy (S3, RDS, EB/ECS), logging/alarms, CI/CD.
- **Wk4**: Admin panel, safety, perf/cost, docs, final video.

## Risks & Mitigations

- **Token costs** → small embedding model, hybrid search, reranker toggle.
- **Latency** → ANN index tuning, context window control.
- **Data privacy** → private S3, JWT auth, allowlisted SQL.

## Getting Started (Local)

See `Getting Started Commands` in the roadmap (backend/frontend).
