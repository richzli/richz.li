fake word cloud

+++

https://github.com/richzli/fake-word-cloud resources/icons/github.svg

---

An animated word cloud made up of not-so-real words.

---

The initial scope of the project was simple: figure out how to generate fake words.

I came up with a simple idea using Markov chains: generate new words by predicting the next letter based on the previous two. So I took to Wikipedia, scraping 5000 pages and collecting words over five letters long, feeding the data into my model.

The results weren't perfect, but the words were pretty good considering the relatively short implementation time.

+++

resources/project/words.png fit-width

---

But what if it were *animated*? I mean, I've always wanted to code a physics engine...

It turned out that the most challenging part of the project was learning how to finagle **OpenGL** through the **Python** bindings. In a bid to fix a pesky bug, I studied practically the entire rendering pipeline, only to discover that the error lay in a type inference issue (thank you [Riley](https://github.com/rileyborgard) for the debugging session).

Lesson learned: next time, use C++.

---

+ resources/project/demo.gif fit-width