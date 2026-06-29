# Todo_List_Django_First

## Branching Strategy
- **Base Branches:** The project maintains two primary branches:
  - `master`: Production-ready, stable code.
  - `develop`: Integration branch for ongoing features.
- **Feature Branches:** Always create a new branch from develop branch for new features/tasks using this naming convention:
  - Pattern: `[YourName]/[TaskID]-[ShortDescription]`
  - Example: `s-bababeyk/0001-user-authentication`

## Pull Request Workflow
1. **Create Draft Pull Request:** Right after branch creation, open a **Draft Pull request** to `develop`.
2. **Work in Progress:** Maintain the "Draft" status until the task is 100% complete.
3. **Request Review:** When finished, mark the Pull Request as **"Ready for Review"** to trigger the final review and merge process.
