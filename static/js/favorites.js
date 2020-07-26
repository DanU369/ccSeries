let favButton=document.querySelector(".favButton")
let asta=favButton.getAttribute('data-title')
let id=favButton.getAttribute('data-id')

favButton.addEventListener('click',()=>{

    saveMovie(asta)

})

async function saveMovie(movie) {
    let response = await fetch(`/tv-show/`+id, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(movie)
    })
    if(response.ok) {
        let ceva = await response.json()

        favButton.parentElement.removeChild(favButton);
        console.log(ceva)
    }
}

