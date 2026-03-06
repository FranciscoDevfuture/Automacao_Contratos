
---

# 📄 Gerador de Contratos de Locação Automático

Este projeto é uma ferramenta em **Python** desenvolvida para automatizar a criação de contratos de locação. O script coleta os dados via terminal, preenche um modelo em `.docx` (Word) substituindo *tags* específicas e, opcionalmente, envia o documento gerado diretamente para o e-mail do cliente.

## 🚀 Funcionalidades

* **Coleta Dinâmica:** Interface via linha de comando para inserção de dados do locador, locatário e imóvel.
* **Manipulação de Documentos:** Utiliza a biblioteca `python-docx` para ler um template e substituir variáveis.
* **Envio de E-mail Automático:** Integração com servidores SMTP (ex: Gmail) para envio de anexos de forma segura usando TLS.
* **Multiplataforma:** Compatível com Windows e sistemas Unix (Linux/macOS) para limpeza de tela e manipulação de arquivos.

---

## 🛠️ Tecnologias e Bibliotecas

As seguintes ferramentas foram utilizadas no desenvolvimento:

* [Python 3.x](https://www.python.org/)
* [python-docx](https://python-docx.readthedocs.io/): Para manipulação de arquivos .docx.
* `smtplib` & `email`: Para composição e envio dos e-mails.
* `os` & `platform`: Para interação com o sistema operacional.

---

## 📋 Pré-requisitos

Antes de começar, você precisará instalar a biblioteca responsável por editar arquivos Word:

```bash
pip install python-docx

```

### ⚠️ Configuração Importante (Gmail)

Para que o envio de e-mail funcione, você não deve usar sua senha comum.

1. Acesse sua Conta Google.
2. Vá em **Segurança** > **Verificação em duas etapas** (ative se não tiver).
3. No final da página, procure por **Senhas de app**.
4. Crie uma nova senha para "E-mail" e copie o código de 16 dígitos gerado para a variável `MINHA_SENHA` no código.

---

## 📂 Estrutura do Projeto

Para que o script funcione corretamente, seu diretório deve estar assim:

```text
.
├── gerador_contrato.py      # O script principal
├── modelo_contrato.docx     # O arquivo Word com as tags {exemplo}
└── README.md                # Documentação

```

> **Nota:** O arquivo `modelo_contrato.docx` deve conter as chaves exatamente como definidas no dicionário do script (ex: `{locador_nome}`, `{locatario_cpf}`, etc.).

---

## 🕹️ Como usar

1. Certifique-se de que o arquivo `modelo_contrato.docx` está na mesma pasta do script.
2. Execute o script:
```bash
python gerador_contrato.py

```


3. Responda às perguntas solicitadas no terminal.
4. Ao final, o arquivo será gerado com o nome `Contrato_Nome_Do_Locatario.docx`.
5. Se desejar, informe o e-mail do cliente para realizar o envio imediato.

---

## 🔒 Segurança

**Atenção:** Nunca publique seu e-mail ou senha de app em repositórios públicos. Recomenda-se o uso de variáveis de ambiente ou um arquivo `.env` para proteger seus dados sensíveis. No código atual, certifique-se de remover suas credenciais antes de dar `git push`.

---

**Desenvolvido por Francisco José Dos Santos** 🚀

---

