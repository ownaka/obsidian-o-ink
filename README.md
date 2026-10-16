# ☵ O-Ink para Obsidian

**O** de Ownaka, **Ink** de tinta e de E-Ink.

Tema minimalista em estilo **E-Ink**, feito a partir da identidade visual de [ownaka.net](https://ownaka.net).
Fundo de pontinhos quase imperceptível, tipografia **Commit Mono** em tudo, cantos retos, bordas finas e um único verde de destaque, o mesmo do selo "online" do site.

> Entender como algo funciona por dentro é a melhor parte. Explicar pra alguém é a segunda.

<!-- Adicione aqui os prints reais do tema:
![O-Ink — modo escuro](assets/screenshots/dark.png)
![O-Ink — modo claro](assets/screenshots/light.png)
-->

## Princípios

- **Tinta e papel.** Duas paletas: escuro (preto `#0c0c0c` com texto bege de papel `#e6e1d5`) e claro (papel envelhecido com tinta escura).
- **Uma cor só pra chamar atenção.** O verde `#689d6a` aparece no que está ativo, feito ou online. O resto fica em tons de cinza quente.
- **Borda no lugar de sombra.** Tudo é separado por linhas de 1px, como os cards do site.
- **Monoespaçado de ponta a ponta.** A Commit Mono vem embutida no tema, não precisa instalar nada.

## Instalação

### Manual

1. Baixe `theme.css` e `manifest.json` (ou a release mais recente).
2. No seu cofre, crie a pasta `.obsidian/themes/O-Ink/` e coloque os dois arquivos nela.
3. Em **Configurações → Aparência → Temas**, escolha **O-Ink**.

### Pela linha de comando

```bash
git clone https://github.com/ownaka/obsidian-o-ink.git
cd obsidian-o-ink
python3 scripts/build.py --vault "~/caminho/do/seu/cofre"
```

## O que o tema muda

### Interface
- Fundo de pontinhos sutil atrás das notas, com intensidade e espaçamento ajustáveis.
- Aba ativa com uma linha verde no topo.
- Explorador de arquivos com o indicador `›` do site no arquivo aberto e pastas em minúsculas.
- Barra de status com o quadradinho verde "online".
- Paleta de comandos, menus e janelas como cards, com o item selecionado marcado em verde.
- Botões com o **flash E-Ink**: piscam invertidos ao clicar, como uma tela de papel eletrônico.
- Interruptores, campos e dicas flutuantes quadrados.
- Gráfico de conexões e Canvas na mesma paleta (o Canvas ganha os mesmos pontinhos).

### Markdown
| Elemento | Como fica |
| --- | --- |
| H1 e H2 | Fortes, com uma linha fina embaixo do H2 |
| H3 | Ganha o indicador `›` em verde |
| H4 a H6 | Viram rótulos em caixa alta, com o H4 entre colchetes: `[RÓTULO]` |
| Listas | Traço `–` no lugar da bolinha, como no site |
| Negrito / itálico | Branco / bege |
| Marca-texto | Verde translúcido |
| Links | Sublinhado fino; notas que não existem ficam tracejadas; externos ganham `↗` |
| Código | Blocos com borda, como os cards |
| Tabelas | Cabeçalho em caixa alta, números alinhados |
| Linha horizontal | Tracejada |
| Imagens | Filtro E-Ink (preto e branco com leve sépia), que realça ao passar o mouse |
| Propriedades | Viram um card, como o `[IDENTIDADE]` do site |

### Tarefas

| Sintaxe | Significado |
| --- | --- |
| `- [ ]` | A fazer |
| `- [x]` | Feita (verde) |
| `- [/]` | Em andamento |
| `- [-]` | Cancelada |
| `- [>]` | Adiada |
| `- [!]` | Importante |
| `- [?]` | Dúvida |
| `- [*]` | Ideia |

### Callouts

Todos os callouts viram cards com o título em colchetes, `[NOTA]`, `[DICA]`, nas cores do tema. E três callouts exclusivos:

```markdown
> [!card] Título
> Um card limpo, igual aos do site.

> [!terminal] Comandos
> docker compose up -d
> sudo systemctl restart jellyfin

> [!online] Status
> O selo verde de "online".
```

No `[!terminal]`, cada linha ganha um `$` verde na frente.

### Classes por nota (`cssclasses`)

Coloque nas propriedades da nota:

```yaml
---
cssclasses:
  - o-ink-numbered
---
```

| Classe | Efeito |
| --- | --- |
| `o-ink-numbered` | Numera os H2 como os cards do site: `[01]`, `[02]`… |
| `o-ink-wide` | Deixa a nota mais larga |
| `o-ink-cards` | Cada H2 vira o topo de um card |
| `o-ink-center` | Centraliza título e parágrafos |
| `o-ink-dots-off` | Tira os pontinhos só desta nota |
| `o-ink-eink-off` | Mostra as imagens desta nota em cores |

## Personalização com Style Settings

Com o plugin [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) instalado, aparece uma seção **O-Ink** com:

- Cor de destaque, cor do texto e cor de fundo (separadas para claro e escuro)
- Liga/desliga, intensidade e espaçamento dos pontinhos
- Usar a fonte do sistema em vez da Commit Mono
- Numerar os H2 em todas as notas
- Bolinhas em vez de traço nas listas
- Desligar o filtro E-Ink, o flash dos botões e o indicador "online"

Sem o plugin, dá pra mudar qualquer cor com um snippet. Veja a pasta [`snippets/`](snippets/).

## Nota de demonstração

A pasta [`docs/`](docs/) tem uma nota com todos os elementos estilizados. Copie para o seu cofre pra ver o tema completo.

## Desenvolvimento

O código do tema fica em `src/ownaka.css`. O `theme.css` é gerado pelo script, que embute a fonte:

```bash
python3 scripts/build.py                      # gera theme.css
python3 scripts/build.py --vault ~/MeuCofre   # gera e instala no cofre
```

Depois, no Obsidian, use o comando **Recarregar o app sem salvar** pra ver as mudanças.

Sugestões e problemas são bem-vindos nas [issues](https://github.com/ownaka/obsidian-o-ink/issues).

## Créditos

- Fonte [Commit Mono](https://commitmono.com), de Eigil Nikolajsen, sob a SIL Open Font License 1.1.
- Inspirado na comunidade de temas do Obsidian, especialmente no cuidado de temas como o [Primary](https://github.com/primary-theme/obsidian) e o [Minimal](https://github.com/kepano/obsidian-minimal).

## Licença

Código sob licença MIT. A fonte Commit Mono segue a [SIL Open Font License 1.1](assets/fonts/OFL.txt).

---

**English:** O-Ink is a minimal E-Ink style theme for Obsidian, based on [ownaka.net](https://ownaka.net). Subtle dot-grid background, Commit Mono everywhere (bundled), square corners, thin borders and a single green accent. Supports Style Settings, alternate checkboxes, custom callouts (`card`, `terminal`, `online`) and per-note `cssclasses`.

Feito por [João Prado (ownaka)](https://ownaka.net).
