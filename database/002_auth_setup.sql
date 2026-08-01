-- FixAI: Supabase Authentication Setup

-- Link our users table with Supabase Auth users
ALTER TABLE public.users
ADD COLUMN auth_user_id UUID UNIQUE
REFERENCES auth.users(id) ON DELETE CASCADE;

-- Useful index for authentication lookups
CREATE INDEX idx_users_auth_user_id
ON public.users(auth_user_id);