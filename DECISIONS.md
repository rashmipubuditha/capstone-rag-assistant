# Decisions Log

- LLM provider: OpenAI (gpt-4o-mini, text-embedding-3-small) for MVP.
- Vector DB: Postgres + pgvector (RDS in prod).
- Infra path: Elastic Beanstalk (simpler) for backend; S3+CloudFront for FE.
- Auth: Simple JWT with roles (admin, user).
