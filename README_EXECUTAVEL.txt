# Instruções para gerar o executável do app bancário

1. Certifique-se de que o PyInstaller está instalado no seu ambiente:
   
   pip install pyinstaller

2. Gere o executável rodando o comando abaixo no terminal, dentro da pasta do projeto:

   pyinstaller --noconfirm --onefile --windowed --icon=icone.ico ex043.py

- O parâmetro --windowed evita que o terminal seja aberto junto ao app.
- O parâmetro --icon permite adicionar um ícone personalizado (opcional, remova se não tiver o arquivo icone.ico).
- O executável será gerado na pasta dist.

3. O arquivo final estará em dist/ex043.exe

Se quiser, posso rodar o comando para você agora.