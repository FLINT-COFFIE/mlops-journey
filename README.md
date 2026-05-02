# My MLOps Journey
Started: January 8, 2026

# UPDATED ROADMAP
# 🏆 The 2026/27 God-Tier AI & MLOps Roadmap

**Target Identity:** Senior AI/MLOps Architect (Industrial Specialist)  
**Philosophy:** 100% Hands-on. Milestone-Based Mastery. Professional Engineering Standards.

-----

### 🧠 The Daily Algorithmic Gym (Ongoing)

*30–45 minutes every morning. This is your "LeetCode Cardio" to pass the technical interview filter.*

  * **Primary Resource:** [NeetCode 150 Practice Map](https://neetcode.io/practice)
  * **Strategy:** Focus on **Arrays & Hashing**, **Trees**, and **Graphs**. These are the data structures that power complex MLOps pipeline DAGs (Directed Acyclic Graphs).

-----

### Quarter 1: The Containerized Programmer (Months 1–3)

**Objective:** Master Python logic, Linux environments, and the "Holy Trinity" of MLOps: Git, Docker, and SQL.

  * **Interactive Resources:**
      * **Python Logic:** [Helsinki MOOC Python 2026](https://programming-26.mooc.fi/) (Finish Parts 6–14). Focus on Classes, OOP, and File I/O.
      * **Environment Mastery:** [MIT: The Missing Semester](https://missing.csail.mit.edu/). Focus on Shell, Git, and Vim.
      * **The Container:** [Docker Curriculum](https://docker-curriculum.com/). Interactive lab for containerizing Python apps.
      * **Data Ingestion:** [SQLZoo](https://sqlzoo.net/). Interactive SQL playground for complex JOINs and Aggregate functions.
  * **🏗 Q1 Project: The "Safe-Sensor" CLI.** \* Build a Python CLI that reads drilling sensor data (CSV), validates schemas using **Pydantic**, and pushes it into a **Dockerized PostgreSQL** database.
  * **Definition of Done (DoD):** \* The entire pipeline starts with a single command: `docker-compose up`.
      * Code includes unit tests with 90% coverage.

-----

### Quarter 2: Infrastructure & Math for Researchers (Months 4–6)

**Objective:** Master the mathematical foundations for scholarship readiness and the code that automates the cloud.

  * **Interactive Resources:**
      * **The Math Sprint:** [Khan Academy: Linear Algebra](https://www.khanacademy.org/math/linear-algebra) + [3Blue1Brown: Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr).
      * **Infrastructure (IaC):** [Piyush Sachdeva: Terraform for AWS](https://github.com/piyushsachdeva/Terraform-Full-Course-Aws).
      * **Data in Motion:** [Confluent Kafka Hands-on Labs](https://developer.confluent.io/get-started/python/).
  * **🏗 Q2 Project: The "Terraformed" Rig Stream.** \* Use Terraform to provision an AWS VPC and an EC2 instance. Deploy a Kafka broker. Write a Python producer to stream simulated reservoir pressure data.
  * **Definition of Done (DoD):** \* Infrastructure is "disposable"—you can destroy and rebuild it with `terraform destroy` and `terraform apply`.

-----

### Quarter 3: Machine Learning & Orchestration (Months 7–9)

**Objective:** Train "Physics-Informed" models and manage their full lifecycle in a production cluster.

  * **Interactive Resources:**
      * **Core ML:** [DataTalks.Club: ML Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp).
      * **MLOps Lifecycle:** [DataTalks.Club: MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp). Focus on **MLflow** and **Prefect**.
      * **K8s Sandbox:** [Killercoda Kubernetes Interactive](https://killercoda.com/playgrounds).
  * **🏗 Q3 Project: Predictive Maintenance Microservice.** \* Train an XGBoost model on time-series sensor data. Wrap it in **FastAPI**, track experiments with **MLflow**, and deploy it to a local Kubernetes cluster.
  * **Definition of Done (DoD):** \* Automated Data Drift detection: If accuracy drops, a Prefect DAG triggers a retraining job automatically.

-----

### Quarter 4: Agentic Systems & LLMOps (Months 10–12)

**Objective:** Bridge industrial domain expertise with Generative AI to create autonomous diagnostic agents.

  * **Interactive Resources:**
      * **LLM Engineering:** [DataTalks.Club: LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp). Focus on **RAG** and **Vector DBs**.
      * **Local Inference:** [Ollama Documentation](https://ollama.com/). Learn to run and serve models locally for secure, offline industrial sites.
      * **Agents:** [LangGraph Tutorials](https://langchain-ai.github.io/langgraph/).
  * **🏗 Q4 Project: The "Digital Driller" AI Agent.** \* Build an autonomous agent that monitors Kafka streams. When an anomaly is detected, it queries a Vector DB containing equipment manuals to provide a root-cause fix via Slack.
  * **Definition of Done (DoD):** \* The system provides a "Post-Mortem" report for every failure.
      * Handles 1,000+ events/sec with 99.9% uptime.

-----


## TODO:
### PHASE 1
- [x] Complete Helsinki Python MOOC
- [x] Finish MIT Missing Semester
- [x] Complete SQL Zoo
- [ ] Complete Docker Curriculum
- Complete google career certs
- [x] Google python for data analysis



