# Advent of Code – Préparation 2026

Entraînement en Python en vue de l'Advent of Code 2026.

## Objectifs

- Me préparer à l'Advent of Code 2026, objectif vitesse pour la 1ere fois
- Renforcer mes compétences en Python
- Écrire 100 % du code à la main, sans génération ni référence IA lors de la première résolution

## Workflow

1. Télécharger l'input du jour avec le script `fetch`
2. Copier l'exemple de l'énoncé dans `example_part{x}.txt`
3. Ouvrir le template de la journée et importer la toolbox
4. Lancer le programme via l'entrée standard (voir ci-dessous)

## Après chaque résolution

- Améliorer le workflow, le template et la toolbox
- Analyser ce qui a fonctionné et ce qui n'a pas fonctionné
- Lister les points d'amélioration et les leçons à retenir
- Refactoriser la solution dans un second fichier

## Outils

| Outil | Rôle |
|---|---|
| `fetch` | Télécharge l'input du jour |
| Template | Fournit la structure de départ d'une journée |
| Toolbox | Regroupe les helpers réutilisables, enrichis au fil des jours |

### Alias

| Alias | Commande équivalente |
|---|---|
| `aot` | `python dayXX.py < example_part1.txt` |
| `aoc` | `python dayXX.py < input.txt` |

## Entrée standard et debugging

Les solutions lisent leur input avec `fileinput.input()` plutôt qu'avec `sys.stdin.read()` :

```python
with fileinput.input() as lines:
    data: str = "".join(lines)
```

Avec `< fichier`, l'entrée standard est occupée par le fichier, alors que les shells interactifs en ont besoin pour lire le clavier. C'est le cas d'`ipdb`, que j'utilise pour le debugging, et d'IPython, que j'utilise pour certains tests. Je leur passe donc l'input en argument :

```bash
ipdb3 dayXX.py example_part1.txt
```

```python
# Dans IPython
%run dayXX.py example_part1.txt
```

Sans argument, `fileinput` lit l'entrée standard : les alias fonctionnent donc toujours. Si une solution a besoin de ses propres arguments, il faudra préciser les fichiers à lire avec `files=`.

## Données

Les inputs et les exemples ne sont pas versionnés, conformément à la demande d'Advent of Code.
