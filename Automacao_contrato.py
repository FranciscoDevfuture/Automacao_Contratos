#Bibliotecas usadas

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from docx import Document
import os
import platform

# --- CONFIGURAÇÕES DE EMAIL ---
# Se usar Gmail, gere uma "Senha de App" nas configurações da sua conta Google
MEU_EMAIL = "seu_email"
MINHA_SENHA = "sua_senha_app" 

def limpar_tela():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def enviar_email(destinatario, caminho_arquivo):
    try:
        print(f"\nTentando enviar e-mail para {destinatario}...")
        
        msg = MIMEMultipart()
        msg['From'] = MEU_EMAIL
        msg['To'] = destinatario
        msg['Subject'] = "Cópia do seu Contrato de Locação"

        corpo = "Olá, segue em anexo a cópia do seu contrato de locação gerada pelo nosso sistema."
        msg.attach(MIMEText(corpo, 'plain'))

        # Anexando o arquivo .docx
        with open(caminho_arquivo, "rb") as anexo:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(anexo.read())
            
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(caminho_arquivo)}")
        msg.attach(part)

        # Configuração do servidor (Exemplo: Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(MEU_EMAIL, MINHA_SENHA)
        server.sendmail(MEU_EMAIL, destinatario, msg.as_string())
        server.quit()
        
        print(f'[SUCESSO] O e-mail foi enviado com sucesso!')
    except Exception as e:
        print(f'[ERRO] Falha ao enviar e-mail: {e}')

def pegar_dados():
    limpar_tela()
    print('--- Sistema de Automação de Contratos ---')
    
    dados = {
        '{locador_nome}': input('Nome do Locador: '),
        '{Nacionalidade}': input('Nacionalidade: '),
        '{Estado_civil}': input('Estado Civil: '),
        '{Profissao}': input('Profissao?: '),
        '{num_rg}': input('Informe o RG: '),
        '{locador_cpf}': input('Informe CPF: '),
        '{endereco_imovel}': input('Endereço completo do Imóvel: '),
        '{locatario_nome}': input('Nome do Locatário: '),
        '{Profissao_locatario}': input('Profissao?: '),
        '{Estado_civil_locatario}': input('Estado Civil: '),
        '{num_rg_locatario}': input('Informe o RG: '),
        '{locatario_cpf}': input('CPF do Locatário: '),
        '{endereco_locatario}': input('Endereço Completo do Imóvel: '),
        '{valor_aluguel}': input('Valor do Aluguel (R$): '),
        '{prazo_meses}': input('Prazo da locação (em meses): '),
        '{vencimento}': input('Dia do vencimento (ex: 10): '),
        '{forma_pagamento}' : input('Forma de pagamento (PIX-BOLETO): '),
        '{valor_pagamento}': input('Informe o valor (R$): '),
        '{cidade}': input('Cidade/Estado (ex: São Paulo - SP): '),
        '{UF}': input('informe UF: '),
        '{data_emisao}' : input('Qual o dia da Emissão?: '),
        '{data_inicio}': input('Data do início: '),
        '{data_termino}': input('Data do término: '),
        '{cidade_foro}': input('Cidade do FORO: '),
        '{UF_foro}': input('UF: ')
    }
    return dados

def preencher_documento(dados, arquivo_modelo):
    try:
        doc = Document(arquivo_modelo)
        
        for paragraph in doc.paragraphs:
            for tag, valor in dados.items():
                if tag in paragraph.text:
                    paragraph.text = paragraph.text.replace(tag, valor)
                    
        nome_limpo = dados['{locatario_nome}'].replace(' ', '_')
        novo_arquivo = f'Contrato_{nome_limpo}.docx'
        
        doc.save(novo_arquivo)
        print(f'\n[SUCESSO] Contrato gerado localmente: {novo_arquivo}')
        
        return novo_arquivo # Retorna o nome para ser usado no envio de email
        
    except Exception as e:
        print(f'\n[ERRO] Não foi possível gerar o documento: {e}')
        return None

# --- Fluxo Principal ---
if __name__ == '__main__':
    template = 'modelo_contrato.docx'
    
    # Executa a coleta de dados
    informacoes = pegar_dados()
    
    # Gera o contrato
    arquivo_gerado = preencher_documento(informacoes, template)
    
    # Se o contrato foi gerado, pergunta sobre o e-mail
    if arquivo_gerado:
        print("\n" + "="*40)
        email_cliente = input("Digite o e-mail do cliente para enviar o arquivo (ou pressione ENTER para sair): ").strip()
        
        if email_cliente:
            enviar_email(email_cliente, arquivo_gerado)
        else:
            print("Processo finalizado sem envio de e-mail.")
