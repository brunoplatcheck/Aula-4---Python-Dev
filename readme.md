💬 Hashzap Chat - Documentação Completa
Hashzap é um aplicativo de chat em tempo real multiplataforma desenvolvido com tecnologias modernas, oferecendo versões para web e desktop.

🌟 Recursos Principais
Chat em tempo real com tecnologia WebSocket

Multiplataforma: funciona no navegador e como aplicativo desktop

Interface moderna com temas personalizáveis

Sistema de salas de chat (versão Flet)

Histórico de mensagens com carimbo de data/hora

Notificações de entrada/saída de usuários

🛠️ Tecnologias Utilizadas
Backend:

Python 3.x

Flask (para versão web)

Flask-SocketIO (comunicação em tempo real)

Frontend:

HTML5, CSS3, JavaScript/jQuery (versão web)

Flet (para versão desktop - multiplataforma)

📁 Estrutura do Projeto
Copy
hashzap/
├── app.py                # Servidor principal Flask + Socket.IO
├── main.py               # Alternativa do servidor
├── templates/
│   └── index.html        # Interface web principal
├── homepage.html         # Versão alternativa da interface web
├── hashzap.py            # Versão GUI completa com Flet
├── codigo.py            # Versão Flet simplificada
└── README.md             # Documentação do projeto
🚀 Como Executar
🌐 Versão Web
Instale as dependências:

bash
Copy
pip install flask flask-socketio simple-websocket
Execute o servidor:

bash
Copy
python app.py
Acesse no navegador:

Copy
http://localhost:5000
🖥️ Versão Desktop (Flet)
Instale o Flet:

bash
Copy
pip install flet
Execute a versão simplificada:

bash
Copy
python codigo.py
Ou a versão completa:

bash
Copy
python hashzap.py
O aplicativo será aberto automaticamente no seu navegador padrão

🔧 Configuração
Portas:

Servidor web: 5000

Aplicativo Flet: 8000

Personalização:

Cores do tema podem ser alteradas nos arquivos hashzap.py ou index.html

Nome do aplicativo pode ser modificado nos arquivos de interface

📌 Notas Importantes
Para desenvolvimento local, ambos os servidores (Flask e Flet) podem ser executados simultâneamente

A versão Flet oferece recursos adicionais como:

Múltiplas salas de chat

Interface mais rica

Melhor organização de mensagens

A versão web é mais simples e focada em funcionalidade básica de chat

📄 Licença
Este projeto é open-source e está disponível sob a licença MIT. Sinta-se à vontade para modificar e distribuir conforme suas necessidades.

🤝 Contribuição
Contribuições são bem-vindas! Por favor, abra uma issue ou pull request no repositório do projeto.

Divirta-se conversando! 💬🚀

#   A u l a - 4 - - - P y t h o n - D e v  
 