async function analyze() {
    const comment = document.getElementById("commentInput").value;

    if (comment.trim() === "") {
        alert("Please enter your comment!");
        return;
    }

    try {
        const response = await fetch(
            "https://restaurant-feedback-system-0h88.onrender.com/predict",
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: comment })
            }
        );

        if (!response.ok) {
            console.error("API Error:", response.status, response.statusText);
            alert("Analysis failed due to a server error.");
            return;
        }

        const result = await response.json();
        console.log("Model Response:", result);

        const prediction = result.prediction;

        document.getElementById("screen-entry").classList.add("hidden");
        document.getElementById("screen-positive").classList.add("hidden");
        document.getElementById("screen-negative").classList.add("hidden");
        document.getElementById("screen-feedback-received").classList.add("hidden");

        if (prediction === 1) {
            document.getElementById("screen-positive").classList.remove("hidden");
        } else {
            document.getElementById("screen-negative").classList.remove("hidden");
        }

    } catch (error) {
        console.error("Fetch/Network Error:", error);
        alert("A network error occurred. Is the server running?");
    }
}

function sendFeedback() {
    document.getElementById("screen-negative").classList.add("hidden");
    document.getElementById("screen-feedback-received").classList.remove("hidden");
    document.getElementById("feedbackInput").value = "";
}

function goBack() {
    document.getElementById("screen-positive").classList.add("hidden");
    document.getElementById("screen-negative").classList.add("hidden");
    document.getElementById("screen-feedback-received").classList.add("hidden");

    document.getElementById("screen-entry").classList.remove("hidden");

    document.getElementById("commentInput").value = "";
}