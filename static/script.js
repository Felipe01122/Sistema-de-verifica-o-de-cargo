document.getElementById('btn-buscar').addEventListener('click', async() =>{

    const nome = document.getElementById('nome').value;
    const id = document.getElementById('id').value;
    const erroDiv = document.getElementById('mensagem-erro');

    const resposta = await fetch('/index', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({nome,id,})
    });

    const resultado = await resposta.json();

    if (resposta.ok && resultado.sucesso){
        window.location.href = '/painel';
    } else{
        erroDiv.innerHTML = resultado.mensagem;
        erroDiv.className = "erro-visivel"
    }

})