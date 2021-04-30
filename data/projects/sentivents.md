sentivents

+++

https://github.com/cyu0003/sentivents resources/icons/github.svg
https://github.com/richzli/sentivents-server resources/icons/github.svg

---

Mood tracker app leveraging a sentiment analysis ML model.

---

This is a **React Native** mobile application with a **Python** backend.

This project was created for the Boilermake VIII hackathon with a group of three others. We wanted to utilize MIT's **DeepMoji**, an interesting machine learning model that recognizes emotion in text by using emojis.

A slight problem was that this model only had Python implementations, so including it directly in the app was infeasable. We ended up deciding separating this project into two parts, the app, and a simple HTTP server to service the requests.

+++

resources/project/sentivents-5.PNG fit-half-width
resources/project/sentivents-2.PNG fit-half-width

---

Given my expertise in Python, I was given the task of implementing the backend. One problem I ended up encountering was that the provided DeepMoji implementation used an old version of **PyTorch**, causing it to break completely. It took a surprising amount of time to find references online and isolate the problem.

After I fixed that, I set up a simple API with Python's **http.server** on a Google Cloud Compute instance. This allowed the rest of the team to start implementing functionality in the app.

+++

resources/project/sentivents-3.PNG fit-half-width
resources/project/sentivents-4.PNG fit-half-width