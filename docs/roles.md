# Roles Document

## Phase 0 – Team Responsibilities

### Bhavya (Owner + Backend + Leader)
**Main Role:** Build the repository foundation and guide the team.

**Tasks:**
- Create the GitHub repository named `ai-tutoring-system`.
- Add folders: `/backend`, `/frontend`, `/ai_engine`, `/docs`, `/tests`, `/design`, `/deployment`.
- Initialize the FastAPI backend in `/backend/main.py`.
- Add the health-check API (`GET /ping → { "status": "ok" }`).
- Write deployment notes in `/deployment/README-deployment.md` with hosting options.
- Add a placeholder `docker-compose.yml` file.

**Final Output:**  
A well-structured repository with backend setup and deployment notes ready for development.

---

### Chandini (Frontend)
**Main Role:** Setup the user interface and create designs.

**Tasks:**
- Create a React app in `/frontend` using `npm create vite@latest frontend`.
- Add and configure TailwindCSS for styling.
- Display “Hello World” on the page.
- Create design mockups for Signup, Login, and Dashboard in `/design/mockups/`.

**Final Output:**  
A working React app styled with TailwindCSS and saved design mockups.

---

### Dhanushya & Sahithi (AI Team)
**Main Role:** Prepare the logic for skill-level detection.

**Tasks:**
- Write pseudocode in `/ai_engine/adaptive_quiz/diagnostic_logic.ipynb` for classifying students into Beginner, Intermediate, or Advanced levels.
- Create a quiz flowchart in `/design/flowcharts/` showing how quiz answers determine skill levels.

**Final Output:**  
Pseudocode and flowchart ready for implementation.

---

### Sahithi & Kavya (Documentation Team)
**Main Role:** Write clear reference documentation for the team.

**Tasks:**
- Write the Vision Document (`/docs/vision.md`) explaining why the project is built and who it helps.
- Write the Roles Document (`/docs/roles.md`) describing each member’s tasks in all phases.
- Write the Roadmap Document (`/docs/roadmap.md`) with a full 54-day development plan.

**Final Output:**  
Clear and structured documentation that guides the team throughout the project.

---

### Kavya & Dhanushya (Testing Team)
**Main Role:** Setup testing to catch bugs early.

**Tasks:**
- Write backend tests in `/tests/backend_tests/` to check if `/ping` API returns `{ "status": "ok" }`.
- Write frontend tests in `/tests/frontend_tests/` to verify that “Hello World” renders correctly.

**Final Output:**  
Testing framework set up with pytest and jest, and two basic tests passing.

