---
name: codex-ai-framework
description: Inicializa ou adapta um framework documental de engenharia assistida por IA em qualquer repositório, independentemente da linguagem, criando AGENTS.md, orquestração, workflows, memória, gates e templates a partir de evidências locais. Use quando o usuário quiser preparar um projeto novo ou existente para trabalho contínuo com Codex. Não use para alterar apenas documentação comum.
---

# Codex AI Framework

Prepare o repositório para colaboração contínua com IA sem impor uma linguagem ou arquitetura.

## Antes de instalar

1. Confirme a raiz do projeto e leia qualquer `AGENTS.md` aplicável.
2. Verifique `git status` e preserve alterações preexistentes.
3. Inspecione apenas fontes locais: árvore, manifests, configuração, testes, CI e documentação.
4. Não trate nomes de pastas como prova de tecnologia ou arquitetura.
5. Não leia nem copie valores de segredos. Registre somente nomes de variáveis quando necessário.

## Escolha do modo

- Projeto vazio: instale a base com contexto marcado como `[PENDENTE DE CONFIRMAÇÃO]`.
- Projeto existente sem framework: instale a base e personalize a memória com fatos confirmados.
- Projeto com `AGENTS.md` ou `docs/IA`: não sobrescreva. Faça diagnóstico, apresente conflitos e peça autorização antes de mesclar.

## Instalação

1. Execute primeiro `scripts/install_framework.py --project <raiz> --dry-run`.
2. Revise a lista de arquivos e os conflitos informados.
3. Se não houver colisões, execute novamente sem `--dry-run`.

O instalador nunca sobrescreve arquivos. Se houver conflito, faça diagnóstico e proponha uma mesclagem manual; não contorne a proteção.

Depois da cópia:

1. Confirme que o instalador substituiu os marcadores básicos de projeto e data.
2. Leia [references/project-discovery.md](references/project-discovery.md) e preencha apenas fatos sustentados por arquivos locais.
3. Mantenha tecnologias desconhecidas como `[PENDENTE DE CONFIRMAÇÃO]`.
4. Adapte workflows somente quando a estrutura real exigir; preserve contratos de autorização e segurança.
5. Execute `scripts/validate_framework.py --project <raiz>`, além das verificações reais do projeto.
6. Informe separadamente o que foi analisado, confirmado, criado, personalizado e validado.
7. Não faça commit, push, instalação de dependência ou ação externa sem pedido explícito.

## Resultado mínimo

- `AGENTS.md` ativa o framework.
- `docs/IA/ORQUESTRADOR.md` roteia o trabalho.
- `docs/IA/MEMORIA/` contém contexto, estado, tarefas, decisões, riscos e histórico.
- `docs/IA/WORKFLOWS/` cobre bug, feature, documentação, testes, revisão, deploy e memória.
- `docs/IA/PROMPTS/` separa descoberta, diagnóstico, plano, implementação, verificação, revisão e entrega.
- `docs/IA/PERSONAS/` define responsabilidades sem exigir agentes separados.
- `docs/IA/CHECKLISTS/` contém gates de descoberta, implementação e memória.
- `docs/IA/TEMPLATES/` oferece registros reutilizáveis.

O framework organiza o trabalho; ele não inventa regras de negócio nem concede autorização adicional.
