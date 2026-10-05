# TrueCareer – Career Guidance Platform for Vietnamese High School Students

TrueCareer helps Vietnamese high school students choose a suitable major and career path. Students take a career assessment, get matched with experts who fit their profile, and talk to them through a 1-on-1 video call.

**Project type:** Academic group project
**My role:** Business Analyst. I worked on the problem analysis, customer journey, user stories (business rules, acceptance criteria, states, permissions) and the UI prototype. I also built a small data prototype to test the recommendation logic.

| | Link |
|---|---|
| UI prototype (Axure) | https://fjsshr.axshare.com/?id=1sxs4v |
| User story sample | [docs/user-story-payment-en.md](docs/user-story-payment-en.md) |
| Presentation | [Presentation/TrueCareer_presentation.pdf](Presentation/TrueCareer_presentation.pdf) |
| Data dashboard (Streamlit) | [Live demo](https://truecareer-career-guidance-system-j2ayh9kkh4s2pjjeufejfw.streamlit.app/) |

---

## 1. The problem

Grade 11–12 students in Vietnam have to pick a university major, but most of them:

- don't know which major fits their strengths and interests,
- have to collect information about majors from many scattered sources,
- can't easily see which jobs will be in demand in the next 3–5 years,
- have very little time on top of school and exam preparation.

On the other side, there are experienced professionals (5+ years in their field) who can give real advice, but students have no simple way to reach them. Students in our research said they would prefer coaching from a mentor over generic advice.

## 2. Product goals

- Help students make a more informed choice of major, based on an assessment rather than guesswork.
- Connect students with the right expert quickly, through a video call.
- **Revenue model:** students pay per call package; advertising is a secondary source.
- **Vision:** become a leading career guidance platform in Vietnam that makes good use of new technology.

## 3. Customer journey

The full journey is on slide 12 of the presentation. In short:

```
Log in → Take the assessment → See results → Pick a recommended expert
→ Choose a package & pay → Waiting room → Video call (up to 60 min)
→ Rate the expert → Receive written feedback within 24h
```

Each step in the presentation lists the screen elements and the call-to-action buttons, which were then used to design the prototype.

## 4. Business analysis documents

| Document | What's inside |
|---|---|
| [User story: buy a call package](docs/user-story-payment-en.md) | Business rules, order states, permissions, acceptance criteria (Given/When/Then), edge cases, prototype gaps found, open questions |
| [User story (Vietnamese)](docs/user-story-payment-vi.md) | Same content in Vietnamese |
| [Data prototype](docs/data-prototype.md) | Dataset, clustering, recommendation and mentor matching details |

While writing the user story, I reviewed the prototype screen by screen and found a few gaps (for example, the payment screen showing the wrong amount for the selected package). These are listed in the document.

## 5. UI prototype

The Axure prototype has 19 screens covering the main flow: welcome page, assessment (3 pages), recommended experts, error screens (no expert online, expert account issue, server error), package selection, payment, waiting room, video call, rating and thank-you pages.

👉 https://fjsshr.axshare.com/?id=1sxs4v

## 6. Data prototype: recommendation logic

To check that the "recommended experts" step is realistic, I built a small data prototype in Python.

- **Data:** 800 synthetic student profiles in a Vietnamese context (admission subject groups such as A00, A01, D01…), 22 assessment features. The data is synthetic and for demonstration only.
- **Clustering:** K-Means groups students into 6 orientation groups (Tech-Analytical, Business-Strategic, Finance-Oriented, Social-Communicative, Creative-Design, Balanced Explorer).
- **Recommendation:** rule-based mapping from each group to suitable majors, courses, mentor types and career paths.
- **Mentor matching:** students are matched to mentors by mentor type, and a mentor can see all students who match their field.
- **Dashboard:** a Streamlit app shows the clusters, recommended majors and mentor matching.

This part is exploratory. It is not a validated prediction model.

👉 Full technical details: [docs/data-prototype.md](docs/data-prototype.md)

## 7. Project structure

```
truecareer-career-guidance-system/
├── docs/            # BA documents (user stories)
├── Presentation/    # Final presentation (PDF, PPTX)
├── prototype/       # Axure prototype link
├── data/            # Synthetic dataset and outputs
├── src/             # Data processing, clustering, recommendation scripts
├── dashboard/       # Streamlit app
└── screenshots/
```

## 8. How to run the data prototype

```bash
pip install -r requirements.txt
python src/data_preprocessing.py   # validate the dataset
python src/clustering.py           # run K-Means
python src/recommendation.py       # build recommendations
streamlit run dashboard/app.py     # open the dashboard
```

## 9. What I'd do next

- Write user stories for the rest of the journey (assessment, waiting room, rating, refunds).
- Get answers to the open questions in the user story from the business side.
- Test the assessment with real students and compare results with the synthetic data.

---

*TrueCareer is a prototype. It does not replace professional counseling or official university admission guidance.*
