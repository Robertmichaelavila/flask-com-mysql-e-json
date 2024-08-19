//função que lista os elementos que estão no arquivo .json
function dados(){
    //buscar dados no arquivo
    fetch('http://127.0.0.1:5000/json/produtos/motos')
        .then(response => response.json())
        .then(motos => {
            const container = document.querySelector("main")

            motos.map(moto => {
                const card = document.createElement("div")
                card.classList.add("card")

                const titulo = document.createElement("h2")
                titulo.textContent = moto.modelo

                const img = document.createElement("img")
                img.src = moto.imagem
                img.alt = moto.modelo

                const marca = document.createElement("p")
                marca.textContent = moto.marca

                const ano = document.createElement("p")
                ano.textContent = moto.ano

                const btn = document.createElement("button")
                btn.textContent = 'Adicionar ao Carrinho'

                const preco = document.createElement("h3")
                preco.textContent = `R$ ${moto.preco}`


                card.appendChild(img)
                card.appendChild(titulo)
                card.appendChild(marca)
                card.appendChild(ano)
                card.appendChild(preco)
                card.appendChild(btn)
                container.appendChild(card)
            })
        })
}

dados()