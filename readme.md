# 💬 Hashzap Chat - Documentação Completa

**Hashzap** é um aplicativo de chat em tempo real **multiplataforma**, desenvolvido com tecnologias modernas, oferecendo versões para **web** e **desktop (GUI)** com suporte a múltiplas salas de conversa, interface leve e integração por WebSocket.

---

## 🌟 Recursos Principais

- 🔄 Comunicação em tempo real com **WebSocket**
- 🌐 Compatível com navegadores e como app de desktop (GUI)
- 🎨 Interface moderna com suporte a temas personalizáveis
- 🧩 Sistema de **salas de chat independentes** (versão Flet)
- 🕘 Histórico de mensagens com **carimbo de data e hora**
- 🔔 Notificações de **entrada e saída de usuários**

---

## 🛠️ Tecnologias Utilizadas

### Backend
- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/) — servidor web leve
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/) — comunicação em tempo real

### Frontend Web
- HTML5, CSS3
- JavaScript (jQuery)
- [Socket.IO](https://socket.io/) via CDN

### Frontend Desktop (GUI)
- [Flet](https://flet.dev/) — biblioteca Python para UIs modernas e multiplataforma

---

## 📁 Estrutura do Projeto

hashzap/ ├── app.py # Servidor principal Flask + Socket.IO ├── main.py # Alternativa de execução do servidor ├── templates/ │ └── index.html # Interface web principal (chat HTML + JS) ├── homepage.html # Versão alternativa da interface web ├── flet/ │ ├── hashzap.py # Versão GUI completa (com salas) │ └── codigo.py # Versão GUI simplificada └── README.md # Documentação do projeto

yaml
Copiar
Editar

---

## 🚀 Como Executar

### 🌐 Versão Web (Flask + Socket.IO)

1. Instale as dependências:
```bash
pip install flask flask-socketio simple-websocket
Execute o servidor:

bash
Copiar
Editar
python app.py
Acesse no navegador:

arduino
Copiar
Editar
http://localhost:5000
💡 Você pode abrir em múltiplas abas ou em dispositivos da mesma rede.

🖥️ Versão Desktop (Flet)
Instale o Flet:

bash
Copiar
Editar
pip install flet
Execute uma das versões:

Versão simplificada:

bash
Copiar
Editar
python codigo.py
Versão completa com múltiplas salas:

bash
Copiar
Editar
python hashzap.py
A aplicação abrirá automaticamente no seu navegador padrão.

🔧 Configurações
Portas padrão:

Servidor Flask: 5000

Aplicação Flet: 8000

Personalização:

As cores podem ser alteradas nos arquivos hashzap.py (Flet) ou index.html (web).

O nome do aplicativo e das salas também pode ser editado diretamente no código.

📌 Notas Importantes
É possível executar as duas versões em paralelo durante o desenvolvimento local.

A versão Flet possui:

Suporte a múltiplas salas

Interface com botões, cards, layout moderno

Melhor organização do histórico de mensagens

A versão web é focada na simplicidade e agilidade, ideal para navegadores.

📄 Licença
Este projeto é open-source e está licenciado sob a MIT License. Sinta-se livre para usar, estudar, modificar e distribuir conforme sua necessidade.

🤝 Contribuições
Contribuições são muito bem-vindas!
Se quiser colaborar com melhorias ou correções, por favor abra uma issue ou envie um pull request.

🔗 Repositório Oficial
https://github.com/brunoplatcheck/Aula-4---Python-Dev

Divirta-se conversando! 💬🚀

yaml
Copiar
Editar

---

Se quiser também posso gerar uma **versão em inglês** ou criar um `logo.svg` para o cabeçalho. Deseja?
