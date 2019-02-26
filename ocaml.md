# OCaml

Menu: [Home](README.md) | [bash](bash.md) | [Compilers](compilers.md) | [Elixir](elixir.md) |  [F#](fsharp.ms) | [Go](go.md) | [Haskell](haskell.md) | [OCaml](ocaml.md) | [Octave](octave.md) | [Perl](perl.org) | [Python](python.md) | [R](r.md) | [Rust](rust.md) | [Scala](scala.md)  | [SQL](sql.md)

## The Short List 
+ [[https://try.ocamlpro.com][Web REPL]]
+ [[http://www.csc.villanova.edu/~dmatusze/resources/ocaml/ocaml.html][A Concise Introduction to Objective Caml]]
+ [[https://github.com/rizo/awesome-ocaml][Awesome OCaml: A curated collection of awesome OCaml tools, frameworks, libraries and articles]]
+ [[https://realworldocaml.org][Real World OCaml]]
+ [[https://www.youtube.com/playlist?list=PLea0WJq13cnCef-3KSU3qWFge9OGUlKx1][33 Learning oCaml videos]]
+ [[https://ocaml.org][Official OCaml Site]]

## Inbox
+ [[https://www.cl.cam.ac.uk/~lp15/MLbook/pub-details.html][ML for the Working Programmer, 2nd Edition]]
+ [[https://ocaml.org/learn/tutorials/99problems.html][99 Problems (solved) in OCaml]]
+ https://www.reddit.com/r/ocaml/comments/49zzg6/oml_machine_learning_in_ocaml_composeconf_talk
+ http://roscidus.com/blog/blog/2014/06/06/python-to-ocaml-retrospective
 - http://roscidus.com/blog/blog/2014/02/13/ocaml-what-you-gain/
   + https://news.ycombinator.com/item?id=7234855
+ [[https://www.youtube.com/playlist?list=PLea0WJq13cnA1622rtoEhd911spMDRvWh][OCaml Data Structures - YouTube]]
+ [[http://github.com/the-lambda-church/merlin][Merlin: Context sensitive completion for OCaml in Vim and Emacs]]
+ [[http://www.lexicallyscoped.com/2015/06/06/intro-to-ocaml.html][A brief introduction to OCaml]]
 - http://news.ycombinator.com/item?id=9712225
+ http://www.reddit.com/r/ocaml/comments/39pxqg/what_are_the_most_common_bugs_in_ocamlfunctional
+ http://www2.lib.uchicago.edu/keith/ocaml-class/home.html
+ http://www2.lib.uchicago.edu/keith/ocaml-class/userdefined.html
+ https://ocaml.org/learn/tutorials/ocaml_and_the_web.html
+ [[http://blog.nullspace.io/beginners-guide-to-ocaml-beginners-guides.html][Beginner's guide to OCaml beginner's guides.]]
+ [[http://fsharpforfunandprofit.com][F# for fun and profit]]
+ http://www.infoq.com/presentations/jane-street-caml-ocaml
+ [[http://tech.esper.com/2014/07/15/why-we-use-ocaml/][Why We Use OCaml]]
+ https://www.reddit.com/r/ocaml/comments/3ifwe9/what_are_ocamlers_critiques_of_haskell
+ [[https://spyder.wordpress.com/2014/03/16/why-ocaml-why-now][Why OCaml, why now?]]
 - https://news.ycombinator.com/item?id=9049467
+ [[http://hyegar.com/2015/10/20/so-youre-learning-ocaml/index.html][So you're learning OCaml]]
 - http://news.ycombinator.com/item?id=10417521
+ https://www.reddit.com/r/ocaml/comments/4b2oot/dealing_with_strings_in_ocaml_for_a_beginner/
+ https://michipili.github.io/essay/2016/04/11/ocaml-on-operations.html
+ https://github.com/inhabitedtype/ocaml-aws - Generated OCaml bindings for Amazon Web Services

## F#
+ [[http://jj09.net/getting-started-with-fsharp/][Getting started with F#]]
+ https://www.reddit.com/r/fsharp/comments/4ggl1c/getting_started_with_f_via_the_linux_command_line/

### F# Differences
+ http://stackoverflow.com/questions/179492/f-changes-to-ocaml
+ http://web.archive.org/web/20080410181630/http://research.microsoft.com/fsharp/manual/ml-compat.aspx

## Libraries
+ https://github.com/hammerlab/oml
 - http://www.hammerlab.org/2015/08/11/introducing-oml-a-small-ocaml-library-for-numerical-computing/
 - https://www.youtube.com/watch?v=czZ18YtZlaw
  + Slides: http://rleonid.github.io/slides/oml/compose2016

```ocaml

(* Addition *)

1 + 1

```


* Variables

```ocaml 
let pi = 3.1416;;

let () = print_endline "Hello, World!"
``` 


```ocaml 
toplevel

let average a b =
  (a +. b) /. 2.0;;
average;;

let rec // recursion

my_ref := 100;
``` 

* Functions

A function always has exactly one parameter, and returns one result.
```ocaml 
(* In this case, the one argument is a tuple, and the one result is a tuple. *)
let swap (x, y) = (y, x);;
``` 


```ocaml 
let sum (x, y) = x + y;;
sum(3, 5);;
let max (x, y) = if x > y then x else y;;
max(9, 5)

let hi () =
  print_string "hello\n";;
```


```ocaml
(*
Here, the one argument is the unit, (), which is a value--it is not syntax to indicate an empty parameter list. Similarly, the unit is returned as a result.
*)
print_newline ();;
``` 

## Include Files
```ocaml 
use "myFile.sml"
``` 
The most common functions are in the "Pervasives module," which means you don't have to do anything special to use them

```ocaml 
open String;; 
length "hello";;
``` 

Identifiers must begin with a lowercase letter or underscore, and may contain letters, digits, underscores, and single quotes.

## Lists
[2; 3; 5; 7]
Only the :: operator (LISP cons) and @ operator (list concatenation) can be used without opening the List module or prefixing the function name with List. .

### List Operations

```ocaml 
5 :: [6; 7]
[5] @ [6; 7]
List.nth [3; 5; 7] 2
List.rev [1; 2; 3]
``` 

## Tuples
```ocaml 
(5, "hello", ~16)
```

### Tuple Operations
```ocaml
open Char;;
Char.uppercase 'a'
``` 

## Exceptions

The name of an exception must begin with a capital letter. 

You can declare new types of exceptions, with or without a parameter

## Comments
```ocaml
(* One line *)
(* 
 * Multi-line
 *)

(* 
 * (* Embedded *)
 *)

```

## opam Package Manager
+ http://opam.ocaml.org/doc/Install.html
 - brew install opam
```ocaml

```

```ocaml

```

```ocaml

```

```ocaml

```

```ocaml

```
