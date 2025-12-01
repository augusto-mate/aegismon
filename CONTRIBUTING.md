# Diretrizes de Contribuição para AegisMon

Agradecemos o seu interesse em contribuir para o projeto AegisMon!

Para garantir um fluxo de trabalho eficiente e manter a qualidade do código, por favor, siga estas diretrizes:

## 🏷 Versões e Commits

Utilizamos o padrão **Conventional Commits** para manter um histórico de commits limpo e significativo.

Cada mensagem de commit deve seguir o formato: `<tipo>(<escopo opcional>): <descrição>`

| Tipo        | Descrição                                                                      | Exemplo                                             |
|-------------|--------------------------------------------------------------------------------|-----------------------------------------------------|
| `feat`      | Nova funcionalidade.                                                           | `feat: adiciona suporte a SHA512`                   |
| `fix`       | Correção de bug.                                                               | `fix(cli): corrige erro de argumento`               |
| `docs`      | Mudanças na documentação.                                                      | `docs: atualiza README com novos comandos`          |
| `refactor`  | Mudança de código que não corrige bug nem adiciona feature.                      | `refactor(scanner): simplifica função de hash`      |
| `test`      | Adicionando ou corrigindo testes.                                              | `test: adiciona teste para heurísticas`             |
| `chore`     | Manutenção de build/dependências/ferramentas.                                  | `chore: atualiza pyyaml para v6.0`                  |

## 🚀 Como Contribuir

1.  **Fork** o repositório.
2.  Crie uma **Branch** com um nome descritivo (ex: `feat/adicionar-sha512`).
3.  Faça suas alterações e use as **Mensagens de Commit** apropriadas.
4.  Crie um **Pull Request (PR)** para a branch `main` do AegisMon, descrevendo claramente as mudanças e por que elas são necessárias.
