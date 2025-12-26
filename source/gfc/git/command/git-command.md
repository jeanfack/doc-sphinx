:hide-toc:

# Git Command

::::{grid}
:::{grid-item-card} Question
:::

:::{grid-item-card} Réponse
:::

:::{grid-item-card} Explication
:::

:::{grid-item-card} Source
:::
::::

::::{grid}
:::{grid-item-card}
Chris Griffin just pushed his latest changes to GitHub but realizes that one of the commits contains a critical error.\
He wants to undo that specific commit.\
 What should Chris do to undo the mistaken commit while keeping the commit history intact ?
:::

:::{grid-item-card}
`git revert <SHA>`
:::

:::{grid-item-card}
{bdg-primary}`NOTES`

Commit sans push => `git commit --amend` \
Commit avec push => `git revert <SHA>`
:::

:::{grid-item-card}
* [https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/#undo-a-public-change](https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/#undo-a-public-change)
:::
::::

::::{grid}
:::{grid-item-card}
What is the process for deleting a file that was added in the most recent unpushed commit ?
:::

:::{grid-item-card}
`git rm --cached <FILE-NAME>`\
`git commit --amend -CHEAD`
:::

:::{grid-item-card}
:::

:::{grid-item-card}
* [https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---cached](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---cached)
* [https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend)
:::
::::

::::{grid}
:::{grid-item-card}
What tool can be used to remove files from a repository's history if they were added in earlier commits ?
:::

:::{grid-item-card}
BFG Repo-Cleaner or `git filter-repo` command.
:::

:::{grid-item-card}
:::

:::{grid-item-card}
* [https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github?platform=windows#removing-a-file-that-was-added-in-an-earlier-commit](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github?platform=windows#removing-a-file-that-was-added-in-an-earlier-commit)
* [https://git-scm.com/docs/git-filter-branch](https://git-scm.com/docs/git-filter-branch)
:::
::::

::::{grid}
:::{grid-item-card}
How can you create a new branch in Git using the terminal ?
:::

:::{grid-item-card}
`git checkout -b <branch-name>`
:::

:::{grid-item-card}
:::

:::{grid-item-card}
:::
::::

::::{grid}
:::{grid-item-card}
Peter Griffin wants to ignore a file that is already checked into his Git repository.\
What command should he use to untrack the file before adding a rule to ignore it ?
:::

:::{grid-item-card}
`git rm --cached <FILENAME>`
:::

:::{grid-item-card}
:::

:::{grid-item-card}
:::
::::

::::{grid}
:::{grid-item-card}
What does git status do in Git ?
:::

:::{grid-item-card}
Shows the state of the working tree and staging area.
:::

:::{grid-item-card}
:::

:::{grid-item-card}
:::
::::

::::{grid}
:::{grid-item-card}
Which type of commits are excluded from the Commit graph ?
:::

:::{grid-item-card}
Merge commits.
:::

:::{grid-item-card}
:::

:::{grid-item-card}
:::
::::

::::{grid}
:::{grid-item-card}
Peter wants to rename his local branch named `feature-1` to `new-feature` on the remote repository named `origin`.\
Which Git command should he use?
:::

:::{grid-item-card}
`git push origin feature-1:new-feature`
:::

:::{grid-item-card}
:::

:::{grid-item-card}
* [https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#renaming-branches](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#renaming-branches)
:::
::::
