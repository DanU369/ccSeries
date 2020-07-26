let actors = document.querySelectorAll("li");
let panels=document.querySelectorAll(".panel");

for ( let i = 0; i < actors.length; i++) {
  actors[i].addEventListener("click", async function() {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("active");
    /* Toggle between hiding and showing the active panel */
    let panel = this.nextElementSibling;
    let actorId = this.getAttribute("data-id")
    await submit_entry(actorId, "/actors")
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  })
}

async function submit_entry(elementName, url) {
    let submitData = {
        'name': `${elementName}`
    };
    let response = await fetch(`${url}`, {
        method: "POST",
        mode: "cors",
        cache: "default",
        credentials: "include",
        headers: {"Content-Type": "application/json"},
        redirect: "follow",
        body: JSON.stringify(submitData)
    })
    let result = await response.json()
    add_movies(result)
}

function add_movies(titles){

  let ul=document.createElement("ul");
  for ( title of titles) {
    let li=document.createElement("li");
    li.textContent=title.title +" as "+title.character_name
    ul.appendChild(li)
  }
  console.log(titles)
  let panel=document.querySelector(`div[data-id="${titles[0].actor_id}"]`)
  panel.innerHTML=""
  console.log(panel)
  panel.appendChild(ul)
}