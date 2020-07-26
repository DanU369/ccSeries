let titleBtn=document.querySelector(".titlebtn")
let yearBtn=document.querySelector(".yearbtn")
let runtimeBtn=document.querySelector(".runtimebtn")
let ratingBtn=document.querySelector(".ratingbtn")
let genresBtn=document.querySelector(".genresbtn")
let dataContainer=document.getElementsByClassName("data-container")[0]

titleBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
yearBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
runtimeBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
ratingBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
genresBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`


titleBtn.addEventListener('click',sortByTitle)
yearBtn.addEventListener('click',sortByYear)
runtimeBtn.addEventListener('click',sortByRuntime)
ratingBtn.addEventListener('click',sortByRating)
genresBtn.addEventListener('click',sortByGenres)

async function sortByTitle() {
    let request=await fetch(`${window.location.href}`, {
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }

    })
    dataContainer.innerHTML=''
    let datas=await request.json()
    console.log(datas)
    datas.sort(function(a, b){
  var x = a.title.toLowerCase();
  var y = b.title.toLowerCase();
  if (x < y) {return -1;}
  if (x > y) {return 1;}
  return 0;
})
    if (titleBtn.classList.contains('asc')){
        yearBtn.innerText='Year'
        yearBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        runtimeBtn.innerText='Runtime'
        runtimeBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        ratingBtn.innerText='Rating'
        ratingBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        genresBtn.innerText='Genres'
        genresBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`

        titleBtn.innerText='Title'
        titleBtn.innerHTML+='<i class="fa fa-sort-asc" style="color :black"></i>'
        titleBtn.classList.remove('asc')
        titleBtn.classList.add('desc')
    }
    else{
        titleBtn.innerText='Title'
        titleBtn.innerHTML+='<i class="fa fa-sort-desc" style="color :black"></i>'
        titleBtn.classList.remove('desc')
        titleBtn.classList.add('asc')
        datas.reverse()
    }
    sorting(datas)

}

async function sortByYear() {
    let request=await fetch(`${window.location.href}`, {
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }

    })
    dataContainer.innerHTML=''
    let datas=await request.json()
    datas.sort(function(a, b){
  return a.year - b.year
})
    if (yearBtn.classList.contains('asc')){
        titleBtn.innerText='Title'
        titleBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        runtimeBtn.innerText='Runtime'
        runtimeBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        ratingBtn.innerText='Rating'
        ratingBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        genresBtn.innerText='Genres'
        genresBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`


        yearBtn.innerText='Release Year'
        yearBtn.innerHTML+='<i class="fa fa-sort-asc" style="color :black"></i>'
        yearBtn.classList.remove('asc')
        yearBtn.classList.add('desc')
    }
    else{
        yearBtn.innerText='Release Year'
        yearBtn.innerHTML+='<i class="fa fa-sort-desc" style="color :black"></i>'
        yearBtn.classList.remove('desc')
        yearBtn.classList.add('asc')
        datas.reverse()
    }
    sorting(datas)

}

async function sortByRuntime() {
    let request=await fetch(`${window.location.href}`, {
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }

    })
    dataContainer.innerHTML=''
    let datas=await request.json()
    datas.sort(function(a, b){
  return a.runtime - b.runtime

})
    if (runtimeBtn.classList.contains('asc')){
        titleBtn.innerText='Title'
        titleBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        yearBtn.innerText='Year'
        yearBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        ratingBtn.innerText='Rating'
        ratingBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        genresBtn.innerText='Genres'
        genresBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`


        runtimeBtn.innerText='Runtime'
        runtimeBtn.innerHTML+='<i class="fa fa-sort-asc" style="color :black"></i>'
        runtimeBtn.classList.remove('asc')
        runtimeBtn.classList.add('desc')
    }
    else{
        runtimeBtn.innerText='Release Year'
        runtimeBtn.innerHTML+='<i class="fa fa-sort-desc" style="color :black"></i>'
        runtimeBtn.classList.remove('desc')
        runtimeBtn.classList.add('asc')
        datas.reverse()
    }

    sorting(datas)

}

async function sortByRating() {
    let request=await fetch(`${window.location.href}`, {
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }

    })
    dataContainer.innerHTML=''
    let datas=await request.json()
    datas.sort(function(a, b){
  return a.rating - b.rating
})
    if (ratingBtn.classList.contains('asc')){
        titleBtn.innerText='Title'
        titleBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        yearBtn.innerText='Year'
        yearBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        runtimeBtn.innerText='Runtime'
        runtimeBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        genresBtn.innerText='Genres'
        genresBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`


        ratingBtn.innerText='Rating'
        ratingBtn.innerHTML+='<i class="fa fa-sort-asc" style="color :black"></i>'
        ratingBtn.classList.remove('asc')
        ratingBtn.classList.add('desc')
    }
    else{
        ratingBtn.innerText='Rating'
        ratingBtn.innerHTML+='<i class="fa fa-sort-desc" style="color :black"></i>'
        ratingBtn.classList.remove('desc')
        ratingBtn.classList.add('asc')
        datas.reverse()
    }
    sorting(datas)

}

async function sortByGenres() {
    let request=await fetch(`${window.location.href}`, {
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }

    })
    dataContainer.innerHTML=''
    let datas=await request.json()
    console.log(datas)
    datas.sort(function(a, b){
  var x = a.genres.toLowerCase();
  var y = b.genres.toLowerCase();
  if (x < y) {return -1;}
  if (x > y) {return 1;}
  return 0;
})
    if (genresBtn.classList.contains('asc')){
        titleBtn.innerText='Title'
        titleBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        yearBtn.innerText='Year'
        yearBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        runtimeBtn.innerText='Runtime'
        runtimeBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`
        ratingBtn.innerText='Rating'
        ratingBtn.innerHTML+=`<i class="fa fa-sort" style="color :black"></i>`

        genresBtn.innerText='Genres'
        genresBtn.innerHTML+='<i class="fa fa-sort-asc" style="color :black"></i>'
        genresBtn.classList.remove('asc')
        genresBtn.classList.add('desc')
    }
    else{
        genresBtn.innerText='Genres'
        genresBtn.innerHTML+='<i class="fa fa-sort-desc" style="color :black"></i>'
        genresBtn.classList.remove('desc')
        genresBtn.classList.add('asc')
        datas.reverse()
    }
    sorting(datas)

}

function sorting(argument) {
    for ( let i = 0; i < argument.length; i++){
        if (argument[i].homepage === null) {
        dataContainer.innerHTML+=`
        <tr class="${argument[i].id}">
                <td><a href="/tv-show/${argument[i].id}" >  ${argument[i].title} </a></td>
                <td>${argument[i].year} </td>
                <td>${argument[i].runtime} </td>
                <td>${argument[i].rating}</td>
                <td>${argument[i].genres}</td>
                <td>No Urls</td>
        </tr>`}
        else{
            dataContainer.innerHTML+=`
        <tr class="${argument[i].id}">
                <td><a href="/tv-show/${argument[i].id}" >  ${argument[i].title} </a></td>
                <td>${argument[i].year} </td>
                <td>${argument[i].runtime} </td>
                <td>${argument[i].rating}</td>
                <td>${argument[i].genres}</td>
                <td><a href="${argument[i].homepage}">Homepage</a> <a href=" ${ argument[1].trailer }">Trailer</a></td>
        </tr>`}
        }
    }
