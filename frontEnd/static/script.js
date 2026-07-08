console.log("SupportLens JS Loaded");

async function analyzeIssue() {

    try {

        const formData = new FormData();

        formData.append(
            "issue",
            document.getElementById("issue").value
        );

        formData.append(
            "logs",
            document.getElementById("logs").value
        );

        const image = document.getElementById("image").files[0];

        if (image) {
            formData.append("image", image);
        }

        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();

        document.getElementById("result").innerHTML = `
            <h2>Analysis</h2>
            <pre class="analysis">${data.analysis}</pre>
        `; 

    } catch (error) {

        console.error(error);

        document.getElementById("result").innerHTML = `
            <h2>Error</h2>
            <pre>${error}</pre>
        `;

    }

}