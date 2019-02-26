# Octave


Menu: [Home](README.md) | [bash](bash.md) | [Compilers](compilers.md) | [Elixir](elixir.md) |  [F#](fsharp.ms) | [Go](go.md) | [Haskell](haskell.md) | [OCaml](ocaml.md) | [Octave](octave.md) | [Perl](perl.org) | [Python](python.md) | [R](r.md) | [Rust](rust.md) | [Scala](scala.md)  | [SQL](sql.md)

## Inbox
+ https://www.chemie.fu-berlin.de/chemnet/use/info/octave/octave_toc.html
+ http://orgmode.org/worg/org-contrib/babel/languages/ob-doc-octave-matlab.html

## Misc Commands
```octave
% Comments begin with percent sign: %
PS1('>> ') % Change prompt
pwd % Current directory
cd '/tmp' % Change working directory; Will load .m functions from here
help help
help plot
```

* Language Introduction

** If statement
```octave

```

** For loop
```octave

```

** Simple Function
```octave
% No parameters
% Invoke: hello() or hello
%
function hello()
  printf("Hello\n");

end

% Two parameters
% Invoke: mymax(1,2)
%
function mysum(x,y)
  a = x + y
  printf("Sum:%d\n", a);
end

% Two parameters
% Invoke: mysum(1,2)
%
function a = mysum(x,y)
  a = x + y

end
```

** Load and Save Data
```octave

```

** Plot statement
```octave

```

** Matrices
```octave
A = [1 2; 3 4; 5 6];
B = [1 2 3; 4 5 6];
zeros(1,3) % [0 0 0 0]
```

A = 
|1| 2|
|3|4|
|5|6|
```octave
A = [1 2; 3 4; 5 6];
```

B=
|1|2|3
|4|5|6
```octave
B = [1 2 3; 4 5 6];
```
*** Identity Matrix
```octave
eye(4) % 4x4 identity matrix
```
