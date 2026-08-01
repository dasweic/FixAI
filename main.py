import ast
from ollama import chat

def ai(prompt, model="gemma3:4b"):
    response = chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def normalize_complaint(complaint: str) -> str:
    prompt = f"""
You are a complaint normalization AI.

Your task is to rewrite the complaint into a clean, professional, and concise version.

Rules:
- Preserve the original meaning.
- Remove abusive, emotional, repetitive, or unnecessary words.
- Correct grammar and spelling.
- Do NOT add any new information.
- Keep important details like names, dates, locations, product names, IDs, etc.
- Return ONLY the normalized complaint.
- No explanations.
- No markdown.
- No quotes.

Complaint:
{complaint}
"""

    return ai(prompt).strip()

import json

def extract_keywords(complaint):
    prompt = f"""
Extract important keywords from the complaint.

Return ONLY a JSON array.

Example:
["fan","room 204","sparks"]

Complaint:
{complaint}
"""

    response = ai(prompt).strip()

    # remove markdown if model adds it
    response = response.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(response)
    except Exception:
        print(response)
        return []


def classify_category(complaint: str) -> str:
    prompt = f"""
You are a complaint classification AI.

Classify the complaint into exactly ONE of these categories:

- Electrical
- Water
- Furniture
- Internet
- Cleaning
- Civil
- Other

Rules:
- Return ONLY the category name.
- Do not explain.
- Do not use markdown.
- Do not return multiple categories.
- If no category matches, return "Other".

Complaint:
{complaint}
"""

    category = ai(prompt).strip()

    valid_categories = {
        "Electrical",
        "Water",
        "Furniture",
        "Internet",
        "Cleaning",
        "Civil",
        "Other"
    }

    if category not in valid_categories:
        return "Other"

    return category


def classify_subcategory(complaint: str, category: str) -> str:
    prompt = f"""
You are a complaint subcategory classification AI.

Main Category:
{category}

Choose exactly ONE subcategory.

Electrical:
- Fan
- Light
- Switch
- Socket
- Open Wire
- MCB
- Power Failure
- Generator
- Other

Water:
- Leakage
- Tap
- Pipe
- Water Supply
- Drainage
- Tank
- Water Cooler
- Other

Furniture:
- Chair
- Table
- Bed
- Cupboard
- Door
- Window
- Lock
- Other

Internet:
- WiFi
- LAN
- Router
- Slow Speed
- No Internet
- Login Issue
- Other

Cleaning:
- Garbage
- Dust
- Washroom
- Corridor
- Room Cleaning
- Pest Control
- Other

Civil:
- Wall Crack
- Ceiling
- Floor
- Paint
- Roof
- Tiles
- Plumbing Structure
- Other

Rules:
- Return ONLY the subcategory name.
- No explanation.
- No markdown.
- If unsure, return "Other".

Complaint:
{complaint}
"""

    subcategory = ai(prompt).strip()

    valid = {
        "Fan","Light","Switch","Socket","Open Wire","MCB","Power Failure","Generator",
        "Leakage","Tap","Pipe","Water Supply","Drainage","Tank","Water Cooler",
        "Chair","Table","Bed","Cupboard","Door","Window","Lock",
        "WiFi","LAN","Router","Slow Speed","No Internet","Login Issue",
        "Garbage","Dust","Washroom","Corridor","Room Cleaning","Pest Control",
        "Wall Crack","Ceiling","Floor","Paint","Roof","Tiles","Plumbing Structure",
        "Other"
    }

    if subcategory not in valid:
        return "Other"

    return subcategory


def category_confidence(complaint: str, category: str) -> float:
    prompt = f"""
You are a complaint classification evaluator.

Complaint:
{complaint}

Predicted Category:
{category}

Estimate how confident you are that the category is correct.

Rules:
- Return ONLY a decimal number between 0.00 and 1.00.
- Examples:
0.99
0.87
0.51
0.12
- No explanation.
- No markdown.
- No percent sign.
- No extra text.
"""

    response = ai(prompt).strip()

    try:
        score = float(response)

        if score < 0:
            return 0.0
        if score > 1:
            return 1.0

        return round(score, 2)

    except:
        return 0.0


def generate_title(complaint: str) -> str:

    prompt = f"""
You are an AI that generates complaint titles.

Generate a short, professional title for the complaint.

Rules:
- Maximum 8 words.
- Minimum 2 words.
- Use Title Case.
- Be specific.
- Do not include room numbers, hostel numbers, names, IDs, or unnecessary details unless essential.
- Do not end with a period.
- Return ONLY the title.
- No explanation.
- No markdown.
- No quotes.

Complaint:
{complaint}
"""

    title = ai(prompt).strip()

    # Remove accidental quotes/newlines
    title = title.replace('"', "").replace("'", "").replace("\n", " ").strip()

    return title

def generate_professional_description(complaint: str) -> str:
    prompt = f"""
You are a professional complaint writing AI.

Rewrite the student's complaint into a clear, formal, and professional complaint.

Rules:
- Preserve the original meaning.
- Correct grammar and spelling.
- Remove emotional, abusive, or repetitive words.
- Keep all important details.
- Do not invent any information.
- Use a polite and professional tone.
- Output a single paragraph (40–120 words).
- Return ONLY the professional complaint.
- No markdown.
- No explanation.
- No quotes.

Student Complaint:
{complaint}
"""

    description = ai(prompt).strip()

    # Clean accidental formatting
    description = (
        description
        .replace("```", "")
        .replace('"', "")
        .strip()
    )

    return description


cs = "fan in my room is not working from last 4 days. i complained many times but nobody came."

def summarize_issue(complaint: str) -> str:
    prompt = f"""
You are an AI that summarizes complaints.

Generate a concise one-line summary of the complaint.

Rules:
- Maximum 15 words.
- Minimum 4 words.
- Mention the main issue only.
- Be specific.
- Use sentence case.
- Do not include unnecessary details like room numbers, hostel numbers, names, IDs, unless essential.
- Do not end with a period.
- Return ONLY the summary.
- No explanation.
- No markdown.
- No quotes.

Complaint:
{complaint}
"""

    summary = ai(prompt).strip()

    # Clean accidental formatting
    summary = (
        summary
        .replace("```", "")
        .replace('"', "")
        .replace("'", "")
        .replace("\n", " ")
        .strip()
    )

    return summary


import ast

def detect_safety_keywords(complaint: str) -> list:
    prompt = f"""
You are a safety hazard detection AI.

Identify safety-related hazards mentioned in the complaint.

Possible hazards include (but are not limited to):
- fire
- smoke
- spark
- electric shock
- exposed wire
- open wire
- short circuit
- gas leak
- chemical leak
- water leakage near switch
- water leakage near socket
- burning smell
- overheating
- explosion risk
- ceiling collapse
- wall collapse
- falling object
- broken glass
- live wire

Rules:
- Return ONLY a valid Python list.
- Use lowercase.
- No duplicates.
- If no safety hazard exists, return [].
- No explanation.
- No markdown.
- No quotes outside the list.

Complaint:
{complaint}
"""

    response = ai(prompt).strip()

    try:
        hazards = ast.literal_eval(response)

        if isinstance(hazards, list):
            return [str(x).lower() for x in hazards]

    except:
        pass

    return []

def calculate_priority(complaint: str) -> str:
    prompt = f"""
You are a complaint priority classification AI.

Determine the priority of the complaint.

Return ONLY one of these values:

- Low
- Medium
- High
- Critical

Guidelines:

Critical:
- Fire
- Smoke
- Sparks
- Electric shock
- Open/live wire
- Gas leak
- Ceiling collapse
- Wall collapse
- Explosion risk
- Water leakage near electrical equipment
- Any life-threatening situation

High:
- Complete power failure
- Water leakage
- Major plumbing issue
- Internet outage affecting many users
- Broken door lock
- Broken window
- Ceiling leakage
- Serious damage requiring urgent repair

Medium:
- Fan not working
- Light not working
- Dirty washroom
- Broken furniture
- Slow internet
- Water cooler not working
- Paint damage

Low:
- Cleaning request
- Minor maintenance
- Cosmetic issues
- Suggestions
- Non-urgent complaints

Rules:
- Consider the severity and safety risk.
- Return ONLY one word.
- No explanation.
- No markdown.

Complaint:
{complaint}
"""

    priority = ai(prompt).strip()

    valid = {"Low", "Medium", "High", "Critical"}

    if priority not in valid:
        return "Medium"

    return priority


import json

def explain_priority(
    complaint: str,
    category: str,
    subcategory: str,
    priority: str
) -> dict:
    prompt = f"""
You are a complaint analysis AI.

Explain why this complaint received its priority.

Complaint:
{complaint}

Category:
{category}

Subcategory:
{subcategory}

Priority:
{priority}

Return ONLY a valid JSON object.

Format:
{{
    "priority": "Critical",
    "reason": "Complaint contains a serious electrical safety hazard.",
    "matched_keywords": ["spark", "smoke"],
    "category": "Electrical",
    "subcategory": "Open Wire",
    "risk_type": "Electrical Hazard",
    "recommended_action": "Immediate inspection and repair."
}}

Rules:
- Return ONLY JSON.
- No markdown.
- No explanation outside JSON.
- If no safety keyword exists, return an empty list for matched_keywords.
"""

    response = ai(prompt).strip()

    try:
        return json.loads(response)
    except:
        return {
            "priority": priority,
            "reason": "Unable to determine.",
            "matched_keywords": [],
            "category": category,
            "subcategory": subcategory,
            "risk_type": "Unknown",
            "recommended_action": "Manual review required."
        }



from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def generate_embedding(text: str) -> list[float]:
    """
    Generates a semantic embedding vector for the given text.

    Returns:
        list[float] : 384-dimensional embedding vector.
    """

    embedding = embedding_model.encode(
        text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embedding.tolist()


from sentence_transformers import util

def compare_similarity(text1: str, text2: str) -> float:
    """
    Returns cosine similarity between two texts.
    Range: 0.0 - 1.0
    """

    emb1 = embedding_model.encode(
        text1,
        convert_to_tensor=True,
        normalize_embeddings=True
    )

    emb2 = embedding_model.encode(
        text2,
        convert_to_tensor=True,
        normalize_embeddings=True
    )

    similarity = util.cos_sim(emb1, emb2).item()

    return round(similarity, 2)


def detect_duplicate(
    complaint: str,
    complaints: list,
    threshold: float = 0.90
) -> dict:
    """
    Detect duplicate complaint using cosine similarity.

    Returns:
    {
        "duplicate": True/False,
        "original_complaint_id": int or None,
        "confidence": float
    }
    """

    new_embedding = generate_embedding(complaint)

    best_similarity = 0.0
    best_id = None

    for item in complaints:

        similarity = compare_similarity(
            new_embedding,
            item["embedding"]
        )

        if similarity > best_similarity:
            best_similarity = similarity
            best_id = item["id"]

    return {
        "duplicate": best_similarity >= threshold,
        "original_complaint_id": best_id if best_similarity >= threshold else None,
        "confidence": round(best_similarity, 2)
    }

def rank_similar_complaints(
    complaint: str,
    complaints: list,
    top_k: int = 5
) -> list:
    """
    Returns the Top-K most similar complaints.

    complaints format:
    [
        {
            "id": 101,
            "text": "...",
            "embedding": [...]
        }
    ]
    """

    new_embedding = generate_embedding(complaint)

    results = []

    for item in complaints:

        similarity = compare_similarity(
            new_embedding,
            item["embedding"]
        )

        results.append({
            "complaint_id": item["id"],
            "complaint": item["text"],
            "confidence": round(similarity, 2)
        })

    results.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    return results[:top_k]



def recommend_department(
    complaint: str,
    category: str,
    subcategory: str
) -> str:
    prompt = f"""
You are a complaint routing AI.

Recommend the most appropriate department.

Complaint:
{complaint}

Category:
{category}

Subcategory:
{subcategory}

Choose ONLY one department from the following:

- Electrical Maintenance
- Plumbing Department
- Civil Maintenance
- Housekeeping
- IT Support
- Furniture Maintenance
- Security Department
- Administration
- Other

Routing Guide:

Electrical:
- Fan
- Light
- Switch
- Socket
- Open Wire
- MCB
- Generator
-> Electrical Maintenance

Water:
- Leakage
- Tap
- Pipe
- Tank
- Drainage
- Water Cooler
-> Plumbing Department

Civil:
- Wall Crack
- Ceiling
- Floor
- Roof
- Paint
- Tiles
-> Civil Maintenance

Cleaning:
- Garbage
- Dust
- Washroom
- Corridor
- Room Cleaning
- Pest Control
-> Housekeeping

Internet:
- WiFi
- LAN
- Router
- Slow Speed
- No Internet
-> IT Support

Furniture:
- Chair
- Table
- Bed
- Cupboard
- Door
- Window
- Lock
-> Furniture Maintenance

Security issues:
-> Security Department

Unknown issues:
-> Administration

Rules:
- Return ONLY the department name.
- No explanation.
- No markdown.
"""

    department = ai(prompt).strip()

    valid_departments = {
        "Electrical Maintenance",
        "Plumbing Department",
        "Civil Maintenance",
        "Housekeeping",
        "IT Support",
        "Furniture Maintenance",
        "Security Department",
        "Administration",
        "Other"
    }

    if department not in valid_departments:
        return "Administration"

    return department


def recommendation_confidence(
    complaint: str,
    category: str,
    subcategory: str,
    department: str
) -> float:
    prompt = f"""
You are a complaint routing evaluator.

Complaint:
{complaint}

Category:
{category}

Subcategory:
{subcategory}

Recommended Department:
{department}

Estimate how confident you are that the complaint has been assigned to the correct department.

Rules:
- Return ONLY a decimal number between 0.00 and 1.00.
- Examples:
0.99
0.94
0.82
0.45
- No explanation.
- No markdown.
- No percent sign.
- No extra text.
"""

    response = ai(prompt).strip()

    try:
        confidence = float(response)

        if confidence < 0:
            return 0.0

        if confidence > 1:
            return 1.0

        return round(confidence, 2)

    except:
        return 0.0


def fallback_department(
    category: str,
    subcategory: str = ""
) -> str:
    """
    Rule-based department recommendation.
    Used only if AI fails.
    """

    category = category.strip().lower()
    subcategory = subcategory.strip().lower()

    # Category-based mapping
    category_map = {
        "electrical": "Electrical Maintenance",
        "water": "Plumbing Department",
        "civil": "Civil Maintenance",
        "cleaning": "Housekeeping",
        "internet": "IT Support",
        "furniture": "Furniture Maintenance"
    }

    # Subcategory overrides (higher priority)
    subcategory_map = {
        "fan": "Electrical Maintenance",
        "light": "Electrical Maintenance",
        "switch": "Electrical Maintenance",
        "socket": "Electrical Maintenance",
        "open wire": "Electrical Maintenance",
        "mcb": "Electrical Maintenance",
        "generator": "Electrical Maintenance",

        "tap": "Plumbing Department",
        "pipe": "Plumbing Department",
        "leakage": "Plumbing Department",
        "drainage": "Plumbing Department",
        "tank": "Plumbing Department",
        "water cooler": "Plumbing Department",

        "wall crack": "Civil Maintenance",
        "ceiling": "Civil Maintenance",
        "floor": "Civil Maintenance",
        "roof": "Civil Maintenance",
        "paint": "Civil Maintenance",
        "tiles": "Civil Maintenance",

        "garbage": "Housekeeping",
        "dust": "Housekeeping",
        "washroom": "Housekeeping",
        "corridor": "Housekeeping",
        "room cleaning": "Housekeeping",
        "pest control": "Housekeeping",

        "wifi": "IT Support",
        "lan": "IT Support",
        "router": "IT Support",
        "slow speed": "IT Support",
        "no internet": "IT Support",
        "login issue": "IT Support",

        "chair": "Furniture Maintenance",
        "table": "Furniture Maintenance",
        "bed": "Furniture Maintenance",
        "cupboard": "Furniture Maintenance",
        "door": "Furniture Maintenance",
        "window": "Furniture Maintenance",
        "lock": "Furniture Maintenance"
    }

    # Prefer subcategory if available
    if subcategory in subcategory_map:
        return subcategory_map[subcategory]

    # Otherwise use category
    if category in category_map:
        return category_map[category]

    # Default
    return "Administration"


'''filename = "main.py"

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        if line.lstrip().startswith("def "):
            print(line.strip())
'''


def test():
    complaint = """
    The ceiling fan in Hostel D Room 214 is not working properly.
    Since yesterday it is making sparks and there is a burning smell.
    Please fix it immediately.
    """

    print("=" * 80)
    print("ORIGINAL COMPLAINT")
    print("=" * 80)
    print(complaint)

    # ------------------------------------------------------------------
    # Text Processing
    # ------------------------------------------------------------------
    normalized = normalize_complaint(complaint)
    print("\nNormalized Complaint:")
    print(normalized)

    keywords = extract_keywords(normalized)
    print("\nKeywords:")
    print(keywords)

    # ------------------------------------------------------------------
    # Categorization
    # ------------------------------------------------------------------
    category = classify_category(normalized)
    print("\nCategory:")
    print(category)

    subcategory = classify_subcategory(normalized, category)
    print("\nSubcategory:")
    print(subcategory)

    category_score = category_confidence(normalized, category)
    print("\nCategory Confidence:")
    print(category_score)

    # ------------------------------------------------------------------
    # Complaint Generation
    # ------------------------------------------------------------------
    title = generate_title(normalized)
    print("\nGenerated Title:")
    print(title)

    description = generate_professional_description(normalized)
    print("\nProfessional Description:")
    print(description)

    summary = summarize_issue(normalized)
    print("\nSummary:")
    print(summary)

    # ------------------------------------------------------------------
    # Priority
    # ------------------------------------------------------------------
    safety_keywords = detect_safety_keywords(normalized)
    print("\nSafety Keywords:")
    print(safety_keywords)

    priority = calculate_priority(normalized)
    print("\nPriority:")
    print(priority)

    explanation = explain_priority(normalized, category, subcategory, priority)
    print("\nPriority Explanation:")
    print(explanation)

    # ------------------------------------------------------------------
    # Embeddings & Duplicate Detection
    # ------------------------------------------------------------------
    embedding = generate_embedding(normalized)
    print("\nEmbedding Dimension:")
    print(len(embedding))

    existing = [
        "Fan not working in Hostel D Room 214.",
        "Water leakage near washroom.",
        "Projector not working in Room 108.",
        "Internet is slow in Hostel A."
    ]

    similarities = []

    for item in existing:
        score = compare_similarity(normalized, item)
        similarities.append((item, score))

    print("\nSimilarity Scores:")
    for item, score in similarities:
        print(score, " -> ", item)

    
    # ------------------------------------------------------------------
    # Department Recommendation
    # ------------------------------------------------------------------
    department = recommend_department(normalized, category, subcategory)
    print("\nRecommended Department:")
    print(department)

    confidence = recommendation_confidence(normalized, category, subcategory, department)
    print("\nDepartment Confidence:")
    print(confidence)

    fallback = fallback_department(category, subcategory)
    print("\nFallback Department:")
    print(fallback)

    # ------------------------------------------------------------------
    # Final Output
    # ------------------------------------------------------------------
    result = {
        "normalized": normalized,
        "keywords": keywords,
        "category": category,
        "subcategory": subcategory,
        "category_confidence": category_score,
        "title": title,
        "description": description,
        "summary": summary,
        "priority": priority,
        "priority_explanation": explanation,
        "department": department,
        "department_confidence": confidence,
        #"duplicate": detect_duplicate,
        #"ranked_duplicates": ranked
    }

    print("\n" + "=" * 80)
    print("FINAL RESULT")
    print("=" * 80)
    print(result)

    return result

test()