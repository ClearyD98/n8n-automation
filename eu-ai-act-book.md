# EU AI Act Compliance for Irish Business
## The Complete Practical Guide — 2026 Edition

**By Dylan Cleary, autoprod.io**

---

## About This Book

The EU AI Act took full effect on 2 August 2026. It is the most consequential piece of technology regulation ever passed — and Irish businesses are squarely in its crosshairs.

If your company uses AI for hiring, customer service, pricing, logistics, fraud detection, content generation, or virtually any decision that affects people — you need to comply. The fines reach €35 million or 7% of global turnover. The enforcement bodies are funded, staffed, and actively investigating.

This book is not a legal treatise. It is not a 400-page regurgitation of the legislation. It is a practical, no-nonsense guide written by someone who has built AI governance frameworks inside a global tech company and now helps Irish SMEs navigate the same waters.

You will learn:
- Whether the AI Act applies to your specific business (Chapter 1)
- How to classify your AI systems into the four risk tiers (Chapter 2)
- How to run a self-assessment audit in under 10 hours (Chapter 3)
- A proven 90-day compliance roadmap (Chapter 4)
- What happens if you ignore this — in real numbers (Chapter 5)
- Irish-specific considerations, including the DPC, GDPR overlap, and semi-state procurement (Chapter 6)
- When to handle compliance internally and when to bring in help (Chapter 7)
- Detailed sector guides for finance, health, recruitment, manufacturing, and legal (Chapters 8-12)
- Complete templates, checklists, and worksheets (Appendices)

Let's begin.

---

## Chapter 1: Does the AI Act Apply to You?

### 1.1 The Short Answer

**Probably yes.**

The EU AI Act applies to any business that:
- Develops or deploys AI systems in the EU market
- Has AI systems whose output is used in the EU
- Is established outside the EU but its AI output affects people in the EU

For Irish businesses, this covers virtually every company using:
- AI-powered recruitment or HR tools
- Automated customer service chatbots
- AI-driven pricing or underwriting systems
- Predictive maintenance algorithms
- Fraud detection systems
- AI-generated content or marketing copy
- Recommendation engines
- Automated decision-making in credit, insurance, or employment

### 1.2 The Key Test

Ask yourself one question about each system: **Does an AI system make or influence decisions that affect people?**

If the answer is yes — and for most businesses using modern software, it is — you are in scope.

### 1.3 What Is an "AI System" Under the Act?

The Act defines an AI system broadly as:

> "A machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments."

In plain English: if software makes decisions, predictions, or recommendations without a human explicitly programming every rule, it is likely an AI system under the Act.

This includes:
- Machine learning models (supervised, unsupervised, reinforcement learning)
- Large language models and generative AI (ChatGPT, Claude, Copilot)
- Rule-based systems with learned parameters
- Statistical models that produce predictions
- Computer vision systems
- Natural language processing systems
- Recommendation algorithms

It does NOT include:
- Traditional software with hardcoded business rules
- Simple calculators or spreadsheets
- Basic database queries
- Classic expert systems with no learned components

### 1.4 The Provider vs. Deployer Distinction

The Act distinguishes between two roles:

**Providers** develop AI systems and place them on the market. If you build an AI tool and sell it to others, you are a provider.

**Deployers** use AI systems in their operations. If you buy or license an AI tool and use it internally or with customers, you are a deployer.

Most Irish businesses are deployers — they use AI tools built by others (Microsoft Copilot, ChatGPT Enterprise, Salesforce Einstein, Workday AI, etc.). But some Irish companies are also providers, especially in the fintech, health-tech, and agri-tech sectors.

Both roles have obligations under the Act, but deployer obligations are generally lighter than provider obligations.

### 1.5 The Territorial Scope

The Act applies to:
- Providers and deployers **established in the EU**
- Providers and deployers **outside the EU** if their AI system's output is used in the EU
- Importers and distributors of AI systems in the EU market

This means an Irish subsidiary of a US company is covered. An Irish company selling to EU customers is covered. Even a purely Irish company serving only Irish customers is covered — because Ireland is in the EU.

### 1.6 Common Scenarios

**Scenario 1: Recruitment Agency Using AI Screening**

A Dublin recruitment agency uses an AI tool to screen CVs and rank candidates. The tool was bought from a UK vendor.

**Analysis:** This is a high-risk AI system (employment). The agency is a deployer. Obligations: ensure the system has been conformity-assessed by the provider, implement human oversight, inform candidates they are being assessed by AI, keep records.

**Scenario 2: Accountancy Firm Using ChatGPT**

A Cork accountancy firm lets staff use ChatGPT to draft client communications and summaries of tax guidance.

**Analysis:** This is limited-risk AI (transparency). The firm must disclose when content is AI-generated to clients. No further obligations unless the AI is used for automated decision-making about clients.

**Scenario 3: Manufacturing Company Using Predictive Maintenance**

A Limerick factory uses an AI system to predict when machines will fail based on sensor data.

**Analysis:** If the system is used for safety-critical machinery, it may be high-risk (product safety). If it is used only for non-critical scheduling, it is minimal-risk. Context matters.

**Scenario 4: Insurance Company Using AI Underwriting**

A Galway insurer uses an AI model to set premiums based on customer data.

**Analysis:** This is high-risk (essential private service — insurance). The insurer is a deployer. Full compliance obligations apply: risk management, data governance, transparency, human oversight, accuracy testing.

### 1.7 The Self-Assessment Flowchart

```
Does your business use software that makes
predictions, recommendations, or decisions?
        │
    No  └──→ Stop. The Act likely does not apply.
        │
    Yes ↓
        │
Does that software use machine learning,
statistical models, or language models?
        │
    No  └──→ Probably not an AI system. Document your reasoning.
        │
    Yes ↓
        │
Does the output affect people in the EU?
        │
    No  └──→ Act does not apply.
        │
    Yes ↓
        │
Does it fall into a regulated sector or
affect safety, rights, or essential services?
        │
    No  └──→ Likely limited or minimal risk. Transparency obligations only.
        │
    Yes ↓
        │
    HIGH RISK. Full compliance required.
    Continue to Chapter 2.
```

---

## Chapter 2: The Four Risk Tiers — Detailed Classification

### 2.1 Overview

The AI Act creates a pyramid of risk. The higher your system sits on the pyramid, the more obligations you have.

```
                    ┌─────────┐
                    │ BANNED  │  ← Prohibited entirely
                    └────┬────┘
                    ┌────┴────┐
                    │  HIGH   │  ← Full compliance framework
                    │  RISK   │
                    └────┬────┘
                    ┌────┴────┐
                    │ LIMITED │  ← Transparency only
                    │  RISK   │
                    └────┬────┘
                    ┌────┴────┐
                    │ MINIMAL │  ← No obligations
                    │  RISK   │
                    └─────────┘
```

### 2.2 Unacceptable Risk — BANNED

These AI practices are prohibited entirely. The prohibitions took effect in February 2025, six months before the rest of the Act.

**Banned practices:**

1. **Social scoring** — AI systems that evaluate or classify people based on social behaviour or personal characteristics, leading to detrimental treatment.

2. **Real-time remote biometric identification** in publicly accessible spaces by law enforcement, with narrow exceptions (search for missing children, prevention of imminent terrorist threat, identification of serious criminal suspects).

3. **AI systems that manipulate human behaviour** to cause physical or psychological harm — subliminal techniques or exploiting vulnerabilities due to age or disability.

4. **Emotion recognition systems** in workplaces and educational institutions (except for medical or safety purposes).

5. **Biometric categorization** that infers race, political opinions, trade union membership, religious beliefs, or sexual orientation.

6. **Untargeted scraping of facial images** from the internet or CCTV to build facial recognition databases.

7. **Predictive policing** based on profiling or personality traits.

**Penalties:** Up to €35 million or 7% of global annual turnover, whichever is higher.

**Irish context:** None of these are likely to affect legitimate Irish businesses. If you are building any of these systems, stop immediately and seek legal counsel.

### 2.3 High Risk — REGULATED

This is where most Irish businesses with AI systems will find themselves. High-risk AI is the Act's primary focus.

#### 2.3.1 What makes an AI system high-risk?

An AI system is high-risk if it falls into one of two categories:

**Category A: Product Safety**

The AI system is a safety component of a product covered by EU harmonization legislation, or the AI system is itself such a product. This includes:
- Medical devices (Class IIa and above)
- Machinery
- Toys
- Lifts
- Personal protective equipment
- Radio equipment
- Cableway installations
- Appliances burning gaseous fuels
- Pressure equipment
- Recreational craft

**Category B: Regulated Use Cases (Annex III)**

The AI system is used in one of eight specific areas:

1. **Biometrics** (when permitted) — remote biometric identification, biometric categorization, emotion recognition
2. **Critical infrastructure** — safety components in the management and operation of road traffic, water, gas, heating, and electricity
3. **Education and vocational training** — determining access, admission, or assignment; evaluating learning outcomes; assessing appropriate education level; monitoring prohibited behaviour during tests
4. **Employment, workers' management, and access to self-employment** — recruitment and selection; making decisions on promotions, terminations, and task allocation; monitoring and evaluating performance and behaviour
5. **Access to essential private and public services** — creditworthiness assessment; risk assessment and pricing for life and health insurance; emergency triage and dispatch
6. **Law enforcement** (when permitted) — various uses including individual risk assessments, polygraphs, evidence reliability, profiling, crime analytics
7. **Migration, asylum, and border control** (when permitted) — polygraphs, security risk assessments, application processing, forecasting migration
8. **Administration of justice and democratic processes** — assisting judicial authorities in researching and interpreting facts and law; influencing election outcomes

#### 2.3.2 Obligations for High-Risk AI Systems

If your AI system is high-risk, you must implement:

**1. Risk Management System (Article 9)**
A continuous, iterative process throughout the AI system's lifecycle:
- Identify known and foreseeable risks to health, safety, and fundamental rights
- Estimate and evaluate risks that may emerge when the system is used as intended or under reasonably foreseeable misuse
- Adopt appropriate risk management measures
- Test the system to identify the most appropriate measures
- Ensure residual risks are acceptable

**2. Data Governance (Article 10)**
For systems that involve training models with data:
- Training, validation, and testing datasets must be relevant, representative, free of errors, and complete
- Datasets must take into account the specific geographical, behavioural, or functional setting of intended use
- Data governance practices must cover: design choices, data collection, data preparation (annotation, labelling, cleaning, enrichment, aggregation), formulation of assumptions, assessment of data availability and suitability, examination for biases

**3. Technical Documentation (Article 11)**
Before placing the system on the market or putting it into service, you must draw up technical documentation demonstrating compliance. This includes:
- General description of the AI system
- Detailed description of system elements and development process
- Description of system architecture and design specifications
- Description of training methodologies and datasets
- Description of risk management system
- Description of changes made to the system over its lifecycle
- List of harmonized standards applied
- Copy of EU declaration of conformity
- Description of post-market monitoring system

**4. Record-Keeping (Article 12)**
High-risk AI systems must automatically record events (logs) during operation:
- Recording of the period of each use
- Reference database against which input data has been checked
- Input data for which the search has led to a match
- Identification of natural persons involved in verification of results

**5. Transparency and Information (Article 13)**
Deployers must be able to interpret the system's output and use it appropriately:
- The provider's identity and contact details
- The system's characteristics, capabilities, and limitations
- The system's intended purpose
- The level of accuracy, robustness, and cybersecurity
- Known circumstances that may lead to risks
- The system's performance on specific groups of people
- Specifications for input data
- Human oversight measures
- Expected lifetime and maintenance measures

**6. Human Oversight (Article 14)**
The system must be designed so natural persons can oversee it:
- Understand the system's capabilities and limitations
- Monitor its operation and detect anomalies
- Interpret the system's output correctly
- Decide not to use the system or disregard its output
- Intervene in the system's operation or stop it

**7. Accuracy, Robustness, and Cybersecurity (Article 15)**
The system must be:
- Accurate: appropriate levels of accuracy must be declared and achieved
- Robust: resilient to errors, faults, inconsistencies, and adversarial manipulation
- Cybersecure: protected against attacks attempting to exploit vulnerabilities, including data poisoning, model evasion, and adversarial examples

#### 2.3.3 The Notified Body System

For certain high-risk AI systems, conformity assessment must be carried out by an independent third party called a "notified body." These are organizations designated by EU member states to assess compliance.

The Irish National Standards Authority (NSAI) is the primary notified body for Ireland, though it has not yet been fully designated for all AI Act functions.

For most high-risk AI systems deployed by Irish SMEs, a notified body assessment will NOT be required — internal conformity assessment (self-assessment) is sufficient, provided you can demonstrate compliance with harmonized standards.

### 2.4 Limited Risk — TRANSPARENCY

Limited-risk AI systems have minimal obligations. The primary requirement is **transparency**: users must be informed they are interacting with an AI system.

**Systems covered:**
- AI systems intended to interact directly with natural persons (chatbots, virtual assistants) — users must be informed they are dealing with AI
- AI systems that generate synthetic audio, image, video, or text content — the output must be marked as artificially generated or manipulated
- Emotion recognition systems (outside workplace/education, where they are banned)
- Deepfake generation systems — the content must be labelled as artificially manipulated

**One exception:** AI-generated content that has undergone human review with editorial responsibility does not need to be labelled, provided it is clearly part of a creative, satirical, artistic, or fictional work.

**Practical steps for Irish businesses:**
- Add "AI-powered" labels to chatbots on your website
- Include "Generated with AI assistance" disclaimers on AI-written content
- If you use AI in customer calls, include a pre-recorded message stating this
- If you generate images with AI for marketing, watermark or label them

### 2.5 Minimal Risk — NO REGULATION

These AI systems face no regulatory obligations under the Act. They represent the vast majority of AI applications currently in use.

**Examples:**
- AI-powered video games
- Spam filters
- Inventory management and demand forecasting
- Basic process automation (no decisions about people)
- AI-enhanced search functions
- Grammar checkers and spell-checkers
- Recommendation engines for non-regulated content (music, movies, products — but watch for workplace/employment implications)

**Note:** Minimal-risk status can change. If your "minimal-risk" system starts being used for a high-risk purpose — for example, a demand forecasting tool being used to make hiring decisions — it becomes high-risk.

---

## Chapter 3: The Self-Assessment Audit

### 3.1 Why Audit First?

Before spending a single euro on compliance consultants, software, or training, you need to know what you are dealing with.

The self-assessment audit answers four questions:
1. What AI systems do we actually have?
2. What risk tier does each fall into?
3. What are the gaps between our current state and compliance?
4. What should we fix first?

This chapter walks you through the audit process step by step. Set aside 6-10 hours. Gather your IT lead, your operations lead, and anyone who procures software.

### 3.2 Step 1: AI System Inventory (2-3 hours)

Create a spreadsheet. List every system your company uses that could qualify as AI. Be thorough — include systems you may not think of as "AI."

**Template columns:**

| Column | Description | Example |
|--------|-------------|---------|
| System Name | What you call it | "CV Screening Tool" |
| Vendor/Build | Who made it? | "HireVue Ltd" |
| Purpose | What does it do? | "Screens and ranks job applicants" |
| Data Used | What data feeds it? | "CVs, LinkedIn profiles, assessment scores" |
| Decisions Made | What does it decide? | "Shortlists top 10 candidates" |
| Affected People | Who is impacted? | "Job applicants (100/month)" |
| Autonomy Level | How automated is it? | "Fully automated — outputs sent to hiring manager" |
| Deployment Date | When did we start using it? | "March 2025" |
| Contract Owner | Who manages the vendor relationship? | "HR Director" |

**Systems to look for:**

*HR & People:*
- Recruitment platforms (LinkedIn Recruiter AI, Indeed AI matching)
- CV screening and ranking tools
- Video interview analysis tools
- Employee performance monitoring
- Workforce scheduling and task allocation
- Promotion and compensation recommendations
- Employee sentiment analysis
- Learning and development personalization

*Customer-Facing:*
- Chatbots and virtual assistants on your website
- AI-powered customer service routing
- Sentiment analysis on customer calls or messages
- Personalization engines on your website or app
- Recommendation systems
- Automated email responses

*Finance & Operations:*
- Credit scoring or risk assessment tools
- Insurance underwriting or pricing models
- Fraud detection systems
- Anti-money laundering screening
- Predictive maintenance systems
- Supply chain optimization
- Inventory forecasting
- Dynamic pricing algorithms

*Marketing & Content:*
- AI content generation tools (Jasper, Copy.ai, ChatGPT for marketing)
- AI image or video generation
- SEO optimization tools with AI components
- Email marketing optimization
- Ad targeting and bidding algorithms

*IT & Security:*
- AI-powered cybersecurity tools (anomaly detection)
- Automated code review or testing tools
- AI-powered help desk or IT support
- Network monitoring with ML components

### 3.3 Step 2: Risk Classification (1-2 hours)

For each system in your inventory, determine its risk tier using the framework in Chapter 2.

Create a new column: "Risk Tier" with values: BANNED, HIGH, LIMITED, MINIMAL.

**Decision tree for each system:**

1. Does it fall into a banned category? → BANNED. Stop using immediately. Consult a lawyer.
2. Does it relate to product safety (medical devices, machinery, toys, etc.)? → HIGH.
3. Does it operate in one of the eight Annex III areas (employment, education, critical infrastructure, essential services, law enforcement, migration, justice, biometrics)? → HIGH.
4. Does it interact directly with people or generate content? → LIMITED.
5. Everything else → MINIMAL.

**Red flags that suggest high-risk classification:**
- The system makes decisions about people's employment, credit, or education
- The system operates without meaningful human review
- The system affects children or vulnerable adults
- The system has known bias issues
- The system was built or trained on data that may not represent your users
- The vendor's documentation is vague about how the system works

### 3.4 Step 3: Gap Analysis (2-3 hours)

For each HIGH-RISK system, assess your current compliance against the obligations listed in Section 2.3.2.

**Gap Analysis Worksheet:**

For each high-risk system, rate each obligation on a scale of 1-5:
1 = Completely missing
2 = Some awareness but no formal process
3 = Partial implementation
4 = Mostly in place
5 = Fully compliant

| Obligation | Rating | Evidence/Gap | Priority |
|-----------|--------|-------------|----------|
| Risk management system |||
| Data governance |||
| Technical documentation |||
| Record-keeping/logging |||
| Transparency to users |||
| Human oversight |||
| Accuracy testing |||
| Robustness testing |||
| Cybersecurity |||
| Conformity assessment |||

**Priority scoring:**
- Obligations rated 1-2 with high regulatory risk → **Critical**
- Obligations rated 1-2 with moderate risk → **High**
- Obligations rated 3 → **Medium**
- Obligations rated 4-5 → **Low**

### 3.5 Step 4: Prioritized Action Plan (1-2 hours)

Rank the gaps by:
1. **Regulatory urgency** — what would get you fined fastest?
2. **Business impact** — what affects customers or operations most?
3. **Implementation effort** — what is fastest to fix?

**Template:**

| Priority | System | Gap | Action | Owner | Deadline | Cost |
|----------|--------|-----|--------|-------|----------|------|
| Critical | CV Screening | No transparency | Add notice to job ads: "AI-assisted screening used" | HR Director | 1 week | €0 |
| High | Underwriting Model | No bias testing | Commission third-party bias audit | CTO | 4 weeks | €3,000 |
| Medium | Chatbot | AI not disclosed | Add "AI-powered" badge to widget | Marketing | 2 weeks | €500 |

### 3.6 Self-Assessment Summary

After completing the audit, you should have:

1. A complete inventory of all AI systems
2. Each system classified by risk tier
3. A gap analysis for all high-risk systems
4. A prioritized action plan with owners and deadlines

**Estimated effort:** 6-10 hours spread over 1-2 weeks.

**Estimated cost:** Free if done internally. €250 if you want autoprod.io to run it for you (includes board-ready report and facilitation).

**What if I find nothing?**
If your audit reveals zero high-risk AI systems, document your findings and review quarterly. The regulatory landscape is evolving, and systems that are minimal-risk today may become high-risk as your usage changes or as regulatory guidance is published.

---

## Chapter 4: The 90-Day Compliance Roadmap

### 4.1 Overview

This chapter assumes you have completed the self-assessment audit (Chapter 3) and identified your high-risk AI systems. It provides a practical, week-by-week roadmap to compliance.

The roadmap is designed for a small to medium Irish business with 1-5 high-risk AI systems. If you have more systems or complex deployments, scale the timeline accordingly.

### 4.2 Month 1: Foundation (Days 1-30)

**Week 1: Governance Setup**
- Day 1-2: Appoint an AI Officer. This does not need to be a full-time role for SMEs. It can be your CTO, IT Manager, Compliance Officer, or an external consultant acting as Designated AI Officer.
- Day 3-4: Brief your leadership team on the AI Act's requirements and the compliance roadmap. Get explicit buy-in and budget commitment.
- Day 5: Set up your AI compliance documentation repository. This can be a shared drive, SharePoint, Notion, or a dedicated compliance platform.

**Week 2: Inventory & Classification**
- Day 8-10: Complete your AI system inventory (if not done during audit).
- Day 11-12: Classify each system by risk tier (if not done during audit).
- Day 13-14: Document your classification rationale for each system. This is your defence if challenged by a regulator.

**Week 3: Risk Assessment Begins**
- Day 15-19: For each high-risk system, begin the formal risk assessment. Document known risks, foreseeable risks, and risks from reasonably foreseeable misuse.
- Day 20-21: Prioritize risks by severity and likelihood. Use a standard risk matrix (5x5 severity × likelihood).

**Week 4: Training & Awareness**
- Day 22-24: Develop a 90-minute AI Act awareness training module for all staff.
- Day 25-26: Deliver training to management and key operational staff.
- Day 27-28: Create a one-page "AI Act: What You Need to Know" summary for all employees.
- Day 29-30: Review Month 1 progress against the roadmap. Adjust timelines if needed.

### 4.3 Month 2: Implementation (Days 31-60)

**Week 5: Data Governance**
- Day 31-35: Document your data governance practices for each high-risk AI system. Cover: data sources, collection methods, preprocessing steps, bias examination, representativeness assessment.
- Day 36-37: If using third-party systems, request data governance documentation from your vendors.

**Week 6: Technical Documentation**
- Day 38-42: Begin drafting technical documentation for each high-risk system. Start with the system description and architecture (the easiest parts).
- Day 43-44: Document training methodologies, model selection rationale, and performance metrics.

**Week 7: Transparency & Human Oversight**
- Day 45-47: Implement transparency measures. Add AI disclosures to your website, job postings, customer communications, and terms of service.
- Day 48-49: Design and document your human oversight procedures. Define: who oversees each system, how often they review outputs, what they do if they find anomalies, and the escalation path.
- Day 50-51: Test your human oversight procedures with real scenarios.

**Week 8: Record-Keeping**
- Day 52-54: Implement logging for high-risk AI systems. If the system does not support native logging, establish a manual logging process.
- Day 55-56: Define log retention periods. The Act requires logs to be kept for at least six months (longer for certain systems).
- Day 57-58: Test your record-keeping: can you produce logs for a specific decision made two months ago?
- Day 59-60: Review Month 2 progress.

### 4.4 Month 3: Validation & Maintenance (Days 61-90)

**Week 9: Accuracy & Bias Testing**
- Day 61-65: Conduct formal accuracy testing for each high-risk system. Define your accuracy metrics, test against representative datasets, document results.
- Day 66-67: Conduct bias testing. Test for disparate impact across protected characteristics (age, gender, ethnicity, disability status). Document findings.

**Week 10: Cybersecurity Assessment**
- Day 68-72: Commission or conduct a cybersecurity assessment for each high-risk AI system. Include: penetration testing, adversarial example testing, data poisoning vulnerability assessment.
- Day 73-74: Address critical vulnerabilities immediately. Document remaining risks with mitigation plans.

**Week 11: Final Documentation & Review**
- Day 75-79: Complete and review all technical documentation. Ensure consistency across systems.
- Day 80-81: Draft EU declaration of conformity (template in Appendix D).
- Day 82-83: Conduct internal compliance review. Have someone who was not involved in the process review your documentation and challenge assumptions.

**Week 12: Go-Live & Ongoing Monitoring**
- Day 84-85: Implement post-market monitoring system. Define: what metrics you will track, who reviews them, how often, and what triggers a review.
- Day 86-87: Brief leadership on completed compliance programme. Present residual risks and ongoing obligations.
- Day 88-90: Celebrate. Compliance is hard. You have done something most businesses have not. Now maintain it.

### 4.5 Ongoing Obligations

Compliance is not a one-time project. You must:

**Monthly:**
- Review AI system logs for anomalies
- Check for regulatory updates or new guidance
- Monitor vendor notifications for changes to third-party AI systems

**Quarterly:**
- Re-run bias and accuracy tests
- Review and update risk assessments
- Refresh training for new hires
- Review your AI inventory for new systems

**Annually:**
- Full compliance audit and documentation refresh
- Reassess risk classifications (systems can migrate between tiers)
- Review and update your conformity declarations
- Budget for compliance maintenance

**When things change:**
- New AI system deployed → full assessment before go-live
- Major update to existing system → reassessment
- Regulatory enforcement action in your sector → review and tighten
- Security incident or bias complaint → immediate investigation

---

## Chapter 5: Consequences of Non-Compliance

### 5.1 The Fine Structure

The EU AI Act's penalties are among the most severe in any technology regulation:

| Violation | Maximum Fine |
|-----------|-------------|
| Banned AI practices | €35 million or 7% of global annual turnover |
| Non-compliance with high-risk obligations (data governance, transparency, human oversight, etc.) | €15 million or 3% of global annual turnover |
| Supplying incorrect, incomplete, or misleading information to authorities | €7.5 million or 1.5% of global annual turnover |

For SMEs and startups, the lower of the two amounts (fixed sum vs. percentage) applies.

### 5.2 Real Numbers for Irish Businesses

| Annual Revenue | 7% Fine | 3% Fine | 1.5% Fine |
|---------------|---------|---------|-----------|
| €500,000 (micro-business) | €35,000 | €15,000 | €7,500 |
| €2 million (small) | €140,000 | €60,000 | €30,000 |
| €5 million (medium) | €350,000 | €150,000 | €75,000 |
| €20 million (large SME) | €1,400,000 | €600,000 | €300,000 |
| €100 million (enterprise) | €7,000,000 | €3,000,000 | €1,500,000 |

### 5.3 Beyond Fines

Financial penalties are not the only consequence of non-compliance:

**Reputational Damage**
Regulatory actions are public. A DPC enforcement notice becomes a press release. Your customers, partners, and investors will see it. For B2B companies, non-compliance may disqualify you from procurement processes.

**Operational Disruption**
Regulators can order you to:
- Withdraw an AI system from the market
- Restrict or prohibit its use
- Recall it from deployers

If your business depends on an AI system — for hiring, underwriting, customer service, fraud detection — having it pulled by a regulator is an existential threat.

**Contractual Fallout**
Your commercial contracts may require compliance with applicable laws. A regulatory finding of non-compliance could trigger:
- Termination rights for your customers
- Warranty claims
- Indemnification obligations
- Insurance exclusion (your D&O or cyber policy may not cover regulatory fines)

**Personal Liability**
Under certain circumstances, directors and officers may face personal liability for compliance failures, particularly if they were aware of the risk and chose not to act.

### 5.4 Enforcement Bodies

**The European AI Office** (within the European Commission) oversees the Act's implementation, coordinates national authorities, and enforces rules for general-purpose AI models.

**National Competent Authorities** in each member state enforce rules for high-risk AI systems. In Ireland, the Data Protection Commission (DPC) is expected to take the lead, alongside sectoral regulators (Central Bank for financial services, HPRA for medical devices, etc.).

**The Irish DPC** is well-funded, increasingly assertive, and already experienced with complex technology regulation from GDPR enforcement. It has fined major technology companies hundreds of millions of euros under GDPR. The AI Act gives it additional powers and a broader mandate.

### 5.5 Enforcement Timeline

- **February 2025:** Banned AI practices prohibitions took effect
- **August 2025:** General-purpose AI model obligations took effect
- **August 2026:** Full Act took effect — high-risk AI obligations, transparency requirements, penalties
- **August 2027:** Obligations for high-risk AI systems that are products covered by EU legislation take effect (extended transition)

The Irish DPC has indicated it will prioritize education and guidance in the first year of enforcement (2026-2027), but it has also stated that intentional non-compliance or particularly harmful systems will face enforcement action from day one.

### 5.6 The Cost-Benefit Analysis

For an Irish SME with €5 million annual revenue and two high-risk AI systems:

**Cost of compliance:** €5,000-€15,000 (one-time) + €2,000-€5,000/year (ongoing)
**Cost of non-compliance:** €75,000-€350,000 (single fine) + operational disruption + reputational damage

The math is simple. Compliance costs roughly 1-5% of the potential fine. And fines are just the beginning.

---

## Chapters 8-12: Sector-Specific Guides

*[Each chapter follows this structure: industry overview, common AI use cases, risk classification walkthrough, compliance checklist, case study, key contacts and resources]*

### Chapter 8: Financial Services
- Credit scoring and loan underwriting
- Fraud detection and AML
- Insurance pricing and claims
- Robo-advisory and investment management
- Central Bank of Ireland expectations
- DORA and AI Act interaction

### Chapter 9: Healthcare and Life Sciences
- Medical device AI (Class IIa+)
- Diagnostic and triage AI
- Patient management systems
- HPRA notified body role
- Clinical evidence requirements

### Chapter 10: Recruitment and HR
- CV screening and candidate ranking
- Video interview analysis
- Employee monitoring and performance
- Irish employment law interaction
- WRC considerations

### Chapter 11: Manufacturing and Industry
- Predictive maintenance
- Quality control AI
- Supply chain optimization
- Safety-critical applications
- CE marking interaction

### Chapter 12: Legal and Professional Services
- AI for legal research and document review
- Contract analysis
- Professional indemnity implications
- Law Society of Ireland guidance
- Client confidentiality and AI

---

## Appendices

### Appendix A: AI System Inventory Template
### Appendix B: Risk Assessment Worksheet
### Appendix C: Gap Analysis Template
### Appendix D: EU Declaration of Conformity Template
### Appendix E: Compliance Calendar (Monthly/Quarterly/Annual Tasks)
### Appendix F: Glossary of Terms
### Appendix G: Key Contacts and Resources
### Appendix H: Sample AI Act Policy for Employee Handbook

---

## About the Author

Dylan Cleary is an AI Systems Architect based in Dublin, Ireland. He spent over four years at Stripe in enterprise support and escalations, where he co-founded the PSO AI Council and led AI governance, training, and enablement for a 200+ person global support organization.

At Stripe, Dylan:
- Designed and delivered AI training programmes across four international sites
- Co-founded the PSO AI Council with a formal three-pillar governance structure (Enablement, Execution, Governance)
- Built production AI agents for quality review and performance analytics
- Managed executive escalations for Fortune 500 clients
- Led on-call quality strategy, training 23+ Operations Associates and 7 Train-the-Trainers

He now helps Irish businesses navigate the EU AI Act through autoprod.io — a fixed-price AI governance consultancy designed for companies that need Big 4-quality compliance without Big 4 prices.

**Services:**
- **AI Readiness Audit (€250):** Complete AI system inventory, risk classification, gap analysis, board-ready report. 2 weeks.
- **AI Governance Framework (€5,000):** Full policy suite, 90-day implementation roadmap, staff training, DPC-aligned documentation. 4 weeks.

**Contact:** dylan@autoprod.io
**Website:** https://autoprod.io
**LinkedIn:** https://www.linkedin.com/in/dylan-cleary-a510b7105/

---

*This guide is for informational purposes and does not constitute legal advice. Every business situation is unique. Consult a qualified lawyer for advice specific to your circumstances. The author has made reasonable efforts to ensure accuracy as of the publication date, but the regulatory landscape evolves rapidly.*

© 2026 autoprod.io. All rights reserved.
