<!--[[TOC]]-->

# Example

## Breakline

Cette premère phrase est sans
breakline.

Cette deuxième phrase contient un double espace  
qui fait une break line.

## Emphasis<p>

I just love **bold text**.  
I just love *italic text*.

## Citation
> Rendez les choses aussi simples que possible, mais pas plus simples.  
*Albert Einstein*

## Admodition

:::{note}
    Here is *admonition* directive using MyST specification.
:::

!!! danger "danger"
    Here is *admonition* directive using mkdocs-material specification.


>:::: tips
>tips alert

>:::: success
>success alert

>:::: warning
>warning alert

>:::: danger
>danger alert

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.

## List

* introduction
* theme
  * argument 1
  * argument 2
  * argument 3
    * arg3.1
    * arg3.2
* antithese
* synthese
* conclusion

1. cas1
1. cas2
    1. ex2.1
    1. ex2.2
1. cas3

## Math

La somme des n premiers entiers naturels est
$\sum_{i=1}^n = \frac{n(n+1)}{2}$

## Image

Example de graph avec dot de graphviz  
![example](../_include/examples/example1/img/cluster.svg "example")

## Link
[markdown basic syntax](https://www.markdownguide.org/basic-syntax/)


## code

exemple d'usage de la commande ```mkdir``` :

```bat
%SYSTEMDRIVE%
cd %USERPROFILE%
dir dummy
mkdir dummy
dir dummy
rmdir dummy
dir dummy
```


```console
Microsoft Windows [version 10.0.19045.5247]
(c) Microsoft Corporation. Tous droits réservés.

C:\Users\jeanf>%SYSTEMDRIVE%

C:\Users\jeanf>cd %USERPROFILE%

C:\Users\jeanf>dir dummy
 Le volume dans le lecteur C s’appelle Windows
 Le numéro de série du volume est A0ED-B83C

 Répertoire de C:\Users\jeanf\dummy

28/07/2024  11:31    <DIR>          .
28/07/2024  11:31    <DIR>          ..
               0 fichier(s)                0 octets
               2 Rép(s)  530 155 786 240 octets libres

C:\Users\jeanf>mkdir dummy
Un sous-répertoire ou un fichier dummy existe déjà.

C:\Users\jeanf>dir dummy
 Le volume dans le lecteur C s’appelle Windows
 Le numéro de série du volume est A0ED-B83C

 Répertoire de C:\Users\jeanf\dummy

28/07/2024  11:31    <DIR>          .
28/07/2024  11:31    <DIR>          ..
               0 fichier(s)                0 octets
               2 Rép(s)  530 155 786 240 octets libres

C:\Users\jeanf>rmdir dummy
Le répertoire n’est pas vide.

C:\Users\jeanf>dir dummy
 Le volume dans le lecteur C s’appelle Windows
 Le numéro de série du volume est A0ED-B83C

 Répertoire de C:\Users\jeanf\dummy

28/07/2024  11:31    <DIR>          .
28/07/2024  11:31    <DIR>          ..
               0 fichier(s)                0 octets
               2 Rép(s)  530 155 786 240 octets libres

C:\Users\jeanf>
```

## Mermaid

```{mermaid}
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

## Graphviz

```{graphviz} ../_include/examples/example1/code/dot/example.dot
```

<!--
```{eval-rst}

.. graphviz::

   digraph foo {
      A -> B
   }
```
-->
