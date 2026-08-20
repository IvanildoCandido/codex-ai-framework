# Codex AI Framework

Uma skill reutilizável para preparar projetos novos ou existentes para colaboração contínua com o Codex, independentemente da linguagem, framework ou tipo de aplicação.

Ela foi extraída de uma experiência real de documentação, mas não contém regras de negócio, tecnologias, credenciais ou dados do projeto de origem.

## O que a skill faz

Quando utilizada em um projeto, a skill:

1. analisa a estrutura e as configurações existentes;
2. identifica linguagens, frameworks, comandos, testes e CI por evidências locais;
3. cria um `AGENTS.md` para ativar as instruções automaticamente;
4. cria `docs/IA` com Orquestrador, memória, workflows, gates e templates;
5. registra somente informações confirmadas;
6. marca informações desconhecidas como `[PENDENTE DE CONFIRMAÇÃO]`;
7. preserva arquivos e alterações já existentes;
8. não executa deploy, migrations, instalações ou outras ações externas sem autorização.

O framework funciona com JavaScript, TypeScript, Python, Java, PHP, Go, Rust, C#, aplicativos mobile, sistemas web, APIs, monorepos ou qualquer outra estrutura que o Codex consiga analisar.

## Instalação da skill

Clone este repositório privado diretamente no diretório pessoal de skills do Codex:

```bash
git clone git@github.com:IvanildoCandido/codex-ai-framework.git ~/.codex/skills/codex-ai-framework
```

Se a pasta já existir, não sobrescreva automaticamente. Compare as versões antes de atualizar.

Se preferir não executar comandos, peça ao Codex:

> Instale a skill `codex-ai-framework` a partir deste repositório GitHub privado.

Após a instalação, a skill ficará disponível nas próximas interações do Codex.

Para atualizar uma instalação clonada:

```bash
git -C ~/.codex/skills/codex-ai-framework pull --ff-only
```

## Usar em um projeto novo e vazio

Crie e abra uma pasta vazia no Codex. Você pode apenas dizer:

> Use a skill `codex-ai-framework` para preparar este projeto novo.

O Codex criará:

```text
meu-projeto/
├── AGENTS.md
└── docs/
    └── IA/
        ├── ORQUESTRADOR.md
        ├── README.md
        ├── CHECKLISTS/
        ├── MEMORIA/
        ├── TEMPLATES/
        └── WORKFLOWS/
```

Como ainda não existe código, tecnologias e comandos ficarão como `[PENDENTE DE CONFIRMAÇÃO]`. Depois de criar a aplicação na linguagem desejada, peça:

> Analise a estrutura atual e atualize o contexto e a memória do framework de IA.

O Codex identificará a tecnologia pelos arquivos reais do projeto.

## Usar enquanto o Codex cria um projeto novo

Você também pode solicitar o projeto e o framework na mesma conversa:

> Crie um novo projeto em Python para uma API e use a skill `codex-ai-framework` para preparar a documentação de IA.

Ou:

> Crie um aplicativo na tecnologia mais adequada para esta ideia e inicialize o framework de IA.

A skill não escolhe uma linguagem por conta própria quando essa decisão muda o produto. O Codex deverá confirmar a escolha ou apresentar opções quando necessário.

## Usar em um projeto que já existe

Abra a raiz do projeto existente no Codex e diga:

> Use a skill `codex-ai-framework` para analisar e preparar este projeto sem sobrescrever arquivos existentes.

O Codex examinará manifests, configurações, testes, documentação, CI e estrutura do código. Em seguida, criará e personalizará o framework com fatos encontrados no repositório.

Se já existir `AGENTS.md` ou `docs/IA`, a instalação será interrompida. O Codex deverá mostrar os conflitos e pedir autorização antes de mesclar qualquer conteúdo.

## Usar no dia a dia

Depois da inicialização, não é necessário mencionar a skill em todas as solicitações. O `AGENTS.md` orientará o Codex a consultar o Orquestrador e a memória do projeto.

Exemplos:

```text
Corrija o erro de autenticação.
Crie testes para este serviço.
Planeje esta nova funcionalidade.
Revise as alterações ainda não commitadas.
Atualize a documentação e a memória técnica.
Prepare o deploy, mas não execute.
```

## Instalação manual do template

O instalador incluído pode ser executado diretamente:

```bash
python3 scripts/install_framework.py --project /caminho/do/projeto
```

Ele aborta caso algum arquivo de destino já exista. Essa proteção evita sobrescrever instruções ou documentação de outro projeto.

Após a cópia, o Codex deve substituir os marcadores `{{PROJECT_NAME}}` e `{{DATE}}`, analisar o projeto e preencher a memória com evidências locais.

## Arquivos deste repositório

```text
codex-ai-framework/
├── SKILL.md
├── agents/openai.yaml
├── assets/project-template/
├── references/project-discovery.md
└── scripts/install_framework.py
```

- `SKILL.md`: comportamento da skill.
- `agents/openai.yaml`: nome e prompt exibidos pelo Codex.
- `assets/project-template`: arquivos colocados nos projetos.
- `references/project-discovery.md`: critérios para analisar diferentes tecnologias.
- `scripts/install_framework.py`: cópia segura do template.

## Garantias de segurança

- Não sobrescreve arquivos existentes silenciosamente.
- Não copia informações do projeto usado como inspiração.
- Não inventa regras de negócio.
- Não registra valores secretos ou dados pessoais.
- Não transforma documentação histórica em prova do estado atual.
- Não executa commit, push, deploy, migration ou seed sem autorização.

## Verificação do próprio framework

O projeto possui testes sem dependências externas:

```bash
python3 scripts/test_framework.py
python3 scripts/validate_framework.py --project assets/project-template --allow-placeholders
```

O primeiro comando testa simulação, instalação, substituição de marcadores, validação, datas inválidas e proteção contra colisões. O segundo verifica estrutura obrigatória, links e independência em relação ao projeto de origem.
