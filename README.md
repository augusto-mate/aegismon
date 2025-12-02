<h1 align="center">🛡 AegisMon — Advanced Security Scanner Toolkit 🔒</h1>

<p align="center">
  <a href="https://github.com/augusto-mate/aegismon/actions">
    <img src="https://github.com/augusto-mate/aegismon/actions/workflows/tests.yml/badge.svg" alt="Build">
  </a>
  <a href="https://github.com/augusto-mate/aegismon/releases">
    <img src="https://img.shields.io/github/v/release/augusto-mate/aegismon" alt="Release">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/augusto-mate/aegismon" alt="License">
  </a>
  <img src="https://img.shields.io/badge/coverage-pending-black" alt="Coverage">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python">
  <a href="https://augusto-mate.github.io/aegismon/">
    <img src="https://img.shields.io/badge/docs-online-gold" alt="Docs">
  </a>
</p>

<p align="center">
    <img src="./docs/assets/logo-aegismon-minimal.png" alt="Logo AegisMon" width="350" style="border:2px solid #ddd; padding:15px; border-radius:10px;">
</p>

**AegisMon** é uma ferramenta de código aberto para cibersegurança projetada para realizar varreduras de integridade de arquivos (FIM - File Integrity Monitoring), detecção de malware por assinatura e avaliação heurística de risco. Desenvolvido para ser modular e extensível, utiliza uma interface de linha de comando robusta.

---

## ✨ Funcionalidades Principais

* **Detecção Multifacetada:** Utiliza Assinaturas (Hashing), Heurísticas de Risco e Regras Personalizadas.
* **Múltiplos Hashing:** Suporte nativo para **MD5**, **SHA1** e **SHA256**.
* **Relatórios Estruturados:** Exportação de resultados em formato JSON para fácil processamento e integração.
* **Configurável:** Suporte a arquivos de configuração externos (YAML/JSON) e carregamento de banco de dados de assinaturas personalizado.
* **Arquitetura Modular:** Código organizado em pacotes `scanner`, `reports`, `logging` e `utils`.

## 📂 Estrutura do Projeto

```
aegismon/
├── cli.py                   # Interface de linha de comando
├── .github/workflows/       # CI/CD (deploy e testes)
├── docs/assets/             # Logos e elementos visuais do projeto 
├── logging/                 # Configuração e utilitários de logging
├── reports/                 # Geração de relatórios (JSON, etc.)
├── scanner/                 # Núcleo de escaneamento e assinaturas
├── tests/                   # Testes automatizados
├── utils/                   # Funções auxiliares
├── LICENSE                  # Licença MIT
├── CHANGELOG.md             # Histórico de alterações
├── CONTRIBUTING.md          # Diretrizes de contribuição
├── README.md                # Documentação principal
├── setup.py                 # Instalação via setuptools
└── requirements.txt         # Dependências do projeto
```

## ⚙️ Instalação e Uso

### Pré-requisitos

O **AegisMon** requer Python 3.8+ e as dependências listadas em `requirements.txt`.

```bash
# Clone o repositório
git clone https://github.com/augusto-mate/aegismon.git
cd aegismon

# Instale as dependências
pip install -r requirements.txt

# Instale o pacote localmente (modo editável para desenvolvimento)
pip install -e .
```

### Uso da CLI

O comando principal é `aegismon scan`.

```bash
# 1. Scan básico em um diretório (exibe resultados verbose no terminal)
aegismon scan /caminho/para/analise --verbose

# 2. Scan e exportação do relatório JSON
aegismon scan /home/user/documentos --json ./report.json

# 3. Scan usando um arquivo de configuração externo (hashes e log level)
aegismon scan /var/www --config ./config/config.yaml

# 4. Scan carregando um banco de assinaturas personalizado
aegismon scan /etc --signatures ./config/signatures.json
```

## 🤝 Contribuindo

Cada contribuição fortalece o **AegisMon** como projeto de portfólio e aprendizado.  
Antes de começar, leia o [`CONTRIBUTING.md`](CONTRIBUTING.md) para entender:
- Como propor melhorias
- Como relatar problemas
- Como enviar código seguindo o padrão do projeto

Sua participação é bem‑vinda e valorizada!

## 📜 Licença

Este projeto é distribuído sob a **Licença MIT**, permitindo uso, modificação e distribuição livre, desde que mantidos os créditos originais.  
Consulte o arquivo [`LICENSE`](LICENSE) para mais detalhes.

## 👤 Autor

- **Augusto Mate** — Desenvolvedor e mantenedor principal do AegisMon    
	- GitHub: [@augusto-mate](https://github.com/augusto-mate)  
	- LinkedIn: [linkedin.com/in/augusto-mate/](https://www.linkedin.com/in/augusto-mate/)

---

> 🌟 *AegisMon — monitorar, proteger e impressionar: um marco de inovação que transforma código em impacto.*

