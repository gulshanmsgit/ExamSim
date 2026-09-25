# ExamSim

Timed MCQ mock exams with negative marking, organised into subjects and topics.
Everything is a single `index.html`; data is stored in your own free Firebase project.

## Features

- Upload questions as JSON, plain text or PDF (or generate them with the built-in AI prompts)
- Library: subjects → topics → question sets, with default exam settings per subject
- Timed exams with option E ("I choose not to answer", no penalty) and configurable penalties (`1/4`, `1/3`, `25%` or a fixed number)
- Every attempt is saved: score trend, per-question history and "Practise mistakes"
- Same library on phone and laptop via a private sync code (no login)

## Setup (about 5 minutes)

### 1. Create a Firebase project
1. Open <https://console.firebase.google.com> and click **Create a project**. Google Analytics is not needed.

### 2. Create the database
1. In the left menu: **Build → Firestore Database → Create database**.
2. Choose a location close to you (e.g. `asia-south1` for Mumbai). This cannot be changed later.
3. Choose **Start in production mode**.

### 3. Publish the security rules
1. In Firestore, open the **Rules** tab.
2. Replace everything with the contents of [`firestore.rules`](firestore.rules) and click **Publish**.

### 4. Get the web config
1. Click the ⚙ gear → **Project settings** → scroll to **Your apps** → click the **Web** icon (`</>`).
2. Give it any nickname, leave "Firebase Hosting" unticked, click **Register app**.
3. Copy the `firebaseConfig` object it shows.

### 5. Paste the config into `index.html`
Near the top of the `<script>`, replace

```js
const FIREBASE_CONFIG = null;
```

with your values:

```js
const FIREBASE_CONFIG = {
  apiKey: "AIza...",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abc123"
};
```

These values are public by design (every Firebase web app ships them to the browser). The rules from step 3 are what protect the data.

### 6. Host on GitHub Pages
1. Push this repository to GitHub (public repository).
2. Repository **Settings → Pages → Build and deployment → Deploy from a branch → `main` / root → Save**.
3. After a minute your app is live at `https://<username>.github.io/<repo>/`.

You can also just double-click `index.html`; it needs an internet connection to reach Firebase.

## Sync codes (how data is kept private without a login)

When you click **Create my library**, the app generates a random sync code such as
`k7mq-x2vd-…`. Your data is stored under that code. Anyone who has the code can open
and edit that library, and nobody can list or discover other codes.

- Save your code somewhere safe (a note, or an email to yourself).
- To use the same library on another device, open the app there and enter the code,
  or use the link from the **☁ Synced** button (it contains the code).
- Don't post your code or link publicly.

## Free-tier limits (Firebase Spark plan)

1 GiB stored, 50,000 document reads and 20,000 writes per day. One exam is a handful of
reads and one write, so personal use or a small study group stays far below this.
A single question set can be up to about 1 MB (roughly 1,500–2,000 questions); split larger files.
