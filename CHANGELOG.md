# CHANGELOG

## v1.0.0 — 2025-12-01 (Initial Stable Release)

Esta versão consolida todas as melhorias e correções em uma arquitetura modular e robusta, focada em extensibilidade e funcionalidade completa para portfólio.

### 🌟 Novas Funcionalidades

* **Scanner Robusto:** Implementação de um sistema de scanning baseado em assinaturas, heurísticas e múltiplos algoritmos de hashing (`MD5`, `SHA1`, `SHA256`).
* **Sistema de Severidade:** Introdução da classe `ScanResult` para calcular o nível de severidade (low, medium, high) com base nas detecções de heurísticas e assinaturas.
* **CLI Completa:** Interface de Linha de Comando (`cli.py`) com suporte a Configuração Externa (`--config`) e Assinaturas Externas (`--signatures`).

### 🛠 Refatorações e Melhorias

* Unificação da estrutura de saída dos relatórios (`results` e `stats`).
* Refatoração do sistema de logs para usar o módulo `logging` padrão do Python.
* Criação de `setup.py` e `requirements.txt` para fácil instalação e distribuição.