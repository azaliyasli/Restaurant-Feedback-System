async function analyze() {
    const comment = document.getElementById("commentInput").value;

    if (comment.trim() === "") {
        alert("Please enter your comment!");
        return;
    }

    try {
        // Save Comment into Database
        const saveResponse = await fetch("http://127.0.0.1:5000/comment", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ comment })
        });
        const saveResult = await saveResponse.json();
        const comment_id = saveResult.comment_id;

        // Send Request to AI API
        const response = await fetch("https://restaurant-feedback-system-0h88.onrender.com/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: comment })
        });
        const result = await response.json();
        const prediction = result.prediction;

        document.getElementById("screen-entry").classList.add("hidden");
        document.getElementById("screen-positive").classList.add("hidden");
        document.getElementById("screen-negative").classList.add("hidden");
        document.getElementById("screen-feedback-received").classList.add("hidden");

        if (prediction === 1) {
            document.getElementById("screen-positive").classList.remove("hidden");
        } else {
            document.getElementById("screen-negative").dataset.commentId = comment_id;
            document.getElementById("screen-negative").classList.remove("hidden");
        }

    } catch (error) {
        console.error("Error:", error);
        alert("Something went wrong. Check backend server!");
    }
}

async function sendFeedback() {
    const feedback = document.getElementById("feedbackInput").value;
    const comment_id = document.getElementById("screen-negative").dataset.commentId;

    if (feedback.trim() === "") {
        alert("Please enter your feedback!");
        return;
    }

    // Save Feedback into Database
    try {
        await fetch("http://127.0.0.1:5000/feedback", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ comment_id, feedback })
        });

        document.getElementById("screen-negative").classList.add("hidden");
        document.getElementById("screen-feedback-received").classList.remove("hidden");
        document.getElementById("feedbackInput").value = "";
    } catch (error) {
        console.error("Error:", error);
        alert("Feedback could not be sent!");
    }
}

function goBack() {
    document.getElementById("screen-positive").classList.add("hidden");
    document.getElementById("screen-negative").classList.add("hidden");
    document.getElementById("screen-feedback-received").classList.add("hidden");

    document.getElementById("screen-entry").classList.remove("hidden");
    document.getElementById("commentInput").value = "";
}