// script.js

function getFila() {
    return JSON.parse(localStorage.getItem('filaAtendimento') || '[]');
}

function setFila(fila) {
    localStorage.setItem('filaAtendimento', JSON.stringify(fila));
}

function adicionarPessoa(nome) {
    const fila = getFila();
    fila.push({ nome, data: new Date().toLocaleString() });
    setFila(fila);
}

function listarFila() {
    const fila = getFila();
    const lista = document.getElementById('lista');
    lista.innerHTML = '';

    fila.forEach((item, index) => {
        const li = document.createElement('li');
        li.textContent = `${index + 1}. ${item.nome} - ${item.data}`;
        lista.appendChild(li);
    });
}

function limparFila() {
    if (confirm("Deseja realmente limpar o banco de dados?")) {
        localStorage.removeItem('filaAtendimento');
        location.reload();
    }
}
