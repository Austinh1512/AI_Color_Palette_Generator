form = document.querySelector("#getPromptForm");

form.addEventListener("submit", async e => {
    e.preventDefault();
    const response = await fetch(
        "/palette",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({"prompt": form.elements.prompt.value})
        }
    );
    const { colors } = await response.json();
})