# Exam technique

How to turn what you know into marks in the CSC 583 paper. Read this once early in your revision and again the day before the exam.

## The paper

!!! warning "The format below is an assumption"
    No past papers were available. The format comes from the student's description: a **written paper of about five questions**, possibly with a **compulsory Question 1**, of which you answer **three or four**. The site assumes **2 hours** and **about 20 marks per question**, split into parts (a), (b), (c) and sometimes (d). Check the real instructions on the day and adjust the time plan.

What the questions test, from the same description:

- **Most marks are for the concepts exactly as taught:** definitions, lists with their full count, explanations and comparisons. Each unit's **Recall drill** is built to cover every one of these.
- **Some parts are applied:** a short scenario where you identify the concept, apply it and justify a recommendation. Use I-A-J-A (below).

### Time plan

| | Answer 3 questions | Answer 4 questions (Q1 + 3 others) |
|---|---|---|
| Read the whole paper, choose questions, mark which units each part needs | 5 min | 5 min |
| Per question | 35 min (≈ 1¾ min per mark) | 27 min (≈ 1⅓ min per mark) |
| Final check: counts, labels on diagrams, unanswered parts | 10 min | 7 min |

- **Do the compulsory question first** if there is one. It is usually many short parts across the course, so it is the cheapest marks on the paper.
- **Spend time in proportion to the marks.** A 4-mark definition does not need a page; a 10-mark scenario needs a structured answer.
- **Never leave a part blank.** A correct definition and a relevant list earn marks even if you can't finish the application.

## What each command word asks for

| Command word | What the examiner wants | CSC 583 example |
|---|---|---|
| **Define** | The courseware definition, as close to word for word as you can; one or two sentences | Define *vulnerability*. |
| **State / List / Name** | The items only, with the **full count**; no explanation needed | State the three impact levels of a security breach. |
| **Explain** | Each item plus *what it means and why it matters*; one to three sentences per point | Explain four of the essential security practices. |
| **Describe** | What it is and how it works, step by step | Describe the hash-based digital signature process. |
| **Differentiate / Distinguish** | Both sides on the **same criteria**, best as a table; one row per criterion | Differentiate between a stateless and a stateful firewall. |
| **Compare** | Similarities **and** differences | Compare WPA2 and WPA3. |
| **Discuss** | Points for and against, or several angles, ending with a judgement | Discuss the challenges of access control in organisations. |
| **Outline** | The main points or stages in order, briefly | Outline the five stages of the wireless security process. |
| **With the aid of a diagram** | A labelled diagram **and** text that refers to it; the diagram carries marks | With the aid of a diagram, explain the security concepts and relationships. |
| **Justify / Recommend** | A choice, the evidence for it, and why not the alternatives | Recommend a firewall type for a hospital and justify your choice. |

!!! tip "Exam angle"
    "List" and "explain" are often in the same part ("List and explain four…"). Then **each** item needs its explanation; a bare list gets about half the marks.

## Answering a recall question

1. **Start with the definition** of the topic, even when the question doesn't ask for it outright. It shows the examiner you know what you're writing about.
2. **Give the number first:** "The courseware lists **thirteen** fundamental security design principles: …". Examiners mark against the full list.
3. **Use the courseware's names** for items (e.g. "Separation of privilege", not "splitting powers"). The names are what the marking scheme contains.
4. **One bold heading per point**, then one to three sentences. It is easier to mark and harder to miss.
5. **For a comparison, use a table** with the criteria as rows.

## The scenario method: I-A-J-A

Applied parts give you a short case and ask what is happening, what should be done, or which option is best. Work through four steps:

1. **Identify** the concept being tested (the attack type, the CIA property, the impact level, the control family).
2. **Apply** it to the scenario's facts. **Quote the facts** ("because the staff member *copied* the records…").
3. **Justify** with the courseware: its definition, list item or example.
4. **Act:** make a recommendation, and say **why it beats the alternatives**.

??? example "Worked example: altered results on a university portal"
    **Scenario.** A Nigerian university's results portal runs over plain HTTP. Students on the open campus Wi-Fi report that results they viewed on their phones were different from the official records, while the database itself was unchanged. *Identify the attack and recommend controls. (8 marks)*

    **Identify.** This is an **active attack**, specifically **modification of messages** or a **man-in-the-middle** attack ([Unit 2](../unit-2-attacks.md#active-attacks)). It breaks **data integrity** ([Unit 1](../unit-1-security-concepts.md#what-computer-security-means-the-cia-triad)).

    **Apply.** The stored records are correct, but the copies *students saw* were different. So the data was changed **in transit**, between the server and the phones, on a network anyone can join.

    **Justify.** Active attacks alter data or its transmission; a passive attack would only read it. Data in transit is protected by cryptographic protocols such as **TLS** ([Unit 4](../unit-4-cryptography.md#cryptographic-protocols-tls-ssl-and-ssh)), which give encryption, authentication of the server through its certificate, and integrity checks.

    **Act.** Serve the portal only over **HTTPS with a TLS/SSL certificate**, and secure the campus Wi-Fi with **WPA2/WPA3** ([Unit 7](../unit-7-wireless-mobile.md#the-four-wireless-network-security-protocols)). A firewall alone would *not* fix this: it filters traffic entering or leaving the network, but it doesn't protect data on the wireless link.

    *Marking points (site's suggestion):* attack identified and classified (2); CIA property (1); use of the scenario facts (2); TLS/HTTPS recommendation with reason (2); why not the alternative (1).

## Diagrams worth practising

Practise drawing each of these in under three minutes. Label every part; the labels carry most of the marks.

| Diagram | Unit | Where to learn it |
|---|---|---|
| Fig. 1: essential network and computer security requirements (5 around "Data and services") | 1 | [Authenticity and accountability](../unit-1-security-concepts.md#beyond-the-triad-authenticity-and-accountability) |
| Security concepts and relationships (owners, countermeasures, risk, assets, threat agents, threats) | 1 | [Concepts and relationships](../unit-1-security-concepts.md#security-concepts-and-relationships) |
| Fig. 2.1 Passive attacks and Fig. 2.2 Active attack | 2 | [Passive attacks](../unit-2-attacks.md#passive-attacks), [Active attacks](../unit-2-attacks.md#active-attacks) |
| Asymmetric encryption (p.26) | 4 | [Asymmetric encryption](../unit-4-cryptography.md#asymmetric-encryption) |
| Fig. 4.1 Hash-based digital signature model, and its verification | 4 | [Signing](../unit-4-cryptography.md#signing-a-document-the-hash-based-model), [Verifying](../unit-4-cryptography.md#verifying-a-digital-signature) |
| SSL handshake (6 steps) | 4 | [SSL](../unit-4-cryptography.md#secure-sockets-layer-ssl) |
| Fig. 6.1 Firewall evolution (four generations) | 5 | [Firewall evolution](../unit-5-firewalls.md#firewall-evolution-the-four-generations) |
| Fig. 6.2 How a firewall works | 5 | [Stateless firewalls](../unit-5-firewalls.md#stateless-firewalls-packet-filtering) |
| Fig. 6.3 NGFW characteristics | 5 | [Next-generation firewalls](../unit-5-firewalls.md#next-generation-firewalls-ngfw) |
| WEP vs WPA vs WPA2 vs WPA3 table (6 rows × 4 protocols) | 7 | [The four protocols](../unit-7-wireless-mobile.md#the-four-wireless-network-security-protocols) |
| Wireless layers of defense (5 stages in order) | 7 | [Layers of defense](../unit-7-wireless-mobile.md#how-wireless-security-works-layers-of-defense) |
| The three malware protection stages | 9 | [Protection stages](../unit-9-malware.md#the-three-malware-protection-stages) |
| IDPS components (sensor/agent, management server, database server, console) | 12 | [IDPS components](../unit-12-idps.md#idps-components) |

## Questions whose counts don't match the courseware

Courseware errors are a trap in the exam: the examiner sets questions from the courseware as printed. **Write the courseware's version**, and add a short clarifying phrase where it helps. The full list of errors is in each unit's Courseware notes.

| Unit | Where the count or list is odd | What to write in the exam |
|---|---|---|
| 1 | **13 design principles** are listed, but *least astonishment* is never explained | Name all 13; explain least astonishment in its standard meaning (a system should behave the way users expect) ([Unit 1](../unit-1-security-concepts.md#least-astonishment)) |
| 1 | The **essential security practices** are not numbered or counted in the source | There are **17**; say "seventeen" if asked to list them |
| 2 | "**Six** categories" of active attack, where the classic textbook list has four | Give the courseware's six: masquerade, replay, modification of messages, MitM, DoS/DDoS, APT ([Unit 2](../unit-2-attacks.md#active-attacks)) |
| 2 | **Avenues of attack** are uncounted, and eavesdropping is buried inside the password paragraph | Seven avenues, including eavesdropping ([Unit 2](../unit-2-attacks.md#avenues-of-attack-on-computer-networks)) |
| 4 | Hashing is listed as one of the three "**encryption**" categories, though hashing is one-way | Give the three categories as listed, then add "hashing is one-way, so it is not true encryption" ([Unit 4](../unit-4-cryptography.md#the-three-categories-of-encryption-techniques)) |
| 4 | Benefits of digital certificates are numbered i, ii, iii, iv, **iv** | There are **five**: security, scalability, authenticity, reliability, public trust ([Unit 4](../unit-4-cryptography.md#benefits-of-digital-certificates)) |
| 4 | SSH is said to authenticate "the client and the server", but all four methods listed are client authentication | Give the four methods; mention that the server proves itself with its host key ([Unit 4](../unit-4-cryptography.md#secure-shell-ssh)) |
| 6 | **17 ISP components** are listed but only two are explained | Name all 17; explain any that are asked using the site's labelled explanations ([Unit 6](../unit-6-security-policy.md#components-of-an-information-security-policy)) |
| 6 | Heading "Policy Weakness" (singular), with **six** uncounted examples | Six policy weaknesses ([Unit 6](../unit-6-security-policy.md#policy-weakness)) |
| 7 | Chapter titled "Wireless **and Mobile** Security" covers only Wi-Fi | Answer mobile questions from the Wi-Fi measures plus the site's labelled mobile notes ([Unit 7](../unit-7-wireless-mobile.md#what-about-mobile-security)) |
| 7 | In the comparison table, WPA3's "Authentication" cell repeats its encryption (AES-CCMP/GCMP) | Reproduce the table as printed if asked to draw it; add that WPA3 authenticates with SAE (Personal) or 802.1X (Enterprise) |
| 9 | Malware types numbered **1–15**, but **16** are named (the worm is inside item 1) | "Fifteen numbered types (sixteen counting worms separately)" ([Unit 9](../unit-9-malware.md#malware-types-that-threaten-pc-and-enterprise-systems)) |
| 9 | "5 ways to strengthen real-time malware protection": the fourth names a vendor product | Give the generic point (AI visibility and governance), not the brand ([Unit 9](../unit-9-malware.md#five-ways-to-strengthen-real-time-malware-protection)) |
| 10 | The case study asks **six** questions, but its "Appropriate Security Approach" answers them in one paragraph | Answer each question separately ([Unit 10](../unit-10-ethics-legal.md#the-case-study-a-vulnerability-in-a-university-website)) |
| 11 | Only the **10 best practices** are numbered; the 6 threats, 5 architecture principles and 3 emerging trends are not | Use those counts; they are the site's but match the printed lists ([Unit 11](../unit-11-database-security.md#common-database-security-threats)) |
| 11 | Best practice 3 says TLS encrypts data **at rest** | TLS protects data **in transit**; data at rest needs storage encryption such as AES ([Unit 11](../unit-11-database-security.md#database-security-best-practices)) |
| 12 | Anomaly-based detection stops mid-sentence; its drawbacks are never stated | Benefit: catches previously unknown threats. Drawbacks (completion from NIST SP 800-94): profiles go out of date, false positives ([Unit 12](../unit-12-idps.md#anomaly-based-detection)) |
| 12 | "IDPS Security Capabilities" covers only tuning and customisation | Answer from what is printed: thresholds, blacklists/whitelists, alert settings, code viewing and editing ([Unit 12](../unit-12-idps.md#idps-security-capabilities-tuning-and-customization)) |

!!! tip "Exam angle"
    When the courseware doesn't give a count, still **state one**: "The courseware gives six common database threats: …". It shows the examiner you know the whole list.

## High-yield lists and their counts

Every named list in the course with its count. In a "list" or "state" question, write the number first, then the items. Each unit's Recall drill has a question for every one of these.

| Unit | List | Count | Learn it |
|---|---|---|---|
| 1 | CIA triad objectives (5 sub-concepts) | 3 | [CIA triad](../unit-1-security-concepts.md#what-computer-security-means-the-cia-triad) |
| 1 | Essential network and computer security requirements (Fig. 1) | 5 | [Authenticity and accountability](../unit-1-security-concepts.md#beyond-the-triad-authenticity-and-accountability) |
| 1 | Things accountability supports | 5 | [Authenticity and accountability](../unit-1-security-concepts.md#beyond-the-triad-authenticity-and-accountability) |
| 1 | Impact levels (each with 4 example effects) | 3 | [Impact levels](../unit-1-security-concepts.md#impact-levels-of-a-security-breach) |
| 1 | Assets of a computer system | 4 | [Assets](../unit-1-security-concepts.md#assets-of-a-computer-system) |
| 1 | Computer security terms | 8 | [Terminology](../unit-1-security-concepts.md#computer-security-terminology) |
| 1 | Essential security practices | 17 | [Essential practices](../unit-1-security-concepts.md#essential-security-practices) |
| 1 | Fundamental security design principles | 13 | [Design principles](../unit-1-security-concepts.md#fundamental-security-design-principles) |
| 2 | Examples of attack surfaces | 5 | [Attack surfaces](../unit-2-attacks.md#attack-surfaces) |
| 2 | Attack surface categories (network, software, human) | 3 | [Categories](../unit-2-attacks.md#categories-of-attack-surface) |
| 2 | Avenues of attack on computer networks | 7 | [Avenues](../unit-2-attacks.md#avenues-of-attack-on-computer-networks) |
| 2 | Main categories of attack (passive, active) | 2 | [What an attack is](../unit-2-attacks.md#what-a-security-attack-is) |
| 2 | Categories of active attack | 6 | [Active attacks](../unit-2-attacks.md#active-attacks) |
| 2 | Groups of attackers (hackers, crackers, scriptkiddies) | 3 | [Attackers](../unit-2-attacks.md#hackers-crackers-and-scriptkiddies) |
| 3 | OS vulnerabilities | 8 | [Vulnerabilities](../unit-3-os-security.md#vulnerabilities-of-operating-systems) |
| 3 | OS threats | 8 | [Threats](../unit-3-os-security.md#threats-to-operating-systems) |
| 3 | Security measures to protect operating systems (2 points each) | 13 | [Measures](../unit-3-os-security.md#security-measures-to-protect-operating-systems) |
| 4 | Applications of cryptography | 5 | [Why cryptography matters](../unit-4-cryptography.md#why-cryptography-matters-five-applications) |
| 4 | Categories of encryption techniques (plus hybrid) | 3 | [Categories](../unit-4-cryptography.md#the-three-categories-of-encryption-techniques) |
| 4 | Symmetric algorithm entries | 5 | [Symmetric encryption](../unit-4-cryptography.md#symmetric-encryption) |
| 4 | Main features of asymmetric encryption | 4 | [Asymmetric features](../unit-4-cryptography.md#main-features-of-asymmetric-encryption) |
| 4 | Working points of a hash function | 6 | [How a hash works](../unit-4-cryptography.md#how-a-cryptographic-hash-function-works) |
| 4 | Properties of hash functions | 6 | [Properties](../unit-4-cryptography.md#properties-of-cryptographic-hash-functions) |
| 4 | Applications of hash functions | 3 | [Applications](../unit-4-cryptography.md#applications-of-cryptographic-hash-functions) |
| 4 | Popular hash algorithms | 5 | [Algorithms](../unit-4-cryptography.md#popular-cryptographic-hash-algorithms) |
| 4 | SSL features / SSL handshake steps | 5 / 6 | [SSL](../unit-4-cryptography.md#secure-sockets-layer-ssl) |
| 4 | SSH overview points / SSH authentication methods | 7 / 4 | [SSH](../unit-4-cryptography.md#secure-shell-ssh) |
| 4 | Properties of a signature / additional requirements for a digital signature | 5 / 4 | [Digital signatures](../unit-4-cryptography.md#digital-signatures) |
| 4 | Types of public key certificate / forms of TLS/SSL certificate (DV, OV, EV) | 3 / 3 | [Digital certificates](../unit-4-cryptography.md#digital-certificates) |
| 4 | Benefits of digital certificates | 5 | [Benefits](../unit-4-cryptography.md#benefits-of-digital-certificates) |
| 5 | Firewall functions (NAT, VPN) | 2 | [NAT and VPN](../unit-5-firewalls.md#firewall-functions-nat-and-vpn) |
| 5 | Generations of firewall evolution | 4 | [Evolution](../unit-5-firewalls.md#firewall-evolution-the-four-generations) |
| 5 | NGFW characteristics in Fig. 6.3 | 3 | [NGFW](../unit-5-firewalls.md#next-generation-firewalls-ngfw) |
| 5 | Hybrid mesh firewall form factors | 3 | [Hybrid mesh](../unit-5-firewalls.md#hybrid-mesh-firewalls) |
| 6 | Core reasons for an information security policy | 7 | [Why organisations need one](../unit-6-security-policy.md#why-organisations-need-an-information-security-policy) |
| 6 | Components of an information security policy | 17 | [Components](../unit-6-security-policy.md#components-of-an-information-security-policy) |
| 6 | Policy weaknesses | 6 | [Policy weakness](../unit-6-security-policy.md#policy-weakness) |
| 7 | Wireless security measures | 6 | [Six measures](../unit-7-wireless-mobile.md#why-wireless-networks-are-exposed-and-the-six-security-measures) |
| 7 | Layers of defense (stages, in order) | 5 | [Layers of defense](../unit-7-wireless-mobile.md#how-wireless-security-works-layers-of-defense) |
| 7 | Things wireless security involves | 5 | [Five things](../unit-7-wireless-mobile.md#the-five-things-wireless-security-involves) |
| 7 | Wireless security protocols (WEP 1997, WPA 2003, WPA2 2004, WPA3 2018) | 4 | [Protocols](../unit-7-wireless-mobile.md#the-four-wireless-network-security-protocols) |
| 7 | Types of WPA3 | 3 | [Each protocol](../unit-7-wireless-mobile.md#each-protocol-in-detail) |
| 8 | Key aspects of access control (physical, logical) | 2 | [Key aspects](../unit-8-access-control.md#key-aspects-of-access-control-physical-and-logical) |
| 8 | Benefits of access control | 3 | [Why it matters](../unit-8-access-control.md#why-access-control-is-important-for-security) |
| 8 | Types of access control system (DAC, MAC, RBAC, ABAC, RuBAC) | 5 | [Types](../unit-8-access-control.md#types-of-access-control-systems) |
| 8 | Components of an effective access control system | 5 | [Components](../unit-8-access-control.md#components-of-an-effective-access-control-system) |
| 8 | Challenges in access control | 4 | [Challenges](../unit-8-access-control.md#challenges-in-access-control) |
| 8 | Best practices for access control | 5 | [Best practices](../unit-8-access-control.md#best-practices-for-access-control-implementation) |
| 8 | Advantages of NAC / types of NAC | 7 / 2 | [NAC](../unit-8-access-control.md#network-access-control-nac) |
| 9 | Malware protection stages | 3 | [Stages](../unit-9-malware.md#the-three-malware-protection-stages) |
| 9 | Critical malware protection technologies | 6 | [Technologies](../unit-9-malware.md#critical-malware-protection-technologies) |
| 9 | Malware types | 15 (16) | [Types](../unit-9-malware.md#malware-types-that-threaten-pc-and-enterprise-systems) |
| 9 | Malware protection best practices | 11 | [Best practices](../unit-9-malware.md#malware-protection-best-practices) |
| 9 | Organisational malware strategies | 3 | [Strategies](../unit-9-malware.md#organizational-malware-strategies) |
| 9 | Factors in malware protection vs antivirus | 5 | [Versus antivirus](../unit-9-malware.md#malware-protection-versus-antivirus) |
| 9 | Ways to strengthen real-time malware protection | 5 | [Five ways](../unit-9-malware.md#five-ways-to-strengthen-real-time-malware-protection) |
| 10 | Ethical issues / legal issues | 6 / 5 | [Ethics and law](../unit-10-ethics-legal.md#ethics-and-law-in-information-security) |
| 10 | Professional responsibilities | 7 | [Professional responsibility](../unit-10-ethics-legal.md#professional-responsibility) |
| 10 | Requirements for ethical hacking | 5 | [Ethical hacking](../unit-10-ethics-legal.md#ethical-hacking) |
| 10 | Activities of digital forensics / examples of digital evidence | 5 / 6 | [Forensics](../unit-10-ethics-legal.md#digital-evidence-and-forensics) |
| 10 | Ethical principles for security professionals | 9 | [Principles](../unit-10-ethics-legal.md#ethical-principles-for-security-professionals) |
| 10 | Rows of the ethical vs legal table | 4 | [Ethical vs legal](../unit-10-ethics-legal.md#ethical-vs-legal-issues) |
| 11 | Common database threats | 6 | [Threats](../unit-11-database-security.md#common-database-security-threats) |
| 11 | Database security best practices | 10 | [Best practices](../unit-11-database-security.md#database-security-best-practices) |
| 11 | Principles of database security architecture | 5 | [Architecture](../unit-11-database-security.md#key-principles-of-database-security-architecture) |
| 11 | Emerging trends | 3 | [Trends](../unit-11-database-security.md#emerging-trends-in-database-security) |
| 12 | Uses of an IDPS | 5 | [Uses](../unit-12-idps.md#what-an-idps-is-used-for) |
| 12 | Groups of IPS response techniques | 3 | [IPS responses](../unit-12-idps.md#how-an-ips-responds-three-groups-of-response-techniques) |
| 12 | Detection methodologies (signature, anomaly, stateful protocol analysis) | 3 | [Methodologies](../unit-12-idps.md#idps-detection-methodologies) |
| 12 | IDPS components | 4 | [Components](../unit-12-idps.md#idps-components) |
| 12 | Types of IDPS technology (network-based, wireless, NBA, host-based) | 4 | [Types](../unit-12-idps.md#types-of-idps-technologies) |

## Memory aids

!!! note "In plain terms"
    These memory aids are **the site's**, not the courseware's. Use them to recall a list, then write the courseware's names in the exam.

- **CIA + AA:** Confidentiality, Integrity, Availability, plus **A**uthenticity and **A**ccountability (Unit 1).
- **Impact levels, "limited, serious, severe":** Low = *limited* adverse effect, Moderate = *serious*, High = *severe or catastrophic* (Unit 1).
- **Firewall generations, "Please Stop All Nonsense":** **P**acket filter (stateless), **S**tateful, **A**pplication-level gateway, **N**ext-generation (Unit 5).
- **Wi-Fi dates, "97, 03, 04, 18":** WEP, WPA, WPA2, WPA3 (Unit 7).
- **Access control models, "D-M-R-A-R":** DAC, MAC, RBAC, ABAC, RuBAC: from the owner deciding, to a central authority, to the job role, to attributes, to rules (Unit 8).
- **Malware stages, "before, during, after":** pre-execution, runtime, post-execution (Unit 9).
- **IPS responses, "stop it, change the place, change the payload":** stops the attack itself, changes the security environment, changes the attack's content (Unit 12).
- **Detection methods, "S-A-S":** Signature, Anomaly, Stateful protocol analysis (Unit 12).

## Common mistakes

1. **Mixing up threat and vulnerability.** A vulnerability is a weakness; a threat is "any circumstance or event with the potential to adversely impact" the organisation through an information system, usually by exploiting a vulnerability ([Unit 1](../unit-1-security-concepts.md#computer-security-terminology)).
2. **Saying a passive attack changes data.** Passive attacks only monitor; they threaten confidentiality. Active attacks alter ([Unit 2](../unit-2-attacks.md#what-a-security-attack-is)).
3. **Calling hashing encryption.** A hash is one-way; there is no key to reverse it ([Unit 4](../unit-4-cryptography.md#cryptographic-hash-functions)).
4. **Confusing a digital signature with a digital certificate.** The signature proves who signed and that nothing changed; the certificate binds a public key to an identity and is issued by a CA ([Unit 4](../unit-4-cryptography.md#digital-certificate-vs-digital-signature)).
5. **Mixing up stateless and stateful firewalls.** Stateless checks each packet alone against rules; stateful tracks connections ([Unit 5](../unit-5-firewalls.md#comparing-the-four-firewall-types)).
6. **Treating IDS and IPS as the same.** An IDS detects and alerts; an IPS also tries to stop the incident ([Unit 12](../unit-12-idps.md#intrusion-detection-ids-ips-and-idps)).
7. **Treating "legal" as "ethical".** Something can be legal but ethically questionable ([Unit 10](../unit-10-ethics-legal.md#ethical-vs-legal-issues)).
8. **Writing fewer items than the count**, or mixing items from two lists (e.g. Unit 3's OS security measures with Unit 1's essential practices).
9. **Recommending without justifying.** In a scenario part, the "why not the alternatives" sentence is often worth a mark on its own.
10. **Drawing an unlabelled diagram.** Labels and arrows carry the marks.

## Seven-day revision plan

Each day: read the units, answer their "Check your understanding" MCQs, then **work through the Recall drill without opening the answers**. Write down every one you miss, and redo only those the next morning.

| Day | Units | Extra |
|---|---|---|
| 1 | [1 Security concepts](../unit-1-security-concepts.md), [2 Attacks](../unit-2-attacks.md) | Draw Fig. 1 and the concepts-and-relationships diagram |
| 2 | [3 OS security](../unit-3-os-security.md), [6 Security policy](../unit-6-security-policy.md) | Recite the 17 ISP components |
| 3 | [4 Cryptography](../unit-4-cryptography.md) | Draw Fig. 4.1 and the SSL handshake |
| 4 | [5 Firewalls](../unit-5-firewalls.md), [7 Wireless and mobile](../unit-7-wireless-mobile.md) | Draw Fig. 6.1 and the WEP–WPA3 table |
| 5 | [8 Access control](../unit-8-access-control.md), [9 Malware](../unit-9-malware.md) | Sort the 16 malware types into groups |
| 6 | [10 Ethics and legal](../unit-10-ethics-legal.md), [11 Database security](../unit-11-database-security.md), [12 IDPS](../unit-12-idps.md) | Answer the Unit 10 case study aloud |
| 7 | All | Sit [Mock exam 1](mock-exam-1.md) under time; mark it; read the [crash course](crash-course.md); sit [Mock exam 2](mock-exam-2.md) if time allows |
