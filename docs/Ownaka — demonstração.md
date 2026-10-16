---
tags:
  - ownaka
  - demo
status: online
cssclasses:
  - ownaka-numbered
---

Esta nota mostra tudo que o tema **Ownaka** estiliza. Copie para o seu cofre e abra no modo de leitura e no modo de edição.

## Títulos

# Título H1
## Título H2
### Título H3 — com o indicador do site
#### Título H4 vira rótulo
##### Título H5
###### Título H6

## Texto

Texto normal em Commit Mono. **Negrito em branco**, *itálico em bege*, ==marca-texto em verde==, ~~riscado~~ e `código inline`.

Um [[link interno]], um [[nota que não existe]] e um [link externo](https://ownaka.net).

Uma frase com nota de rodapé.[^1]

[^1]: As notas de rodapé ficam discretas.

#tag #self-hosting #linux

## Listas

- Item com o traço do site
- Outro item
	- Subitem
	- Mais um

1. Primeiro
2. Segundo
3. Terceiro

## Tarefas

- [ ] A fazer
- [x] Feita
- [/] Em andamento
- [-] Cancelada
- [>] Adiada
- [!] Importante
- [?] Dúvida
- [*] Ideia

## Citação

> Entender como algo funciona por dentro é a melhor parte. Explicar pra alguém é a segunda.

## Callouts

> [!note] Nota
> Os callouts viram cards com rótulo entre colchetes.

> [!tip] Dica
> Tudo na paleta do tema, sem cores gritando.

> [!warning] Atenção
> Avisos ficam em âmbar.

> [!card] Card
> Um card limpo, igual aos do site.

> [!terminal] Terminal
> docker compose up -d
> sudo systemctl restart jellyfin

> [!online] Online
> O selo verde de status, como no card de identidade.

## Código

```bash
# backup 3-2-1 com restic
restic -r /mnt/backup backup ~/docs --tag diario
restic forget --keep-daily 7 --keep-weekly 4 --prune
```

## Tabela

| Serviço  | Função                 | Porta |
| -------- | ---------------------- | ----: |
| Jellyfin | Streaming privado      |  8096 |
| Pi-hole  | Filtro de anúncios     |    53 |
| Kavita   | Biblioteca de livros   |  5000 |

---

Fim da demonstração.
