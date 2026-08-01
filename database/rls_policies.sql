-- FIXAI Row Level Security Policies

-- Enable RLS
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE complaints ENABLE ROW LEVEL SECURITY;
ALTER TABLE complaint_images ENABLE ROW LEVEL SECURITY;

-- USERS
CREATE POLICY "Users can view users"
ON users
FOR SELECT
TO authenticated
USING (true);

-- COMPLAINT IMAGES
CREATE POLICY "Users can view complaint images"
ON complaint_images
FOR SELECT
TO authenticated
USING (true);

CREATE POLICY "Users can add complaint images"
ON complaint_images
FOR INSERT
TO authenticated
WITH CHECK (true);

-- ASSIGNMENTS
ALTER TABLE assignments ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Authenticated users can view assignments"
ON assignments
FOR SELECT
TO authenticated
USING (true);

-- STATUS HISTORY
ALTER TABLE status_history ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Authenticated users can view status history"
ON status_history
FOR SELECT
TO authenticated
USING (true);