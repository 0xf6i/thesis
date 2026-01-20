# Thesis Ideas: DNS-Based SaaS Dependency Analysis

This document outlines four potential thesis ideas focused on quantifying and analyzing supply chain risks through DNS artifacts.

---

## Idea 1: The Risk Modeling Thesis
**Title:** Quantifying Supply Chain Risk: A Weighted Scoring Model for SaaS Dependencies using DNS TXT and SPF Records

- **Focus:** Targets Goal 2 and 3 (Risk scoring and levels). Focuses on designing and validating the formula for the risk score.
- **Research Question:** How can DNS-based artifacts be effectively weighted to calculate a quantifiable risk score for 3rd party SaaS dependencies?

### Methodology
*   **Literature Review:** Research existing risk scoring standards (CVSS, DREAD) and apply them to supply chain nodes.
*   **Artifact Creation:** Develop the scoring algorithm (e.g., Is a direct SPF include higher risk than a verification TXT record? Does a chain of 3 redirects dilute the risk?).
*   **Validation:** Run your tool against the "Tranco Top 10,000" domains.
*   **Analysis:** Analyze the results (e.g., "We found that 40% of top Swedish companies use a 3rd party with a 'Critical' risk rating.").

**Why BTH will like it:** It moves beyond coding into Metric Design and Statistical Analysis.

---

## Idea 2: The Graph Theory Thesis
**Title:** Recursive Dependency Mapping: Analyzing the 'Degrees of Separation' in Digital Supply Chains via DNS Analysis

- **Focus:** Targets Goal 2 (Infinite cycle/recursive lookups). A pure computer science/security analysis of the "network" of trust.
- **Research Question:** To what extent can recursive DNS analysis reveal hidden "fourth-party" risks that direct analysis misses?

### Methodology
*   **Tool Development:** Build the recursive feature of your tool (limiting it to N levels to prevent loops).
*   **Data Collection:** Scan a dataset of domains (e.g., all BTH partner universities or a specific industry sector).
*   **Graph Analysis:** Visualize the data as a node graph.
*   **Findings:** Demonstrate "Cluster Risks" (e.g., Company A doesn't use Atlassian directly, but 3 of their vendors do, meaning they are still vulnerable to an Atlassian outage/breach.).

**Why BTH will like it:** It uses Graph Theory and visualizes complex datasets, showing a deep understanding of Systemic Risk.

---

## Idea 3: The Machine Learning/Automation Thesis
**Title:** Automated Categorization of Unidentified DNS Patterns for Shadow IT Discovery

- **Focus:** Targets Goal 4 (Learning new patterns). Transforms the project from a "static lookup" to an "intelligent system."
- **Research Question:** Can unsupervised learning or natural language processing (NLP) accurately categorize unknown DNS TXT records into service types (e.g., 'Marketing', 'Security', 'HR') without manual intervention?

### Methodology
*   **Data Gathering:** Collect a massive dump of "Unknown" TXT records.
*   **Algorithm Design:** Experiment with a simple ML classifier (e.g., Naive Bayes or K-Means clustering) to group them.
*   **Experiment:** Compare the machine's "guess" against a human manual review.
*   **Result:** "The model correctly identified 85% of unknown records as 'Email Service Providers'."

**Why BTH will like it:** It incorporates AI/ML elements into security, which is a very hot topic.

---

## Idea 4: The Comparative Effectiveness Thesis
**Title:** The Hidden Surface: A Comparative Analysis of DNS-Based Supply Chain Discovery versus Web-Scraping Techniques

- **Focus:** Targets Goal 1 and 5 (Discovery capability). Validates why this method is better than existing methods.
- **Research Question:** Does DNS TXT/SPF analysis provide a more complete inventory of 3rd party SaaS usage compared to traditional HTTP header and HTML scraping analysis?

### Methodology
*   **Development:** Build your tool (The "DNS Method").
*   **Selection:** Select a standard open-source web scanner (The "Web Method", e.g., Wappalyzer).
*   **Experiment:** Run both tools against the same 500 domains.
*   **Comparison:** Create a Venn diagram showing what each tool found/missed (e.g., DNS finding a Payroll system missed by web scanners).

**Why BTH will like it:** It provides Empirical Evidence that justifies the existence of your tool.

---

## Critical Advice for BTH IT Security Theses

*   **Do not just "write code":** The code is an artifact used to generate data. Focus on the data and insights, not the lines of Python.
*   **Use a Standard Dataset:** Use the Tranco List or Majestic Million for a statistically significant sample size.
*   **Ethics Section:** Explicitly state that you are using passive reconnaissance (OSINT) and not active exploitation.