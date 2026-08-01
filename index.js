require("dotenv").config();
const { createClient } = require("@supabase/supabase-js");
const OpenAI = require("openai");

const express = require("express");

const app = express();
const PORT = 3000;
const supabase = createClient(
    process.env.SUPABASE_URL,
    process.env.SUPABASE_PUBLISHABLE_KEY
);
const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
});

app.use(express.json());

app.get("/", (req, res) => {
  res.send("FixAI DevOps backend is running!");
});

app.get("/test-db", async (req, res) => {
  const { data, error } = await supabase
    .from("profiles")
    .select("*");

  if (error) return res.status(500).json({ error: error.message });

  res.json(data);
});

app.post("/api/issues", async (req, res) => {
    const { title, description, priority = "medium" } = req.body;

    if (!title || !description) {
        return res.status(400).json({
            error: "Title and description are required"
        });
    }

    const { data, error } = await supabase
        .from("issues")
        .insert([
    {
        title,
        description,
        status: "open",
        priority
    }
])
        .select();

    if (error) {
        return res.status(500).json({
            error: error.message
        });
    }

    return res.status(201).json({
        message: "Issue saved successfully",
        issue: data
    });
});

app.get("/api/issues", async (req, res) => {
    const { data, error } = await supabase
        .from("issues")
        .select("*")
        .order("created_at", { ascending: false });

    if (error) {
        return res.status(500).json({
            error: error.message
        });
    }

    res.json(data);
});
app.patch("/api/issues/:id/status", async (req, res) => {
    const { id } = req.params;
    const { status } = req.body;

    if (!status) {
        return res.status(400).json({
            error: "Status is required"
        });
    }

    const { data, error } = await supabase
        .from("issues")
        .update({ status })
        .eq("id", id)
        .select();

    if (error) {
        return res.status(500).json({
            error: error.message
        });
    }

    return res.json({
        message: "Issue status updated successfully",
        issue: data
    });
});
app.post("/api/analyze", async (req, res) => {
    console.log(">>> ANALYZE ROUTE HIT <<<", req.body);
    try {
        const { title, description } = req.body;

        if (!title || !description) {
            return res.status(400).json({
                error: "Title and description are required"
            });
        }

        const response = await openai.responses.create({
            model: "gpt-4.1-mini",
            input: `Analyze this DevOps issue and suggest a solution.

Title: ${title}
Description: ${description}`
        });

        return res.json({
            analysis: response.output_text
        });

   } catch (error) {
  console.error("ANALYZE ERROR FULL:", error);
  console.error("ANALYZE ERROR MESSAGE:", error?.message);
  console.error("ANALYZE ERROR STATUS:", error?.status);

  return res.status(500).json({
    error: error?.message || "Unknown error",
    status: error?.status || 500
  });
}
});
app.get("/health", (req, res) => {
  res.status(200).json({
    status: "healthy",
    service: "FixAI DevOps",
    timestamp: new Date().toISOString(),
  });
});
app.listen(PORT, () => {
    console.log(`FixAI DevOps server running on http://localhost:${PORT}`);
});