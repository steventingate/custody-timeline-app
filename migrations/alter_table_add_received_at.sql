
ALTER TABLE documents
ADD COLUMN IF NOT EXISTS received_at timestamp;
