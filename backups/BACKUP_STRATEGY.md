# FixAI Backup Strategy

## Database

- PostgreSQL database hosted on Supabase.
- Daily automatic backups enabled (Supabase managed).
- Manual SQL export before major releases.

## Storage

- Images stored in Supabase Storage.
- Regular bucket export recommended.

## Source Code

- GitHub repository acts as source backup.
- Every feature merged through GitHub.

## Environment Variables

- Secrets are never committed.
- Stored securely in Render Environment Variables.

## Disaster Recovery

1. Restore database backup.
2. Redeploy application from GitHub.
3. Configure environment variables.
4. Verify /health endpoint.