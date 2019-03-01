# Go

Menu: [Home](README.md) | [bash](bash.md) | [Compilers](compilers.md) | [Elixir](elixir.md) |  [F#](fsharp.md) | [Go](go.md) | [Haskell](haskell.md) | [OCaml](ocaml.md) | [Octave](octave.md) | [Perl](perl.md) | [Python](python.md) | [R](r.md) | [Rust](rust.md) | [Scala](scala.md)  | [SQL](sql.md)

## The Short List
+ [Awesome Go](https://github.com/avelino/awesome-go)
+ [Go in 5 Minutes](https://github.com/arschles/go-in-5-minutes)
- http://www.goin5minutes.com/screencasts/index.html
+ [Go by Example](https://gobyexample.com)

## Editor/IDE Support

+ [Visual Studio Code Plugin](https://github.com/Microsoft/vscode-go)
+ https://rootpd.com/2016/02/04/setting-up-intellij-idea-for-your-first-golang-project
+ http://hadihariri.com/2015/09/30/setting-up-go-on-intellij
+ http://marcio.io/2015/07/supercharging-atom-editor-for-go-development

## Web

+ [RSS Collector in Ruby and Go](http://rrmartins.herokuapp.com/blog/2016/05/12/rss-collector-in-ruby-and-go/)
+ [Building Web Apps in Go](https://astaxie.gitbooks.io/build-web-application-with-golang/content/en/preface.html)
+ [Curl to Go](https://mholt.github.io/curl-to-go)
+ http://java.dzone.com/articles/exploring-go-template-engine
+ http://news.ycombinator.com/item?id=9439041 - A minimal blog engine written in Go, compatible with Ghost themes
+ http://getting-started.md/guides/3-go-martini
+ [yquotes - Yahoo Stock Quotes in Go](http://github.com/doneland/yquotes)
- http://news.ycombinator.com/item?id=9374373
+ http://nicolasmerouze.com/build-web-framework-golang/
+ [Build a Web Crawler in Go](http://jdanger.com/build-a-web-crawler-in-go.html)
+ http://soryy.com/blog/2014/not-another-go-net-http-tutorial
+ [How To Deploy a Go Web Application with Docker](https://semaphoreci.com/community/tutorials/how-to-deploy-a-go-web-application-with-docker)

## Inbox
+ [Visualizing Concurrency in Go](http://divan.github.io/posts/go_concurrency_visualize/)
- https://news.ycombinator.com/item?id=14224118
+ [Time in Go: A primer](https://machiel.me/post/time-in-go-a-primer/)
+ [Go tooling essentials](http://golang.rakyll.org/go-tool-flags/)
+ http://news.ycombinator.com/item?id=10395694 - Statistics package
+ [An introduction to LLVM in Go](https://blog.felixangell.com/an-introduction-to-llvm-in-go/)
+ http://blog.ksred.me/post/learning-golang-stock-notifier
+ http://github.com/m3ng9i/ran
+ http://news.ycombinator.com/item?id=10286852 - A Lisp Compiler and Environment in Go
+ http://devdungeon.com/content/working-files-go
+ http://news.ycombinator.com/item?id=9829025 - Go-datastructures
+ http://news.ycombinator.com/item?id=9751121 - Resources to learn Go(lang)
+ [Tetris in Go](http://www.jjinux.com/2015/05/tetris-written-in-go.html)
- http://news.ycombinator.com/item?id=9607651
+ http://blog.golang.org/normalization
+ http://news.ycombinator.com/item?id=9058872 - calc
+ [Show HN: I rendered the Go gopher using Go](http://news.ycombinator.com/item?id=9009554)
+ http://www.wadewegner.com/2014/12/4-simple-steps-to-run-go-language-in-azure-websites/
+ http://weblogs.java.net/blog/manningpubs/archive/2014/11/19/go-practical-introduction-slices
+ [gorename: easy refactoring tool for Golang](https://texlution.com/post/gorename/)
- http://news.ycombinator.com/item?id=8643461
+ [Futures in Go](http://blog.charmes.net/2014/11/futures-in-go.html)
-  http://news.ycombinator.com/item?id=8645394
+ [When in Go, do as Gophers do](http://talks.golang.org/2014/readability.slide#1)
+ http://avtok.com/2014/11/05/interface-upgrades.html
+ [Go Wiki - A simple HTTP server rendering Markdown styled documents http://renstrom.github.io/go-wiki](http://github.com/renstrom/go-wiki)
+ [Go Koans](http://github.com/cdarwin/go-koans)

## Setup

```sh
export GOPATH=$HOME

go get github.com/mattn/go-sqlite3
go get github.com/gorilla/mux
go get github.com/gorilla/pat
go get github.com/go-sql-driver/mysql; # http://github.com/go-sql-driver/mysql

---

golang-book.com
gpm
godep
goop
```


## Tutorials

http://www.digitalocean.com/company/blog/get-your-development-team-started-with-go/

	http://micknelson.wordpress.com/2012/11/14/a-tour-of-go-the-web-crawler-exercise/
	http://www.golang-book.com/
	http://play.golang.org/
  http://gobyexample.com/

  http://github.com/jimmahoney/golang-webserver/blob/master/webserver.go
  http://github.com/TeamTwilightSparkle/webserver
  http://blog.smartbear.com/web-development/how-to-build-a-web-service-in-5-minutes-with-go/

http://www.jeffreybolle.com/blog/create-a-web-app-using-google-go
http://github.com/jeffreybolle/rebuilder

  http://codegangsta.gitbooks.io/building-web-apps-with-go/

    http://eager.io/blog/go-and-json/|Go and JSON

  http://news.ycombinator.com/item?id=8413341

http://soryy.com/blog/2014/not-another-go-net-http-tutorial/

http://github.com/apsdehal/Konsoole
http://news.ycombinator.com/item?id=8440755

http://github.com/sosedoff/pgweb/


go test -cover 
eg example-based factoring

gorename
   http://godoc.org/code.google.com/p/go.tools/cmd/gorename
   http://github.com/smartystreets/sublime-gorename

go/types 

goimports
    http://blog.campoy.cat/2013/12/integrating-goimports-with-gosublime-on.html
go oracle 
go tool pprof in 1.4

llgo 

http://github.com/smartystreets/mafsa

### Emacs and Go

http://tleyden.github.io/blog/2014/05/22/configure-emacs-as-a-go-editor-from-scratch/
http://github.com/dominikh/go-mode.el
http://medium.com/@olebedev/live-code-reloading-for-golang-web-projects-in-19-lines-8b2e8777b1ea
http://news.ycombinator.com/item?id=8772636

+ http://news.ycombinator.com/item?id=8791935
+ http://news.ycombinator.com/item?id=8797590

### Simple Crawler
```
package main

import (
	// "fmt"
	// "html/template"
	"fmt"
	"io/ioutil"
	"net/http"
	// "strconv"
	// "strings"
	// "time"
)

func crawl() {
	var url = "http://www.h4labs.com"

	resp, err := http.Get(url)
	if err != nil {
		// handle error
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	fmt.Print(string(body))
}

func main() {
	crawl()
}
```
