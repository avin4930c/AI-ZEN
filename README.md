  # AI ZEN

AI ZEN is a full stack application that utilizes natural language to summarize PDF content and query an SQLite database. Built with Next.js and FastAPI, it offers users an interactive AI experience to extract information from both PDFs and database entries.



  ## Technologies Used

  - **Frontend:**
    - [Next.js](https://nextjs.org/): React framework for server-side rendering and static site generation.
    - [Tailwind CSS](https://tailwindcss.com/): Utility-first CSS framework for styling.

  - **Backend:**
    - [FastAPI](https://fastapi.tiangolo.com/): Modern, fast (high-performance) web framework for building APIs with Python.
    - [SQLite](https://www.sqlite.org/): Lightweight database engine.

  ## Basic Flow

  ![FlowDiagram](/images/AI%20Chatbot.drawio.png)

  ### Chat Interface
  ![Image1](/images/pdf_chatbot.png)
  ![Image2](/images/db_chatbot.png)

  ## Getting Started

  ### Prerequisites

  - Node.js (version 14 or later)
  - Python (version 3.8 or later)
  - Virtualenv (for Python dependencies)

  ### Installation

1. **Clone the repository:**

    Open a terminal and run:

    ```bash
    git clone git@github.com:avin4930c/AI-ZEN.git
    cd ai-zen
    ```

2. **Setup the frontend:**

    Navigate to the `frontend` directory:

    ```bash
    cd frontend
    ```

    Install the frontend dependencies:

    ```bash
    npm install
    ```

    Start the Next.js development server:

    ```bash
    npm run dev
    ```

3. **Setup the backend:**

    Open a new terminal and navigate to the `backend` directory:

    ```bash
    cd backend
    ```

    Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

    Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    **Note:** A `.env` file containing an API key for Google Gemini 1.5 Flash is included temporarily to help new users run the project.

    Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```
