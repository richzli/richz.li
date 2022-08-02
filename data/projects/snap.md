snap

+++

https://github.com/richzli/snap resources/icons/github.svg
https://richzli.github.io/snap resources/icons/link.svg

---

Disintegrate images for fun!

---

There's a particular Discord emote I really enjoy using (shown on the right). It's got this feeling of sadness and angst that's just so incredibly powerful and soul-touching...

Anyways, I went searching for a tool that would apply a similar effect to my own images, to no avail. So I made one myself.

+++

resources/project/boohooa.gif fit-half-width

---

It's coded in **Javascript** with a little help from **gif.js**, a GIF encoder.

My original implementation was incredibly slow, and it turned out that I was re-loading the image data every frame, which completely destroyed performance. But after a few quick tweaks and parameter tunings, it was good to go.

Not much else to say other than to try it out and enjoy the show!

---

+ resources/project/snap-demo.gif fit-width