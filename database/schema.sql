-- FIXAI Database Schema
-- PostgreSQL

-- 1. Departments
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    role VARCHAR(30) NOT NULL
        CHECK (role IN (
            'student',
            'maintenance_staff',
            'department_admin',
            'warden',
            'super_admin'
        )),
    department_id INTEGER REFERENCES departments(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Complaints
CREATE TABLE complaints (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES users(id),
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    location VARCHAR(255),

    category VARCHAR(100),
    priority VARCHAR(20)
        CHECK (priority IN ('low', 'medium', 'high', 'critical')),

    department_id INTEGER REFERENCES departments(id),

    status VARCHAR(30) NOT NULL DEFAULT 'submitted'
        CHECK (status IN (
            'submitted',
            'assigned',
            'in_progress',
            'resolved',
            'closed'
        )),

    ai_summary TEXT,
    ai_suggested_action TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Complaint Images
CREATE TABLE complaint_images (
    id SERIAL PRIMARY KEY,
    complaint_id INTEGER NOT NULL
        REFERENCES complaints(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. Complaint Assignments
CREATE TABLE assignments (
    id SERIAL PRIMARY KEY,
    complaint_id INTEGER NOT NULL
        REFERENCES complaints(id) ON DELETE CASCADE,
    staff_id INTEGER NOT NULL REFERENCES users(id),
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Complaint Status History
CREATE TABLE status_history (
    id SERIAL PRIMARY KEY,
    complaint_id INTEGER NOT NULL
        REFERENCES complaints(id) ON DELETE CASCADE,
    status VARCHAR(30) NOT NULL,
    changed_by INTEGER REFERENCES users(id),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);