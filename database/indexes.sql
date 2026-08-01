-- FIXAI Database Indexes
-- Improves complaint search, filtering and routing performance

-- Find complaints of a particular student
CREATE INDEX idx_complaints_student_id
ON complaints(student_id);

-- Filter complaints by department
CREATE INDEX idx_complaints_department_id
ON complaints(department_id);

-- Filter complaints by status
CREATE INDEX idx_complaints_status
ON complaints(status);

-- Filter complaints by priority
CREATE INDEX idx_complaints_priority
ON complaints(priority);

-- Find latest complaints quickly
CREATE INDEX idx_complaints_created_at
ON complaints(created_at DESC);

-- Find staff assignments
CREATE INDEX idx_assignments_staff_id
ON assignments(staff_id);

-- Find assignment using complaint
CREATE INDEX idx_assignments_complaint_id
ON assignments(complaint_id);

-- Load complaint status history
CREATE INDEX idx_status_history_complaint_id
ON status_history(complaint_id);

-- Find images belonging to a complaint
CREATE INDEX idx_complaint_images_complaint_id
ON complaint_images(complaint_id);