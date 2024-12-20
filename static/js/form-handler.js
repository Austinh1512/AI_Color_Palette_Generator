form = document.querySelector("#getPromptForm");
container = document.querySelector(".container")

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
    container.innerHTML = "";

    colors.forEach(color => {
        const div = document.createElement("div");
        div.style.backgroundColor = color;
        div.classList.add("color");

        const span = document.createElement("span");
        span.innerText = color;
        div.appendChild(span)

        div.addEventListener("click", () => {
            navigator.clipboard.writeText(color)
        })

        container.appendChild(div);
    })
})