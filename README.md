# Discord Fact Bot

## Visão Geral

O **Discord Fact Bot** é uma solução automatizada desenvolvida em Python para integração com servidores do Discord, com foco na interação com usuários, na disponibilização de informações curiosas e na utilização de tecnologias de síntese de voz.

O projeto combina a biblioteca `discord.py`, integração com API REST e processamento de texto para fala, proporcionando uma experiência interativa e automatizada aos usuários.

## Objetivos do Projeto

- Automatizar respostas a comandos enviados no Discord.
- Disponibilizar curiosidades por meio de uma API externa.
- Implementar síntese de voz para reprodução de informações em formato de áudio local.
- Aplicar conceitos de programação assíncrona, integração de serviços e tratamento de erros.

## Funcionalidades

### 1. Sistema de Boas-Vindas

O comando `!start` permite que o bot envie automaticamente uma mensagem de boas-vindas, identificando o usuário que executou o comando.

### 2. Consulta de Curiosidades

O comando `!fact` realiza uma requisição HTTP à API Useless Facts para obter uma curiosidade aleatória.

A funcionalidade contempla:
- Consumo de dados no formato JSON.
- Extração do conteúdo informativo da resposta.
- Verificação do código de status HTTP.
- Tratamento de falhas de conexão e indisponibilidade do serviço.

### 3. Síntese de Voz

O projeto utiliza a biblioteca `pyttsx3` para converter o texto da curiosidade em fala.

Após o envio da mensagem ao Discord, o sistema solicita a reprodução local do conteúdo por meio do mecanismo de síntese de voz.

### 4. Integração com o Discord

O bot utiliza comandos prefixados por `!`, permitindo que os usuários acionem suas funcionalidades diretamente nos canais de texto autorizados do servidor.

## Tecnologias Utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal de desenvolvimento |
| discord.py | Integração com a plataforma Discord |
| Requests | Comunicação com a API externa |
| pyttsx3 | Síntese de voz |
| Useless Facts API | Fornecimento de curiosidades em formato JSON |

## Requisitos de Instalação

É necessário possuir Python instalado e acesso à internet para a comunicação com o Discord e a API de curiosidades.

Instale as dependências com o comando:

```bash
pip install discord.py requests pyttsx3
```

## Configuração e Execução

1. Crie uma aplicação no [Discord Developer Portal](https://discord.com/developers/applications).
2. Configure o bot e habilite as permissões necessárias, incluindo o *Message Content Intent*.
3. Armazene o token de autenticação em um arquivo local chamado `token.py`.
4. Insira o token na variável `token`, sem compartilhá-lo publicamente.
5. Execute o arquivo principal do projeto.
6. Utilize os comandos `!start` e `!fact` em um servidor no qual o bot esteja devidamente configurado.

## Segurança

O token de autenticação deve ser tratado como uma credencial confidencial. Recomenda-se armazená-lo em uma variável de ambiente ou em um arquivo excluído do controle de versão por meio do `.gitignore`.

Credenciais não devem ser incluídas diretamente no código-fonte publicado ou compartilhadas em repositórios públicos.

## Tratamento de Erros e Limitações

O sistema verifica falhas na comunicação com a API e informa o usuário quando não consegue obter uma curiosidade.

A síntese de voz é executada localmente no computador ou servidor em que o programa está em funcionamento. A reprodução automática em um canal de voz do Discord não está contemplada na implementação atual.

## Possibilidades de Evolução

O projeto poderá receber futuras melhorias, incluindo:
- Comandos adicionais e novas categorias de curiosidades.
- Configuração de idioma para as informações obtidas.
- Registro de atividades e aprimoramento do monitoramento de erros.
- Integração com canais de voz do Discord.
- Implementação de configurações personalizáveis por servidor.
- Aprimoramento da segurança e da organização da arquitetura do sistema.

## Considerações Finais

O Discord Fact Bot demonstra a aplicação prática de integração entre plataformas digitais, serviços externos e recursos de síntese de voz. Sua estrutura permite a expansão gradual das funcionalidades e serve como base para o desenvolvimento de soluções mais abrangentes de automação e interação em ambientes digitais.

---

**Projeto:** Discord Fact Bot  
**Categoria:** Automação e integração de serviços  
**Linguagem:** Python  
**Status:** Versão inicial em desenvolvimento
