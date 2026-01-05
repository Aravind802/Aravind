async function compare() {
    const promptInput = document.getElementById("prompt");
    const results = document.getElementById("results");

    const prompt = promptInput.value.trim();

    if (!prompt) {
        results.innerHTML = "<p>Please enter a prompt.</p>";
        return;
    }

    results.innerHTML = "<p>Loading...</p>";

    try {
        const response = await fetch("/compare", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt })
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();

        results.innerHTML = `
            <div class="card">
                <h3>OpenAI</h3>
                <pre>${data.openai}</pre>
            </div>
            <div class="card">
                <h3>Claude</h3>
                <pre>${data.claude}</pre>
            </div>
            <div class="card">
                <h3>Gemini</h3>
                <pre>${data.gemini}</pre>
            </div>
        `;
    } catch (error) {
        results.innerHTML = "<p>Failed to fetch results.</p>";
        console.error(error);
    }
}