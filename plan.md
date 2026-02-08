
# Project Plan for Degree Project

**Template version:** 1.6 -- June 12, 2020
**Course:** DV1583: Degree Project for Bachelor of Science in Engineering (Computer Science)

## Project Details

| Category | Details |
| --- | --- |
| **Title** | **Beyond the Third Party: Quantifying Systemic Risk in DNS Supply Chains** |
| **Classification** | Network Security, Risk Management, Graph Algorithms |
| **Student 1** | **Ludwig Sterner**<br>

<br>E-Mail: luse23@student.bth.se<br>

<br>Person nr: 0302220439<br>

<br>Program: Bachelor of Science in Engineering (Computer Science) |
| **Student 2** | **William Silvstrand**<br>

<br>E-Mail: wisl22@student.bth.se<br>

<br>Person nr: 9810130097<br>

<br>Program: Bachelor of Science in Engineering (Computer Science) |
| **Supervisor** | **Oleksii Baranovskyi**<br>

<br>E-Mail: oleksii.baranovskyi@bth.se<br>

<br>Department: DIDA |
| **Co-advisor** | **Martin Jartelius, AI Product Director**<br>

<br>E-Mail: mj@outpost24.com<br>

<br>Company: Outpost24 AB |

> *2012 ACM Computing Classification System: www.acm.org/about/class/2012*

---

## 1. Introduction

The modern software landscape has shifted from monolithic, on-premise architectures to distributed, third-party service-oriented systems. Software as a Service (SaaS) and cloud-native dependencies are now the backbone of digital infrastructure. Organizations increasingly rely on third-party vendors for critical functions, ranging from Authentication (e.g., Auth0) to email delivery (e.g., SendGrid). The security of the "digital supply chain" has become an increasing concern in cybersecurity governance according to Liu et al. (2024).

However, this reliance on shared infrastructure introduces significant security complexities. As noted by Zhang et al. (2024), the "Cross-Zone" nature of modern cloud services creates logical gaps where trust is granted but rarely verified. A critical, yet often overlooked aspect of this supply chain is the chains of trust established via DNS records (TXT, SPF, MX etc.). These records will often contain static references to third-party vendors. However, organizational dependencies rarely exist in a flat hierarchy; instead, third-party vendors frequently rely on fourth-party vendors, creating a "multi-layered recursive graph" of trust that is unknown to most administrators.

To understand the scope of this vulnerability, two key concepts must be defined:

* **Recursive DNS Dependencies:** Unlike a direct relationship where an organization trusts a vendor, recursive dependencies occur when that vendor silently "includes" fourth-party services via DNS records. For example, an SPF record including `include:thirdparty.com` may recursively trust `include:fourthparty.com`, extending the attack surface beyond the organization's control.
* **Dangling DNS:** This refers to DNS records that point to resources, such as cloud storage or SaaS subdomains, that have been decommissioned or expired. Liu et al (2024) identify these as a primary vector for domain hijacking, allowing attackers to claim the abandoned resource and take control over the domain's reputation.

### Research Gap

While the security of the "digital supply chain" has become a growing concern in cybersecurity, as organizations transition from traditional models to complex digital ecosystems involving cloud computing and IoT (Zhang et al., 2019), existing research and industry tools largely approach supply chain risk through flat vendor ratings or static pattern matching.

* **Software & Infrastructure:** While significant research has been conducted on recursive dependencies in software package managers (e.g., NPM, PyPI), Kula and Reid (2025) argue that "end-of-chain" dependencies are the most critical yet least observed. However, this recursive analysis has yet to be applied to DNS infrastructure, where trust chains are often treated as linear lists rather than directed graphs.

This thesis addresses the blindness toward recursive trust chains. As Squarcina et al. (2021) demonstrated, "dangling" records allow for subdomain takeovers that bypass policies. Without a tool to recursively map these dependencies to depth (*n*) and quantify their risk, organizations remain vulnerable to hijacking attacks from deep within their supply chain.

The relevance of this research extends beyond theoretical modeling. Liu et al. (2024) identified over 20,000 active subdomains hijacked due to "dangling pointers", proving this is a widespread systematic failure. By developing a Recursive Graph Analysis (RGA) tool, this project aims to shift the industry standard from "flat" auditing to depth-aware risk scoring.

## 1.1 Ethical, societal and sustainability aspects

This project involves scanning public DNS records. While this data is public, using it to highlight security vulnerabilities raises ethical concerns regarding responsible disclosure.

### Industry Compliance

All active scanning and data usage will be conducted under the strict supervision of Outpost24 AB, utilizing their resources and following their responsible disclosure policies.

### Data privacy

Throughout this project, strict protocols will be implemented to ensure that sensitive data from various organizations remains unexposed within the thesis report.

---

## 2. Aim and objectives

The overall aim of this thesis is to develop a method using tools and algorithms to create a systemic supply chain risk by performing a recursive graph analysis of DNS dependencies. This method will map third-party relationships and calculate a risk score based on dependency depth, service criticality, and vulnerability status.

### Objectives & Achievable goals

1. **Recursive Graph Analysis (RGA):** Develop a tool capable of recursively parsing DNS records (TXT, SPF, MX, etc.) to map an organization's supply chain dependencies to a defined depth (*n*).
2. **Service Classification:** Leverage existing pattern libraries for known vendors and utilize an auxiliary AI tool (LLM/AGI) to suggest categories for unknown domains based on naming conventions.
3. **"Dangling" & Integrity Risks:** Implement deterministic logic to identify expired domains ("dangling DNS") and weak SPF configurations that allow for hijacking.
4. **CTI:** Automate correlation of identified vendors with **active** threat feeds (CISA KEV, NVD, EUVD) to prioritize "exploitable" risks over theoretical ones.
5. **RSM:** Design and develop a quantitative risk algorithm (0-1) that aggregates Graph Depth, Service Criticality, and Vulnerability Status into a single measurable value.

---

## 3. Research questions

* **RQ1:** How can recursive analysis of DNS records be utilized to map and visualize the multi-tier software supply chain of an organization?
* **RQ2:** To what extent can automated analysis of DNS trust chains (TXT/SPF/MX) detect "dangling" or misconfigured dependencies that expose organizations to domain-hijacking risks?
* **RQ3:** How does a RSM (Risk Scoring Model) improve the prioritization of critical vulnerabilities within the supply chain compared to the traditional flat vendor rating?

---

## 4. Method

The Design Science Research (DSR) Methodology will be used to iteratively build and evaluate the "third-party risk mapper" artifact.

### 4.1 Literature Review

To establish a strong theoretical foundation for our artifact, a systematic literature review should be conducted. Focusing on three intersecting domains: Software Supply Chain Security, DNS-based vulnerabilities, and Network Security.

### 4.2 Implementation

* **Recursive Scanner:** We will develop a tool using available libraries to traverse the DNS dependencies producing a node graph that visualizes existing vendor dependencies.
* **Classification Engine:** We will implement and use already existing libraries of Regex patterns for high-confidence matching. For unknown domains, we will integrate a lightweight LLM API (e.g., OpenAI, Google, Anthropic) supplied by Outpost24 AB as a copilot to give suggestions regarding classifications, which are then verified or flagged for review.

### 4.3 Experiment & Evaluation

* **Data Collection:** We will run the artifact against a vast dataset of domains provided by Outpost24 to generate dependency graphs, which will help us to create a large dataset of domains and their dependencies as a substantial dataset is required to generate statistically significant results.

### 4.4 Validation

* **Third party assessment:** The generated graph and risk score will be presented to an Outpost24 AB employee for evaluation regarding whether the RSM improves the prioritization of critical risks compared to the industry standard check.
* **Technical verification:** A random sample will be manually verified for detected "dangling" pointers and recursive chains for determination regarding the artifact's accuracy and false positive rate (loop detection and infinite recursion handling).

---

## 5. Expected outcomes

* **A recursive DNS Node Graph Risk Mapper:** A functional tool that outputs a visual node graph of dependencies to the user, that shows what dependencies an organization might have, and facilitates a deeper understanding of the dependency hierarchy.
* **Risk Scoring Framework:** A documented algorithm for calculating supply chain risk, given data from the recursive DNS Node Graph Risk Mapper.
* **Thesis Report:** A detailed report regarding the "dangling" risks and the effectiveness of recursive mapping, which also should answer the research questions which are asked.

---

## 6. Time and activity plan

| Month | Week | Activity & Deliverables |
| --- | --- | --- |
| **February** | 6 | Finalize Project Plan<br>

<br>**Deadline: Feb 8 (1st Submission)** |
|  | 7--8 | Literature Review, Tool Setup & Access (Outpost24) |
| **March** | 9--10 | Develop Recursive Scanning Algorithm (Graph Logic) |
|  | 11--12 | Implement "Dangling" Detection & Pattern Library<br>

<br>**Deadline: Mar 22 (2nd Submission)** |
| **April** | 13--14 | Integrate AI Helper & Threat Feeds |
|  | 15--16 | Data Collection & Validation with Industry Experts |
| **May** | 17--19 | Writing Final Report & Adjustments<br>

<br>**Deadline: May 10 (Thesis Draft)** |
|  | 20 | Preparation for Defense<br>

<br>**Deadline: May 24 (Opposition Report)** |
|  | 21 | **Thesis Presentation (May 25--29)** |
| **June** | 23 | Final Revisions based on feedback<br>

<br>**Deadline: Jun 7 (Final Thesis)** |

### Supervision plan

* **Industry:** Weekly syncs or when needed with Martin Jartelius (Outpost24) for technical guidance and access to internal tools/datasets.
* **Academic:** Bi-weekly or when needed meetings with Oleksii Baranovskyi to ensure academic compliance and that the project stays on the right path.

---

## 7. Limitations and risk management

### 7.1 Limitations

While this project aims to provide a clear view of supply chain risks, certain technical and scope boundaries are established to ensure feasibility within the thesis timeline.

1. **No Active Exploitation:** The tool will only identify potential vulnerabilities and high-risk scores; no active exploitation attempts will be made, or attempts to prove the ability of exploitation. This is outside the scope and ensures adherence to ethical and legal boundaries.
2. **Public DNS Only:** The analysis is limited to externally visible DNS records. No internal or private intranets will be used in the collection of data.
3. **Unclear Service Tiers:** In some cases, a "Free Tier" and an "Enterprise Tier" service may use identical DNS configurations. In such instances, the tool will mark the service tier as "Unknown" rather than making an unreliable guess. This is to ensure high confidence in results.
4. **Snapshot-based analysis:** The tool will provide a point-in-time snapshot of the dependency graph, rather than real-time monitoring. However, the impact of this limitation is likely minimal, as DNS records typically exhibit low volatility.

### 7.2 Risk Mitigation

| Risk | Likelihood | Severity | Mitigation |
| --- | --- | --- | --- |
| **Infinite Recursion:** A DNS loop (e.g., Domain A includes B, B includes A) causes the scanner to hang or crash. | Medium | High | Implement a strict `max_depth` limit (e.g., 10 levels) and maintain a "visited nodes" cache to detect and break cycles immediately. |
| **AI Hallucinations:** The AI helper misclassifies a critical security tool as a low-risk "Marketing" tool, skewing the risk score. | Medium | High | Use AI only as a suggestion engine. Implement a "Confidence Threshold"—if confidence is <80%, flag as "Unclassified" for manual review. |
| **Data Access Limits:** Public DNS resolvers or Threat Intel APIs rate-limit the scanner during bulk testing. | High | Medium | Implement exponential backoff for retries and leverage Outpost24's internal cached DNS datasets to reduce external query volume. |
| **False Positives (Dangling):** A domain appears expired (NXDOMAIN) but is actually a temporary glitch or internal-only record. | Medium | Medium | Perform double-verification using multiple resolvers (e.g., Google, Cloudflare, Quad9) before flagging a record as "Dangling." |
| **Scope Creep:** The ambition to map *every* possible vulnerability delays core development. | High | Low | Strictly adhere to the "Must Have" vs. "Nice to Have" feature list defined in the project plan. Prioritize the Recursive Graph over advanced AI features. |
